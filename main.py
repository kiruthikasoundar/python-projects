#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# r_letter = ''
# r_symbol = ''
# r_number = ''
# for letter in range(0, nr_letters):
#   r_letter += str(random.choice(letters))
# for symbol in range(0, nr_symbols):
#   r_symbol += str(random.choice(symbols))
# for number in range(0, nr_numbers):
#   r_number += str(random.choice(numbers))
# print(r_letter + r_symbol + r_number) 
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
r_letter = []
r_symbol = []
r_number = []
random_list = []
for letter in range(0, nr_letters):
  r_letter.append(str(random.choice(letters)))
random_list.extend(r_letter)
for symbol in range(0, nr_symbols):
  r_symbol.append(str(random.choice(symbols)))
random_list.extend(r_symbol)
for number in range(0, nr_numbers):
  r_number.append(str(random.choice(numbers)))
random_list.extend(r_number)
random.shuffle(random_list)
concat = ''
for i in range(0,len(random_list)):
  concat += random_list[i]
print(concat) 