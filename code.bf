main_os_var Define 100 EndDef
:main Jmp

#mul
mul/
100As Rv $0+  101As Rv $1+ 2As Rv #copy
[ 2As $100+ 101As - 0] =


print/
0As Rv 10+ . Rv 'e'+ . Rv 'x'+ . Rv 'i'+ . Rv 't'+ . = #->exit

main/

0As , 1As ,
:mul Call
2As 2As Hex Rv
:print Call

.............................
