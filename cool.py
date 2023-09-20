import time

sandwich_prices = {"chicken":5.25, "beef":6.25, "tofu":5.75}
drink_prices = {"small":1.00, "medium":1.75, "large":2.25, 0:0}
fri_prices = {"small":1.00, "medium":1.50, "large":2.00, 0:0}
fri_size = 0
beverage_size = 0
f = ""
s = ""
b = ""

sandwich_size = input("Hello, what sandwich would you like? (chicken, beef, tofu): ")
time.sleep(.5)
print("\n" + f"Ok, 1 {sandwich_size} sandwich. \n")
s = f"1 {sandwich_size} sandwich,"
time.sleep(.5)

    

byn = input("Would you like a beverage?: ")
if byn == "yes":
    beverage_size = input("\nWhat size would you like? (Small, Medium, Large): ")
    print("\n" + f"Ok, 1 {beverage_size} drink. ")
    b = f"1 {beverage_size} drink,"
    
fby = input("\nWould you like french fries? ")
    
if fby == "yes":
    fri_size = input("\nWhat size would you like? (Small, Medium, Large): ")
    print("\n" + f"Ok, 1 {fri_size} fry. ")
    f = f"1 {fri_size} fry,"
    
print("\nHow many ketchup packets would you like?: ")
ketchup = int(input())


time.sleep(.5)


total = sandwich_prices[sandwich_size] + drink_prices[beverage_size] + fri_prices[fri_size] + ketchup * .25
print(f"Your order is {s}{b}{f} your total is {total}")
#print(f"\nYour total is ${total}")
time.sleep(.5)
print("\nThank you for your order.")