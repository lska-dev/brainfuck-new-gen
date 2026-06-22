errors = {
    -2 : "COMPILE ERROR",
    -1 : "EXECPTION",
     0 : ""
}



class VM():
    def __init__(self, ln):
        self.ln = ln
        self.ram = []
        self.debug = False
        self.stack = []
        self.pc = 0
        self.ap = 0
        self.program = []
        self.input_buffer = []
        self.labels = {}
        self.callStack = []
        self.returnValue = 0
        self.lib = ""; self.raw_pointer = 0; self.raw_inst_len = 0; self.raw_code = {}

        self.tokens = [
            #default
            "+", "-", ">", "<", "[", "]", ".", ",",
            #extend1
            "Rv", "As", "Jmp", "Hex", "=", "Call",
            #compiler
            "/", "Define", "EndDef", "Import",
            #spec
            "nope"
        ]
        self.tokenMaxLen = 6

        for i in range(ln):
            self.ram.append(0)

    def mem_read(self):
        #print(f"read {self.ap}")
        if self.ap < self.ln:
            return self.ram[self.ap]
        else:
            self.raise_op()
            print(f"to high adress {self.ap}")
            return None

    def mem_write(self, d):
        if self.ap < self.ln:
            self.ram[self.ap] = d
            return 1
        else:
            self.raise_op()
            print(f"to high adress {self.ap}")
            return 0

    def dbg(self):
        self.debug = True

    def raise_op(self):
        #pn = self.raw_code[self.raw_pointer - 25:self.raw_pointer + 25]
        print(f"\n\n\x1b[31mInterupt in {self.lib}:\n{self.raw_code[self.lib]}\n{"~" * (self.raw_pointer+2)}{"^" * self.raw_inst_len}Ты блять долбаеб, нахуй!")

    def import_file(self, path):
        try:
            f = open(path+".bf", "r")
            code = f.read()
            f.close()
        except FileNotFoundError:
            try:
                f = open(f"libs/{path}.bf", "r")
                code = f.read()
                f.close()
            except FileNotFoundError:
                self.raise_op()
                print(f"libraly {path} not found")
                return 0
        return code


    def inst(self, op):
        s = op[0]
        n = self.getNum(op[1])

        self.lib = op[2]
        self.raw_pointer = op[3]
        self.raw_inst_len = op[4]

        if s == "+":
            e = self.mem_read()
            if e == None: return 0
            self.mem_write(e + n)

        elif s == "-":
            e = self.mem_read()
            if e == None:return 0
            self.mem_write(e-n)

        elif s == ">":
            self.ap += n

        elif s == "<":
            self.ap -= n
            if self.ap < 0: self.ap = 0

        elif s == ".":
            e = self.mem_read()
            if e == None: return 0
            print(chr(e & 0x7F),end='')

        elif s == "Hex":
            e = self.mem_read()
            if e == None: return 0
            print(hex(e), end='')

        elif s == ",":
            if len(self.input_buffer) == 0:
                for c in input(''):
                    self.input_buffer.append(c)
                self.input_buffer.append("\x00")
            if len(self.input_buffer) > 0:
                e = self.mem_write(ord(self.input_buffer.pop(0)))
                if e == 0: return 0

        elif s == "[":
            self.stack.append(self.pc)

        elif s == "]":
            if self.ram[self.ap] != n:
                self.pc = self.stack.pop(len(self.stack)-1)-1

        elif s == 'Rv':
            e = self.mem_write(0)
            if e == 0: return 0

        elif s == 'As':
            self.ap = n

        elif s == 'Jmp':
            self.pc = n

        elif s == 'Call':
            self.callStack.append(self.pc + 1)
            self.pc = n

        elif s == '=':
            self.pc  = self.callStack.pop(-1)



        return 1
    @staticmethod
    def getNumberSS(s):
        if s.startswith("0x"):
            return int(s,16)
        elif s.startswith("0b"):
            return int(s, 2)
        elif s.startswith("0o"):
            return int(s, 8)
        elif s.startswith("'") and s.endswith("'"):
            if len(s) > 3:
                print("no")
                return 0
            else:
                return ord(s[1])
        else:
            return int(s,10)

    def getNum(self,st):
        s = str(st)
        if s.startswith("$"):
            s = s.split("$")[1]
            if s == "ap":
                return self.ap
            elif s == "pc":
                return self.pc
            else:
                ap = VM.getNumberSS(s)
                return self.ram[ap]

        elif s.startswith(":"):
            l = s.split(":")[1]
            if l in self.labels:
                return self.labels[l]
            else:
                self.raise_op()
                print(f"name {l} is not defined")
                return 0

        else:
            return VM.getNumberSS(s)

    @staticmethod
    def parse(s,list, ml):
        for i in range(ml):
            op = s[len(s)-1-i:]
            n = s[:len(s)-1-i]
            if op in list:
                if n == '': n = "1"
                #tockens
                return [op,n]
        #print(f"invalid instruction {s}")
        return -1


    def compile(self,str):
        code = ""
        in_comment = False
        #clear comments
        for c in str:
            if c == "#" and not in_comment: in_comment = True #start
            if c == "\n" and in_comment: in_comment = False #end
            if not in_comment:
                if c != '\n' and c != ' ': code = code + c

        print(code)

        self.program = []
        s = ""
        for i in range(len(code)):
            s = f"{s}{code[i]}"
            parse = VM.parse(s, self.tokens, self.tokenMaxLen)

            if parse != -1:
                if parse[0] == "Import":
                    print(f"Importing {parse[1]} lib ")
                    self.lib = parse[1]
                    tmp = self.program
                    lib = self.import_file(parse[1])
                    if lib == 0: return 0  # err
                    lib = self.compile(lib)  # recurse
                    if lib == 0: return 0  # recurse error
                    self.program = tmp + self.program
                    self.lib = ""
                else:

                    self.program.append(parse + [self.lib, i, len(f"{parse[0]}{parse[1]}")])
                    s = ""

        #labels generation and check operations и я хз как это назвать
        for i in range(len(self.program)):
            c = self.program[i][0]
            n = self.program[i][1]

            if c == "/":
                self.labels[n] = i
                self.program[i] = ['nope', '0', '', 0, 0]

            if c == "EndDef":
                if self.program[i-1][0] != "Define":
                    self.raise_op()
                    print("expected Define before EndDef")
                    return 0
                self.labels[self.program[i - 1][1]] = self.getNum(self.program[i][1])
                self.program[i] = ['nope', '0', '', 0, 0]
                self.program[i - 1] = ['nope', '0', '', 0, 0]

            if not c in self.tokens:
                self.raise_op()
                print(f"invalid operation {c}")
                return 0

        if not self.lib in self.raw_code: self.raw_code[self.lib] = code





        print(self.program)
        print(self.labels)
        print("bytecode is generate")
        return 1

    def run(self,str):
        print("run VM")
        if self.compile(str) == 0: return -2 #compile error
        print("\n\n\n")
        while self.pc < len(self.program):

            """ FIX IT """
            if self.debug:
                print(self.program)
                print(f"\r{'^' * self.pc}")
            """ FIX IT """

            if self.inst(self.program[self.pc]) == 0:return -1
            self.pc += 1

        return 0

v = VM(1000)
#v.dbg()
f = open("code.bf", "r")
code = f.read()
f.close()


tread = v.run(code)
print(f"INTPR Process finished with exit code {tread} ({errors[tread]})")








