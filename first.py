action=input("что сделать?: ")

A = int(input("A:"))
B = int(input("B:"))

if action== "+":
    print(A + B)

elif action == "-":
    print(A - B)

elif action == "*":
    print(A * B)

elif action == ":":
    if B == 0: 
        print("На ноль делить нельзя!")
    else:
        res = A // B
    
        print("частное = " + str(res) )
        print("остаток = " + str (A % B))

else:
    print("Я не знаю такого действия.")