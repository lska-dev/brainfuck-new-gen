
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
|"$n"| mem[[n]] |
|"''"| ASCII |

"rv" reset value
{n}"as" set ap
{n}"jmp" set pc
"hex" console hex out


