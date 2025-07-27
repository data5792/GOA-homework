# Level 23

# დავალება 1:
# შეიყვანე სიტყვა, სანამ მისი პირველი და ბოლო ასოები არ იქნებიან თანხმოვნები.
user_input = input("გთხოვთ შეიყვანეთ რაიმე სიტყვა რომელიც იწყება და მთავრდება თანხმოვანზე: ")

x = "აეიოუ"

while True:
    if user_input[0] in x or user_input[-1] in x:
        user_input - input("არასწორია,გთხოვთ შეიყვანეთ სიტყვა თავიდან: ")
    else:
        print(f"{user_input} სწორია გმადლობთ")
        break
# დავალება 2:
# შეიყვანე 5 სიტყვა, მაგრამ შეინახე (დაახსოვრე) მხოლოდ ისინი, რომლებიც სწორია.
 x="აეიოუ"
correct_word_list = []
for i in range(5):
    user_input= input("გთხოვთ შეიყვანოთ რაიმე სითყვა რომელშიც იწყება და მტავრდება თანხმოვანზე: ")
    print()
    if user_input[0] in x or user_input[-1] in x:
        print("არასწორია, სცადეთ თავიდან")
        print()

print(f"სწორი სიტყვების სია: {correct_word_list}")
# დავალება 3:
# რობოტმა უნდა დაითვალოს, რამდენჯერ სცადე სწორი სიტყვის შეყვანა.
user_input= input("გთხოვთ შეიყვანოთ რაიმე სითყვა რომელიც იწყება და მთავრდება თანხმოვნებით")
wrong_word_count = 0
x = "აეიოუ"

while True:
    if user_input[0] in x or user_input [-1] in x:
        user_input = input("არასწორია, გთხოვთ შეიყვანოთ სიტყვა თავიდან: ")
        wrong_word_count += 1
    else:
        print(f"{user_input}სწორია, გმადლობთ.")
        print(f"არასწორად შეყვანილი სიტყვების რაოდენობა: {wrong_word_count}")
        break
# დავალება 4:
# შეიყვანე 10 სიტყვა, მაგრამ დაბეჭდოს (გამოაჩინოს) მხოლოდ სწორი სიტყვები.
x = "აეიოუ"
for i in range(10):
    user_input x input("გთხოვთ შეიყვანოთ რაიმე სიტყვა რომელიც იწყება და მთავრდება თანხმოვანზე")
    if user_input[0] in x or user_input[-1] in x:
        print("თქვენს მიერ შეყვანილი სიტყვა არასწორია!")
    else:
        print(user_input)
        print("გმადლობთ, თქვენ შეიყვანედ სწორი სიტყვა!")

# დავალება 5:
# შეიყვანე სიტყვა და რობოტმა უნდა დათვალოს რამდენი ხმოვანია და რამდენი თანხმოვანი აქვს მას.
user_input=input("გთხოცთ შეიყვანოთ რაიმე სიტყვა რომელიც იწყება და მთავრდება თანხმოვანზე: ")
number_of_vowels = 0
number_of_consonants = 0
x = "აეიოუ"
while true:
    if user_input[0] in x or user_input[-1] in x:
        user_input = input("არასწორია =, გთხოვთ შეიყვანეთ სიტყვა თავიდან: ")
else:
    print(f"{user_input} სწორია, გმადლობთ")
    for i in user_input:
        if i in x:
            number_of_vowels
        else:
            number_of_consonants
    print()
    print(f"ხმოვანი ასოების რაოდენობა: {number_of_vowels}")
    print(f"თანხმოვანი ასოების რაოდენობა: {number_of_consonants}")
    print()
    break
