# Assignment 3: What's Your Chinese Food Personality?

print("What's Your Chinese Food Personality?")

# User inputs
name = input("What is your name? ")

spice = int(input("How much do you like spicy food? Enter a number from 1 to 5: "))

staple_food = input("Do you prefer rice or noodles? ")

flavor = input("Choose a flavor: light, sweet, savory, or spicy: ")

adventurous = input("Would you try a food you've never had before? yes or no: ")


# Change yes or no into a boolean
if adventurous == "yes":
    adventurous = True
else:
    adventurous = False


# Find the food personality
if spice >= 4:
    result = "Sichuan"

elif staple_food == "noodles":
    result = "Shaanxi"

elif flavor == "sweet":
    result = "Jiangsu"

else:
    result = "Guangdong"


# Print the result
print("Hi " + name + "!")
print("Your Chinese Food Personality is " + result + "!")

if adventurous == True:
    print("You are adventurous with food!")
else:
    print("You like to stay with food you know!")