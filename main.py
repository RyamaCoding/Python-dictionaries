# Dictionary {Key: Value}
# for e.g. {"bug" : "An error in a program that prevents the program from running as expected."}
# use a comma to add more values

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected", 
    "Function": "An error in a program that prevents the program from running as expected",
    }


# Adding a new key-value pair
programming_dictionary["Loop"] = "The action of doing the same thing over and over again"

empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Bug"] = "Bog"

for key in programming_dictionary:
    print(f"Key: {key}, Value: {programming_dictionary[key]}")