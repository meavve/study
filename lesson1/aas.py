a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print("Равносторонний")
elif a==b and a!=c:
    print("Равнобедренный")
elif a!=b and b!=c and a!=c:
    print("Разносторонний")