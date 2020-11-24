"""
    Lists-Exercise 1
    Author:Andres Ardila 
    Textbook Guide: Head First Python
    Date: nov-23-2020 22:20h
"""
#Work out the Python code required to insert the numeric year
#data into the preceding list, changing the list so that it ends up looking 
#like this: ['The Holly Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]

movies = ['The Holly Grail', 'The Life of Brian', 'The Meaning of Life']

movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)

print(movies)


#Now write the Python code require to re-create the list with the data you need all in one go:
movies2 = ['The Holly Grail', 1975, 'The Life of Brian', 1979, 'The meaning of Life',1983]

