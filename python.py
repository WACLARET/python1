# import random

# health = 50
# difficulty = 1

# postion_health = random.randint(25,50) / difficulty

# health = health + postion_health

# #print(health)

# import math
# m = round(1.5)
# #print(m)

# w = math.floor(1.5)
# #print(w)

# r = math.sin(math.pi/2)
# #print(w)

# known_users = ["Tony", "Wafu", "Huru"]
# #print(len(known_users))

# #while True:
#     #print("Hi i am Tony")
#     #name = input("What is your name?:").strip().capitalize()
#       if name in known_users:
#            print("Hello {}!".format(name))
#            remove = input("would you like to be removed from the system?: (y/n)?:").strip().lower()
#         if remove == "y":
#             known_users.remove(name)
#         elif remove == "n":
#            # print("No problem")


#     else:
#        print("name not recognised {}".format(name))
#         add_me = input("would you like to be added to the system (y/n)?: ").strip().lower()
#         if add_me =="y":
#             known_users.append(name)
#         elif add_me == "n":
#            # print("No worrie see you around")

# / tuples
            # r = 1,2,3,"a","b"
            # print(r)
            # print(type(r))
#Dictionary
# students = {"tony":22, "wafu":20, "ema":19, "mata":45 }
# print(students["tony"])

#cinema simulator validates age and space remaining

# films = {
#     "arrow": [4,3],
#     "wetu": [9,5],
#     "man": [2,9], 
#     "hunter": [3,7],
#     "mafia": [6,9]
# }
# while True:
#     choice = input("film you like?: ").strip()
#     if choice in films:
#         age = int(input("how old are?: ").strip())
#         if age >= films[choice][0]:
#             if films[choice][1]>0:

#                  print("enjoy the film")
#                 films[choice][1] = films[choice][1] - 1
#             else:
#                 print("sorry we are out")
#         else:
#                 print("you are too young to watch the film.")
#     else:
#         print("the film does not exist")


 #while loops --------           
# number = 1
# while number <= 100:
#     if number % 2 != 0:
#      print(number)
#      number = number + 1

# from random import choice

# question = ["why are you dansing?", "where is my pen?: ", "why is tony crying?: "]
# question = choice(question)
# answer = input(question).strip().lower()
# while answer != "just":
#     answer = input("why?: ").strip().lower()
#     print("oh ok")


#for loop -----------

# for number in range(1,20):
#  print(number)
# vowels = 0
# consonants = 0
# for letter in "Hello":
#         if letter.lower() in "aeiou":
#                 vowels = vowels + 1
#         elif letter == "":
#             pass    
#         else:
#                 consonants = consonants + 1

#                 print("There are {} vowels".format(vowels))
#                 print("There are {} consonants".format(consonants))

# students = {
#     "male":["ttt", "yay", "www", "eeaee"],
#     "female":["aaa", "sss", "dad", "ff"]
# }
# for key in students.keys():
#     for name in students[key]:
#         if "a" in name:
#             print(name)


#list comprehension
# even_number = [x for x in range(1,50) if x % 2 == 0]
# print(even_number)

#language convertor to giberish prog asks quest and convert----------------
# original = input("please enter a sentense to be converted: ").strip().lower()
# words = original.split()
# new_words = []
# for word in words:
#     if word[0] in "aeiou":
#         new_word = word + "yay"
#         new_words.append(new_word)
#     else:
#         vowel_pos = 0
#         for letter in word:
#             if letter not in "aeiou":
#                 vowel_pos = vowel_pos + 1
#             else:
#                 break
# cons = word[:vowel_pos]
# the_rest = word[vowel_pos:]
# new_word = the_rest + cons + "ay"
# new_words.append(new_word)
# output = "".join(new_words)
# print(output)


#functions.....................

# def add(x,y):
#    return x + y
# a = add(5,10)
# print(a)

# def rev(text):
#   return text[::-1]
#   a = rev("pen")
#   print(a)
# word = "pen"
# print(word[::-1])

# a = 200
# def f():
#   b = a + 100
# print(b)

def about(name, age, likes):
  about("jack", 23, "python")
  sentence = "Meet {}! They are {} years old and like{}".format(name, age, likes)
  print(sentence)
  return sentence


 



