# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }

# print(f"You ordered a {pizza['crust']}-crust pizza.")

# for topping in pizza['toppings']:
#     print(topping)

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"{topping}")
    
    print(toppings)
    
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')