# commands
all language ignore spaces and returns, comment: `#` to `\n`
## update 1:

`{n}+` value += n or 1

`{n}-` value -= n or 1

`{n}>` ap += n or 1

`{n}<` ap -= n or 1

`[` loop start point

`{n}]` loop end operator, jmp to start if value != n

`.` print ASCII charapter on value

`,` console input on input buffer head to value

## extend operations

---
### compiler
`{name}/` label on code

`{name}Define{value}EndDef` define name = value

`{path}Import` inline module .bf {path} without aplification 

---
### value
`{n}Rset` set register

`Rv` reset value

`{n}As` set ap

`Hex` console hex out

---
### math

`{n}Mul`  value = val * n

`{n}Div`  value = val // n

`{n}FDiv` value = val / n 

---
### logical
logical operations set flag LG Asses on `$LG`

`{n}== val` if value == n

`{n}> val` if n > value

`{n}< val` if n < value

`{n}And val` n and value

`{n}Or val` n or value

`Not val` not value


---
### program control

`:{label}Jmp` jump to label 

`:{label}Call` call label

`:{label}IfJmp` jump to label if LG(True)

`:{label}IfCall` call label if LG(True)

`=` return on function

## supported number types:
| prefix | type                             |
|:------:|----------------------------------|
|        | dec                              |
|  `0x`  | hex                              |
|  `0b`  | bin                              |
|  `0o`  | oct                              |
|  `$n`  | pointer: var->memory, ap, pc, LG |
|  `''`  | ASCII                            |
|  `:`   | label                            |
|  `r`   | get register                     |


---

# Default libs

## 1.FRL (F#ck Rules Language)
default library **FRL** replace index to label for manual asses on default Registers VM
### register table
|   mnemonic    | description          |
|:-------------:|:---------------------|
| `arg0-arg7`   | positional arguments |
|  `tmp0-tmp7`  | temporary            |

### read register
``````
#read register tmp0
0As Rv #clear value
r:tmp0+ #tmp0 -> value
``````
### write register
``````
#write $0 to register tmp0
Rv $0+ #get $0
``````
