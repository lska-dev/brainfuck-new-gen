
update 1:
add number argument:
{command}{number}

{n}"+" add n or increment memory[[ap]] ,if n = '' 
{n}"-" sub n or decrement memory[[ap]] ,if n = ''
{n}">" add n or increment ap ,if n = ''
{n}"<" sub n or decrement ap ,if n = ''

"[" loop start point
{n}"]" loop end operator, jmp to start if memory[[ap]] != n
"." print ASCII charapter memory[[ap]]
"," console input on input buffer head to memory[[ap]]

supported n types:
|m|type|
|--|--|
|""| dec |
|"0x"| hex |
|"0b"| bin |
|"0o"| oct |
|"$n"| pointer: var->memory, ap, pc |
|"''"| ASCII |
|":"| label |

"Call" call
"Rv" reset value
{n}"As" set ap
{n}"Jmp" set pc
"Hex" console hex out
"=" return value
{name}"/" label
{name}"Define"{value}"EndDef" define

:all_testsJmpprint/$0As[.>0]10+.:1Rv=len/1AsRv$0+0As-[0As+$0As0]0As$1-=input/:iAs<[>,.0]=Rvconsole/:'a'+.HexRv10+.==counterr/:counterAsRv[:counterAsHex:valAs''+.Rv:counterAs+10]=ar1Set/:ar1As10+>'h'+>'e'+>'l'+>'l'+>'o'+>''+>'w'+>'o'+>'r'+>'l'+>'d'+>'!'+>Rv0As=all_tests/counterDefine0EndDefvalDefine1EndDefar1Define0x80EndDefiDefine0xffEndDef:ar1SetCall.:consoleCall.:counterrCall.0AsRv:ar1+:printCall0AsRv:ar1+:lenCall0AsHex:inputCall0As10+.0AsRv:i:printCall0AsRv:i:lenCall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^Ты блять долбаеб, нахуй!
