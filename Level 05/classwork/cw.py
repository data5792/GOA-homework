#1) შემოატანინეთ მომხხმარებელს სტრინგი და გამოიტანეთ მისი პირველი ასო
string1 = input("Enter a string: ")
if string1:
    print("The first character is:", string1[0])
else:
    print("The string is empty")

#2) შემოატანინეთ მომხმარებელს ორი სტრინგი და გამოიტანეთ მათ გაერთიანება
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("Combined string:", str1 + str2)

#3) შემოატანინეთ მომხმარებელს სტრინგი და თუ მომხმარებლის შემოტანილი სტრინგი არის 'yes', მაშინ შემოატანინეთ სახელი და გამოიტანეთ ის. ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ მომხმარებლლს მესიჯი 'goodbye' - თი
answer = input("Do you want to continue? (yes/no): ")
if answer.lower() == 'yes':
    name = input("Enter your name: ")
    print("Your name is:", name)

#ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ მომხმარებლლს მესიჯი 'goodbye' - თი
print("goodbye")

#4) შემოატანინეთ მომხმარებელს ასო თუ ეს ასო არის 'A' მაშინ გამოიტანეთ რიცხვი 100, თუ ის არის 'B' - 80, თუ 'C' - 60, თუ 'D' - 40, ხოლო თუ 'F' მაშინ სიტყვა 'Failed!'
grade = input("Enter a grade letter (A, B, C, D, F): ").upper()

if grade == 'A':
    print(100)
elif grade == 'B':
    print(80)
elif grade == 'C':
    print(60)
elif grade == 'D':
    print(40)
elif grade == 'F':
    print("Failed!")
else:
    print("Invalid letter entered.")
