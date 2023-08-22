# name = input("Please enter your name:\n")
# print(f"Hello, {name.title()}!")

# prompt = "Hello."
# prompt += "What's your name?\n"
# name = input(prompt)
# print(f"{name.title()}")

# def greet_user(username):
#     print(f"Hello, {username.title()}!")
    
# greet_user('jesse')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(first_name = f_name, last_name = l_name)
    print(f"\nHello, {formatted_name}!")