
class VM():
    def __init__(self):
        self.memory = []
        self.regs = {"r0":0, "r1":0, "r2":0, "r3":0}
        self.flags = {"C":False, "B":False, "Z":False, "N":False}

    def exp(self, No):
        print("pizda")

    def read(self, a):
        if a < len(self.memory):
            return self.memory[a]
        else:
            VM.exp(0)
            return 0

    def write(self, a, d):
        if a < len(self.memory):
            self.memory[a] = d
        else:
            VM.exp(0)

    def rwr(self, r, d):
        if r in self.regs:
            self.regs[r] = d
        else:
            VM.exp(1)

    def rrd(self, r):
        if r in self.regs:
            return self.regs[r]
        else:
            return 0

    def GetNum(self, str):
        n = 0
        if str[0] == "r":
            n = self.rrd(str)
        elif str.startswith("0x"):
            n = int(str, 16)
        elif str.startswith("0b"):
            n = int(str, 2)
        elif str.startswith("0o"):
            n = int(str, 8)
        elif "." in str:
            n = float(str)
        else:
            n = int(str,10)

        return n


    def math(self, str):
        tokens = str.split()

        if len(tokens) != 3:
            print(f"parse Expression: {str} to low pos args")
            return 0

        a = self.GetNum(tokens[0])
        op = tokens[1]
        b = self.GetNum(tokens[2])

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == ">>":
            return a >> b
        elif op == "<<":
            return a << b
        elif op == "&":
            return a & b
        elif op == "|":
            return a | b
        elif op == "^":
            return a ^ b
        elif op == "==":
            if a == b:return 1
            else: return 0
        elif op == ">":
            if a > b:return 1
            else: return 0
        elif op == "<":
            if a < b:return 1
            else: return 0
        elif op == ">=":
            if a >= b:return 1
            else: return 0
        elif op == "<=":
            if a <= b:return 1
            else: return 0
        elif op == "!=":
            if a != b:return 1
            else: return 0
        else:
            print(f"invalid operator {op} of {str}")
            return 0

    def funtion(self,str):
        agv = str.split(":")
        ins = agv[0]

        if ins == "RLET":
            m = self.math(agv[2])
            self.rwr(agv[1],m)


v = VM()
v.funtion("RLET:r1:123 + 0")
print(v.regs)