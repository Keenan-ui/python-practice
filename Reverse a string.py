def string_reverse(string):
    reverse_string=""
    for char in string:
        reverse_string=""+char+""+reverse_string+""
    print(reverse_string)

string=input("Enter a string: ")
string_reverse(string)