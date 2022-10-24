t1 = list(input().split(' '))
t2 = list(input().split(' '))
t1x = list()
t1y = list()
t2x = list()
t2y = list()

for i,t in enumerate(t1):
    if(int(i)%2 != 0):
        t1y.append(int(t1[i]))
        t2y.append(int(t2[i]))
         #print('y',i, t1[i],t2[i])
    if(int(i)%2 == 0):
        t1x.append(int(t1[i]))
        t2x.append(int(t2[i]))
         #print('x',i, t1[i],t2[i])
i=0
fuera = 0
 #for i,t in enumerate(t1x):
 #if((i+1)==1):

""" T1X1,T1Y1,T1X2,T1Y2,T1X3,T1Y3,T1X4,T1Y4 = input().split()
lista1 = [T1X1,T1Y1,T1X2,T1Y2,T1X3,T1Y3,T1X4,T1Y4] 
T2X1,T2Y1,T2X2,T2Y2,T2X3,T2Y3,T2X4,T2Y4 = input().split()
lista2 = [T2X1,T2Y1,T2X2,T2Y2,T2X3,T2Y3,T2X4,T2Y4] 
for i, item in enumerate(lista1):
    lista1[i] = int(lista1[i])
for j, items in enumerate(lista2):
    lista2[j] = int(lista2[i]) """

if(t1x[i]<=t2x[i] or t1y[i]<=t2y[i]):
    """ print('dentro') """
    i += 1
else:
    fuera+=1
    i += 1
#if((i+1)==2):
if(t1x[i]<=t2x[i] or t1y[i]>=t2y[i]):
    """ print('dentro') """
    i += 1
else:
    fuera+=1
    i += 1
#if((i+1)==3):
if(t1x[i]>=t2x[i] or t1y[i]>=t2y[i]):
    """ print('dentro') """
    i += 1
else:
    fuera+=1
    i += 1
#if((i+1)==4):
if(t1x[i]>=t2x[i] or t1y[i]<=t2y[i]):
    """ print('dentro') """
    i += 1
else:
    fuera+=1
    i += 1

if (fuera==0):
    print('HAN GANADO La tarjeta 1 esta contenida en la tarjeta 2')
else:
    print('HAN PERDIDO')

""" print('tx1',t1x)
print('tx2',t2x)
print('ty1',t1y)
print('ty2',t2y) """