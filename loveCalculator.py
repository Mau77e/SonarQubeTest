# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

count_T = lower_case_name1.count("t")
count_R = lower_case_name1.count("r")
count_U = lower_case_name1.count("u")
count_E = lower_case_name1.count("e")
count_L = lower_case_name1.count("l")
count_O = lower_case_name1.count("o")
count_V = lower_case_name1.count("v")

true_counter = sum([count_T, count_R, count_U, count_E])
love_counter = sum([count_L, count_O, count_V, count_E])

love_calc = int((f"{true_counter}{love_counter}"))


if (love_calc < 10) or (love_calc > 90):
    print(f"Your score is {love_calc}%, you are like coke and mentos together.")
elif (love_calc >= 40) and (love_calc <= 50):
    print(f"Your score is {love_calc}%, you should give it a try.")
else:
    print(f"Your score is {love_calc}%")






#      ░█████╗░███╗░░██╗░██████╗░███████╗██╗░░░░░░█████╗░██╗░██████╗       ░█████╗░░█████╗░██████╗░███████╗
#      ██╔══██╗████╗░██║██╔════╝░██╔════╝██║░░░░░██╔══██╗╚█║██╔════╝       ██╔══██╗██╔══██╗██╔══██╗██╔════╝
#      ███████║██╔██╗██║██║░░██╗░█████╗░░██║░░░░░███████║░╚╝╚█████╗░       ██║░░╚═╝██║░░██║██║░░██║█████╗░░
#      ██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██║░░░░░██╔══██║░░░░╚═══██╗       ██║░░██╗██║░░██║██║░░██║██╔══╝░░
#      ██║░░██║██║░╚███║╚██████╔╝███████╗███████╗██║░░██║░░░██████╔╝       ╚█████╔╝╚█████╔╝██████╔╝███████╗
#      ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═════╝░       ░╚════╝░░╚════╝░╚═════╝░╚══════╝


# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")














#
# #Write your code above this line 👆
# # 🚨 Do NOT modify the code below this line 👇
#
#
# with open('testing_copy.py', 'w') as file:
#   file.write('def test_func():\n')
#   with open('main.py', 'r') as original:
#     f2 = original.readlines()[0:45]
#     for x in f2:
#       file.write("    " + x)
#
#
# import testing_copy
# import unittest
# from unittest.mock import patch
# from io import StringIO
# import os
#
# class MyTest(unittest.TestCase):
#   def run_test(self, given_answer, expected_print):
#     with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
#       testing_copy.test_func()
#       self.assertEqual(fake_out.getvalue(), expected_print)
#
#   def test_1(self):
#     self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')
#
#   def test_2(self):
#     self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')
#
#   def test_3(self):
#     self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')
#
#   def test_4(self):
#     self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')
#
#
# print('\n\n\n.\n.\n.')
# print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
# print('Your score is 43, you are alright together.\n')
# print('\nRunning some tests on your code with different name combinations:')
# print('.\n.\n.')
# unittest.main(verbosity=1, exit=False)
#
# os.remove('testing_copy.py')












