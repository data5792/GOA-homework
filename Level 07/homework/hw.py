# 1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე
# i=1
# while i<10:
#     print(i)
#     i+=1
# 2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე
# i=10
# while i>1:
#     print(i)
#     i-=1
# 3)კომენტარებით ახსენი while loop
#while loopი მუშაობს იქამდე სანამ პირობა არის ჭეშმარიტი
# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან
# password=input("Enter Password: ")
# mypassword="python123"
# while mypassword!=password:
#     input("enter password again: ")  
# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი
number=int(input("enter a number: "))
i=1
while i<number:
    print(i)
    i+=1