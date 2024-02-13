def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer"
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer"
    elif lang == "Java":
        return "You can become a mobile app developer"


print(switch("JavaScript"))
print(switch("PHP"))
print(switch("Java"))


#Implement Switch Statements

lang = input("What's the programming language you want to learn?")

match lang:
             case "JavaScript":
                 print("You can become a web developer.")
             case "PHP":
                 print("You can become a backend developer")
             case "Python":
                 print("You can become a Data Scientist")
             case "Solidity":
                 print("You can become a Blockchain developer")
             case "Java":
                 print("You can become a mobile app developer")
             case _:
                 print("You can become a mobile app developer")


lang("PHP")
             





    
