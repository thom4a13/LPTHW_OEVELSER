the_count = [1, 2, 3, 4, 5]
fruits =['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for i in fruits:
    print(f"A fruit of type: {i}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# use a list comprehension to create a list with elements from 0 to 5
elements = [i for i in range(0, 6)]

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

