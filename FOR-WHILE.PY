""" N = int(input())
n = ''
numeros = []
for i in range(N):
    n = input().split(' ')
    n[0] = int(n[0])
    n[1] = int(n[1])        
    n.sort()
    for j in range(n[0]+1,n[1]):
        n.append(j)
    numeros.append(sum(n))
    n = ''
for i in numeros:
    print(i) """

n = int(input())
lines = []
sums = []
for n in range(n):
    n1, n2 = input().split()
    pareja = [int(n1), int(n2)]
    pareja.sort()
    lines.append(pareja)

for n in range(len(lines)):
    sums.append(sum(range(lines[n][0], lines[n][1] + 1)))

for n in sums:
    print(n)