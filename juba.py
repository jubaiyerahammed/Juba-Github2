"""
name=input("Enter your name:")
age=int(input("Enter your age:"))
print('Hello',name,'ypu will be',age+1,'next year.')

number=int(input("Enter your number:"))
if number%2==0:
    print("Even")
else:
    print("Odd")


password=input("Enter your password:")
if password=="python123":
    print("Access granted")
else:
    print("Access denied")


number=int(input("Enter your number:"))
while number>=0:
    print(number)
    number-=1


total = 0
while True:
    n=int(input("Enter your number:"))
    total+=n
    if n==0:
        break
print(total)

sum=0
while True:
    n=int(input("Enter your number:"))
    sum+=n
    if n>=0:
        break
print(sum)

secret=7
while True:
    guesses=int(input("Enter your guesses:"))
    if guesses==secret:
        print("Correct")
    else:
        print("Incorrect")

num=int(input("Enter your number:"))
if num>=1:
    print("The number is positive",num)
elif num==0:
    print("The number is zero")
else:
    print("The number is negative")


a='1.Say Hello'
b='2.Show favorite number'
c='3.Exit.'
print(a)
print(b)
print(c)
while True:

    choice=int(input("Enter your choice:"))
    if choice==1:
        print('Hello')
    elif choice==2:
        print('My favorite number 7 ')
    elif choice==3:
        print('Goodbye!')
        break


largest= None
while True:
    n=int(input("Enter your number:"))
    if n==-1:
        break
    if largest is None or n>largest:
        largest=n
print('largest number',largest)



username = "admin"
password = "python123"

attempts = 3

while attempts > 0:
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Welcome!")
        break
    else:
        print("Invalid login")
        attempts -= 1

if attempts == 0:
    print("Account locked")




num = int(input("Enter number: "))
i = 1

while i <= 5:
    print(num, "x", i, "=", num * i)
    i += 1

num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits:", count)

temp = int(input("Enter temperature: "))

if temp >= 30:
    print("Hot")
elif temp >= 15:
    print("Warm")
else:
    print("Cold")


while True:
    ans = input("Continue? (yes/no): ")
    if ans == "yes":
        print("Starting...")
        break


num = int(input("Enter number: "))

while num > 0:
    print(num)
    num -= 2

print(num)


total = 0
count = 0

while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num
    count += 1

print("Average:", total / count)


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "3":
        print("Goodbye!")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)


stored = "student"

user = input("Enter username: ")

if user == stored:
    print("Taken")
else:
    print("Available")


count = 0

while True:
    num = int(input("Enter number: "))
    if num == -1:
        break

    if num > 0:
        count += 1

print("Positive count:", count)
"""
