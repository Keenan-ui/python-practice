def string_reverse(string):
    reverse_string="" #Holds the reversed string
    for char in string:
        reverse_string=""+char+""+reverse_string+"" #prefixes reverse_string with the character
    print(reverse_string)

string=input("Enter a string: ")
string_reverse(string)
