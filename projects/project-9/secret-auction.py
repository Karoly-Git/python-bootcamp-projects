programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

programming_dictionary["Loop"] = "Loooooop"
programming_dictionary["Bug"] = "Buuug"

print(programming_dictionary)

for key in programming_dictionary:
    print({key, programming_dictionary[key]})