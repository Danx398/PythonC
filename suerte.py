F = []
N = input().split(' ')
S = input().split(' ')

def sobreescribir(a):        
    S[int(a[1])-1] = int(a[2])
    
def obtener_min_max(c):
    mm =  S[(int(c[1])-1):int(c[2])]
    j = 0
    for i in mm:
        mm[j] = int(i)
        j += 1   
    mm.sort() 
    F.append(str(mm[0]) + ' '+ str(mm[len(mm)-1]))

def mostrar_resultado():
    for i in F:
        print(i)

for i in range(int(N[1])):
    if i%2 == 0:
        obtener_min_max(input().split(' '))
    else:
        sobreescribir(input().split(' '))
        
mostrar_resultado()