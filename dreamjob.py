name = " ".join(input("What is your name? \n").split()).title()
#print(name)
dream_company = " ".join(input("What is your dream company? \n").split())
if not dream_company.isupper():
    dream_company = dream_company.title()
#print(dream_company)
lang_profiency = " ".join(input("What programming language are you proficient in? \n").split()).title().strip()
#print(lang_profiency)
print(f"My name is {name}, I am a {lang_profiency} developer and would love to work for {dream_company}.")