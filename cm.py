prices = {"chicken":9.60, "beef":5.45, "tofu":3.99, "small_fri":1.00, "medium_fri":1.75, "large_fri":2.50, "small_drink":1.00, "medium_drink":2.00, "large_drink":3.20}
# sandwich = {1:lambda: input("What sandwich would you like?: "), "chicken":lambda:print("You "), "beef":lambda a:prices[a], "tofu":lambda a:prices[a]}
print("Hello there! ")
sandwich = (prices[(input("What sandwich would you like?: "))])

fri= {"yes":{"small":lambda:print(prices["small_fri"]), "medium":lambda:prices["medium_fri"], "large":lambda:prices["large_fri"]}, "no":{"":lambda:print(0)}}
drink= {"yes":{"small":lambda:print(prices["small_drink"]), "medium":lambda:prices["medium_drink"], "large":lambda:prices["large_drink"]}, "no":{"":lambda:print(0)}}
fri[input("Would you like french frys?: ")][input("What size would you like?: ")]()
drink[input("Would you like a drink?: ")][input("What size would you like?: ")]()
print(f"Your total is {int(input('How many kectup packets do you want?: ')) + drink + fri + sandwich}, Thank you.")

print("hi")


