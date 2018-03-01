# Dictionaries are Unordered and it cant be accessed using Index
# we need to use the key value Pair
# Key and Value are seperated By : and Dictionaries Start With {}
# keys in the Dictionaries are Unique , if it has duplicates the later one wil lbe replaced other and it will be used
#
fruit = {"orange": " A Sweet Orange Citrus Fruit",
        "apple": "Good For health",
        "lemon": "Vim Bar",
        "grape": "Fruit for Wine",
        "lime": "a Sour Green Citrus Fruit"
}
print(fruit["lime"])
print(fruit)
# append the value
fruit["peer"]= "An odd shaped Apple"
print(fruit)
# Same Key Will replace the Value with the New One
fruit["peer"]="Great Fruit"
print(fruit)

# to delete the dict
del fruit["lime"]
# To clear the contents
#fruit.clear()



