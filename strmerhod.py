a = "harekrishna"
print(a.upper())  #converts in uppercase

print(a.lower()) #convets in lowercase

a1 = "harerame@@@"
print(a1.rstrip("@"))   #removes any trailing characters in a string

a2 = "hare rama"
print(a2.replace("rama", "krishna"))   #replace all occurences in string

a3 = "aana anu anubhuti"
print(a3.split(" "))    #that method make a list 
a4 = "anu@aana@aubhuti"
print(a4.split("@"))

a5 = "introdution to recyclebin"
print(a5.capitalize())   #fisrt character converts in uppercase and rest of character in lowercase

a6 = "Welcome to the jungle"
print(a6.center(40))      #they give spaces in starting in the string 
print(a6.center(60, ">"))    

a7 = "anubhuti"
print(a7.count("u"))
a8 = "anu anubhuti"
print(a8.count("anu"))   #they count characters and words in whole string

a9 = "anu@@"
print(a9.endswith("@"))
print(a9.endswith("@", 2, 4))     #we can also do string slicing

a10 = "her name is maddy, she is good girl"
print(a10.find("is"))  #they find first occunrence in thi string and give a index value, If they didnt find value they give -1

a11 = "Whenigotoparkat10am"
print(a11.isalnum())

a12 = "WhenIgotoaaparkat"
print(a12.isalpha())

a13 = "anubhutisharma"
print(a13.islower())

a14 = "she is fine and she is good"
print(a14.isprintable())        #not allowed any special characters and any white spaces and any espace sequnce 

a15 = "    "
print(a15.isspace())
a16 = "         "
print(a16.isspace())        #using tab 

a17 = "Anubhuti Sharma"
print(a17.istitle())

a18 = "AANA"
print(a18.isupper())

a19 = 'she is good girl'
print(a19.startswith("she"))

a20 = "aNuBhutI"
print(a20.swapcase())     #they converts lowercase to uppercase and uppercase to lowercase

a21 = "she is so kind girl"
print(a21.title())

#practice questions

name = input("Enter a name ")
print("Good afternood", name)

nm = input("Enter the candidnate name:-")
date = input("Enter a date :-")
print("Dear", nm, "\nYou're seleted!", date)

ss = "this is a bird"
print(ss.replace(" ", "  "))

