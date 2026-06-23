#test bf program

:all_tests Jmp
std Import

#console
Rv
console/
'a'+ .                 # set and print 'a'
Hex                    # hex ASCII code
Rv 10+ .               # \n
= =

#defines

#cycle
counterr/
:counter As Rv         # reset counter
[                                     #for...
:counter As
Hex                    # out counter
:val As ' '+ . Rv      # out spase
:counter As +          # counter ++
10]                                   # counter = 0; counter <= 10; counter ++
=

#arrays
ar1Set/
:ar1 As                # ar1 = "\n hello world"
10+ >
'h'+ > 'e'+ >
'l'+ > 'l'+ >
'o'+ > ' '+ >
'w'+ > 'o'+ >
'r'+ > 'l'+ >
'd'+ > '!'+ > Rv       # terminator
0As =



all_tests/

counter Define 0 EndDef
val Define 1 EndDef
ar1 Define 0x80 EndDef
i Define 0xff EndDef

:ar1Set Call .
:console Call .
:counterr Call .

0As Rv :ar1+           # pointer to ar1
:print Call            # print
0As Rv :ar1+           # pointer to ar1
:len Call 0As Hex      # print len

:input Call            # input
0As 10+ .
0As Rv :i              # pointer to input
:print Call            # echo
0As Rv :1i              # pointer to input
:len Call

v = VM(1000)
#v.dbg()
f = open("code.bf", "r")
code = f.read()
f.close()


tread = v.run(code)
print(f"INTPR Process finished with exit code {tread} ({errors[tread]})")