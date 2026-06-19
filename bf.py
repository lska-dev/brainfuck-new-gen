class VM():
    def __init__(self, ln):
        self.ram = []
        self.debug = False
        self.stack = []
        self.pc = 0
        self.ap = 0
        self.program = []
        self.input_buffer = []

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

    def compile(self,str):
        str = str.replace(' ', "")
        str = str.replace('\n', "")
        self.program = []
        s = ""
        for c in str:
            if c in "+-[].,h<>raj":
                if s == '':
                    self.program.append([c, 1])
                else:
                    self.program.append([c, s])
                s = ""
            else:
                s = f"{s}{c}"
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
print(f"Process finished with exit code {v.run(code)}")








