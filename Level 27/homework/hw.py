# 1) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# print()

# def slicing_list(list):
#     return list [1:-1]

# print(slicing_list(numbers))
# 2) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ
# numbers = [10, 20, 30, 40, 50]
# numbers1 = [100, 200, 300, 400, 500]
# def two_list_sum(num1,num2):
#     sum1 = 0
#     for numbers in num1:
#         sum1 += numbers
     
#     sum2 = 0
#     for numbers1 in num2:
#         sum2+= numbers1
        
#     return sum1 * sum2
# print(two_list_sum(numbers, numbers1 ))
# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
# numbers = [5, 6, 10, 4, 3, 8, 10]
# print(numbers)

# def doubled_numbers(num_list):
#     new_list = []
#     number = 0
#     while number < len(num_list):
#         doubled_numbers = num_list[number] * 2
#         new_list.append(doubled_numbers)
#         number += 1
#     return new_list

# print(doubled_numbers(numbers))
# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 100, 200, 300]
# print (num_list)

# def even_numbers(num_list):
#     even_numbers = []
#     for even in num_list:
#         if even % 2 == 0:
#             even_numbers.append(even)
#     return even_numbers

# print(even_numbers(num_list))
# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია
# names = ["data", "giorgi", "bacho" "gela", "nana", "goga"]
# print(names)

# def name_list(names):
#     new_names = []
#     for name in names:
#         if name[0] == "n" or name[0] == "N":
#             new_names.append(name)
#     return new_names

# print (name_list(names))