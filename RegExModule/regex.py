import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)


#The findall() function returns a list containing all matches.
txt2 = "The rain in Spain"
x2 = re.findall("ai",txt2)
print(x2)

#The search() function searches the string for a match, and returns a Match object if there is a match.

txt3 = "The rain in spain"
x = re.search("\s", txt)

print("The first white-space character is located in position", x.start())


#The split() function returns a list where the string has been split at each match:

txt = "The rain in america"
x4 = re.split("\s", txt)
print(x4)

#You can control the number of occurrences by specifying the maxsplit parameter:

txt5 = "The rain in america2"
x5 = re.split("\s", txt5,1)
print(x5)


#The sub() function replaces the matches with the text of your choice:

txt6 = "The rain in Mexico"
x6 = re.sub("\s","8",txt6)
print(x6)

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

txt7 = "The rain in brezial"
x7 = re.search(r"\bS\w+", txt7)
print(x.span())

#string 

txt8 = "The rain in Spain"
x8 = re.search(r"\bS\w+", txt8)
print(x8.string)

#group

txt9 = "The rain in Spain"
x9 = re.search(r"\bS\w+", txt9)
print(x9.group())
