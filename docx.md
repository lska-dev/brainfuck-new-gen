# commands
## update 1:
add number argument:
{command}{number}

`{n}+` value += n or 1
`{n}-` value -= n or 1
`{n}>` ap += n or 1
`{n}<` ap -= n or 1

`[` loop start point
`{n}]` loop end operator, jmp to start if value != n
`.` print ASCII charapter on value
`,` console input on input buffer head to value

`Call` call
`Rv` reset value
`{n}As` set ap
`{n}Jmp` set pc
`Hex` console hex out
`=` return value
`{name}/` label
`{name}Define{value}EndDef` define

`{path or name}Import` 
`{n}Mul` 
`{n}Div`
`{n}FDiv`

## supported number types:
| prefix | type                         |
|:------:|------------------------------|
|        | dec                          |
|  `0x`  | hex                          |
|  `0b`  | bin                          |
|  `0o`  | oct                          |
|  `$n`  | pointer: var->memory, ap, pc |
|  `''`  | ASCII                        |
|  `:`   | label                        |
|  `r`   | get register                 |
|  `@`   | get next empty label         |

---

# Default libs

## 1.FRL (F#ck Rules Language)
default library **FRL** give defined for default Registers VM
### register table
|   mnemonic    | description          |
|:-------------:|:---------------------|
| `arg0-arg7`   | positional arguments |
|  `tmp0-tmp7`  | temporary            |

### read register
brainfuck ``
#read register tmp0
0As Rv #clear value
r:tmp0+ #tmp0 -> value
``
### write register
brainfuck `` 
#write $0 to register tmp0
Rv $0+ #get $0

``
