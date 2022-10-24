cadena= input()
final = []
dicconario = {
'A' : 'Alfa ',
'N' : 'November ',
'1' : 'One',
'B' : 'Bravo ',
'O' : 'Oscar ',
'2' : 'Two',
'C' : 'Charlie ',
'P' : 'Papa ',
'3' : 'Three',
'D' : 'Delta ',
'Q' : 'Quebec ',
'4' : 'Four',
'E' : 'Echo ',
'R' : 'Romeo ',
'5' : 'Five',
'F' : 'Foxtrot S',
'S' :'sierra ',
'6' :' Six',
'G' : 'Golf ',
'T' : 'Tango ',
'7' : 'Seven',
'H' : 'Hotel ',
'U' : 'Uniform ',
'8' : 'Eight',
'I' : 'India ',
'V' : 'Victor ',
'9' : 'Nine',
'J' : 'Juliett ',
'W' : 'Whiskey ',
'0' : 'Zero',
'K' : 'Kilo ',
'X' : 'X-Ray ',
'.' : 'Decimal',
'L': 'Lima ',
'Y': 'Yankee',
'M': 'Mike ',
'Z': 'Zulu',
}

code = ['','','double', 'triple', 'quadruple' ,'quintuple']
nueva = {}
valor=''
for i in cadena:
    if i != ' ':
        final.append(dicconario[i.upper()])
        
for j in final: 
    if j in nueva:
        if j == valor:
            nueva[j] += int(1)
    else:
        nueva[j] = int(1)
    valor = j
    
for k,v in nueva.items():
    if v > 1:
        if v > 5:
            print(code[5],k, end= ' ') 
            print(code[int(v)-5],k, end= ' ')
        else:
            print(code[int(v)],k, end= ' ')
    else: 
        print(k, end= ' ')