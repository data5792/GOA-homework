#1)შემოატანინეთ მომხმარებელს რიცხვი  და თუ 10 ზე მეტი იქნება  გამოიტანინოს ("you are right ")
num = int(input("Enter a number: "))
if num > 10:
    print("You are right")
#2)მომხმარებელს შემოატანინეთ ორი რიცხვი გააკეთეთ მათზე მათემატიკური ოპერაციები  ("+, -, *, /, %, <, >, <=, >=, ==, !=. **)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
    print("Modulo:", a % b)
else:
    print("Cannot divide by zero")

print("Power:", a ** b)
print("a < b:", a < b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)
print("a == b:", a == b)
print("a != b:", a != b)
#3)ახსენით დღეს ნასწავლი If კომენტარებით 

# if არის პირობითი ბრძანება, რომელიც ამოწმებს, მართალია თუ არა გარკვეული პირობა.
x = 5

# ეს კოდი შეამოწმებს, არის თუ არა x ტოლი 5-ს
if x == 5:
    print("x ტოლია 5-ს")  # დაიბეჭდება ეს

# შეგვიძლია გამოვიყენოთ if-else, თუ გვინდა ორი შესაძლო შემთხვევა
if x > 10:
    print("x მეტია 10-ზე")
else:
    print("x ნაკლებია ან ტოლია 10-ს")  # დაიბეჭდება ეს

# ასევე შეგვიძლია გამოვიყენოთ elif — ეს ნიშნავს "else if" ანუ დამატებითი შემოწმება
if x < 3:
    print("x ნაკლებია 3-ზე")
elif x == 5:
    print("x ზუსტად 5-ს ტოლია")  # დაიბეჭდება ეს
else:
    print("x სხვა მნიშვნელობა აქვს")
