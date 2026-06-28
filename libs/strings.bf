#=======================================================================================================================
#                                                  STRING
#=======================================================================================================================

#print
print/                 # 0 - arr
r:arg0As
[. > 0]                # all sring
10+ . Rv               # endl
=                      # return

endl/
Rv 10+ . Rv            # endl

#len
len/                   # 0 - arr 0 - ret
1As Rv $0+             # save pointer
0As -                  # pointer -= 1
[ 0As+ $0As 0]         # counter
0As $1-                # end - start + 1
=                      # return

#input
input/
:iAs <
[> ,. 0]             # buffer to string array
=

