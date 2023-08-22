# languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }

# language = languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in languages.keys():
#     print(name.title())

# for name in languages:
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in languages.keys():
#     print(f"Hi {name.title()}.")
    
#     if name in friends:
#         language = languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
        
# if 'erin' not in languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in languages.values():
#     print(language.title())

# print(languages.keys())
# print(languages.values())

# print("The following languages have been mentioned:")
# for language in set(languages.values()):
#     print(language.title())

languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, language in languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for lang in language:
        print(lang.title())