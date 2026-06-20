class VM():
    def __init__(self, ln):
        self.ram = []
        self.debug = False
        self.stack = []
        self.pc = 0
        self.ap = 0
        self.program = []
        self.input_buffer = []

        self.tokens = [
            #default
            "+", "-", ">", "<", "[", "]", ".", ",",
            #extend1
            "Rv", "As", "Jmp", "Hex"
        ]
        self.tokenMaxLen = 3

        for i in range(ln):
            self.ram.append(0)

    def dbg(self):
        self.debug = True

    def inst(self, op):
        s = op[0]
        n = self.getNum(op[1])
        if s == "+":
            self.ram[self.ap] += n

        elif s == "-":
            self.ram[self.ap] -= n

        elif s == ">":
            self.ap += n
            if self.ap > len(self.ram):
                print("esc ap")
                return 0

        elif s == "<":
            self.ap -= n
            if self.ap < 0: self.ap = 0

        elif s == ".":
            print(chr(self.ram[self.ap] & 0x7F),end='')
        elif s == "h":
            print(hex(self.ram[self.ap]),end='')

        elif s == ",":
            if len(self.input_buffer) == 0:
                for c in input(''):
                    self.input_buffer.append(c)
            if len(self.input_buffer) > 0:
                self.ram[self.ap] = ord(self.input_buffer.pop(0))


        elif s == "[":
            self.stack.append(self.pc)

        elif s == "]":
            if self.ram[self.ap] != n:
                self.pc = self.stack.pop(len(self.stack)-1)-1

        elif s == 'r':
            self.ram[self.ap] = 0

        elif s == 'a':
            self.ap = n

        elif s == 'j':
            self.pc = n


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
            ap = VM.getNumberSS(s.split("$")[1])
            return self.ram[ap]
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
        for c in code:
            s = f"{s}{c}"
            parse = VM.parse(s, self.tokens, self.tokenMaxLen)
            if parse != -1:
                self.program.append(parse)
                s = ""
        print(self.program)
        print("bytecode is generate")
        return 0

    def run(self,str):
        print("run VM")
        if self.compile(str) == 1:
            return -2

        while self.pc < len(self.program):
            if self.debug:
                print(self.program)
                print(f"\r{'^' * self.pc}")
            if self.inst(self.program[self.pc]) == 0:return 0
            self.pc += 1

        return 1

v = VM(1000)
#v.dbg()
f = open("code.bf", "r")
code = f.read()
print(f"INTPR Process finished with exit code {v.run(code)}")
print()







