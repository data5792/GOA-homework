#1) შემოატანინეთ მომხხმარებელს სტრინგი და გამოიტანეთ მისი პირველი ასო
string=input("enter a name: ")
print (string[0])
#2) შემოატანინეთ მომხმარებელს ორი სტრინგი და გამოიტანეთ მათ გაერთიანება
name=input("enter a name: ")
name2=input("enter a second name: ")
print (name + name2)
#3) შემოატანინეთ მომხმარებელს სტრინგი და თუ მომხმარებლის შემოტანილი სტრინგი არის 'yes', მაშინ შემოატანინეთ სახელი და გამოიტანეთ ის. ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ მომხმარებლლს მესიჯი 'goodbye' - თი
guess=input("enter a yes or no: ")
if guess=='yes':
    name=input("enter a name: ")
    print(name)
    print("goodbye")
#ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ მომხმარებლლს მესიჯი 'goodbye' - თი


#4) შემოატანინეთ მომხმარებელს ასო თუ ეს ასო არის 'A' მაშინ გამოიტანეთ რიცხვი 100, თუ ის არის 'B' - 80, თუ 'C' - 60, თუ 'D' - 40, ხოლო თუ 'F' მაშინ სიტყვა 'Failed!'
letter=input("enter a letter: ")
if letter=='A':
    print (100)
if letter=='B':
    print (80)
if letter=='C':
    print (60)
if letter=='D':
    print (40)
if letter=='F':
    print ('Falied!')
