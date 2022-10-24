var2 = max(['9', '7', '7', '7', '7'])
var1 = max(['8','3','4','5','5'])
var1Int = []
var2Int = []
print(var2)
print(var1)

for i in var1:
    var1Int.append(int(i))


if(int(var1) == int(var2)):
    print(0)
else:
    print(1)