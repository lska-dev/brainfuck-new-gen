class VM():
    def __init__(self, ln):
        self.ram = []
        self.debug = False
        self.stack = []
        self.pc = 0
        self.ap = 0

        self.input_buffer = ""

        for i in range(ln):
            self.ram.append(0)

    def dbg(self):
        self.debug = True

    def inst(self, op):
        s = op[0]
        n = 1
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
                self.input_buffer = input('')
            self.ram[self.ap] = ord(self.input_buffer[0])
            self.input_buffer = self.input_buffer[1:]

        elif s == "[":
            self.stack.append(self.pc)

        elif s == "]":
            if self.ram[self.ap] != n:
                self.pc = self.stack.pop(len(self.stack)-1)-1

        return 1

    def run(self,prog):
        while self.pc < len(prog):
            if self.debug:
                print(prog)
                print(f"\r{'^' * self.pc}")
            if self.inst(prog[self.pc]) == 0:return 0
            self.pc += 1

        return 1

v = VM(1000)
#v.dbg()
v.run("[,.]")







