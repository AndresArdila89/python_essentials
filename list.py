"""
    Lists
    Author:Andres Ardila 
    Textbook Guide: Head First Python
    Date: nov-23-2020 21:00h
"""

movies = ["The holy grail", "The Life of Brian", "The Meaning of Life"]

#BIF build-in-function
#list can be access by using the braket [] notation
#list are Pyhton collection objects

print(movies[1])
print("------------------------------")
print(movies)

print("--------------list methods----------------")

cast = ["Cleese",'Palin','Jones',"Idle"]
print(cast)

#Its ok to invoke a BIF on the results of another BIF
#list len() method 
print(len(cast))


#Using the append() method, it adds a single data item to the end of the list
#Methods are invoke using the "." dot notation.
cast.append("Gilliam")
print(cast)

#Now lets use the pop() method, it removes data from the end of the list
cast.pop()
print(cast)

#Thanks to the extend() method, its posible to add a collection of data items to the end of the list
cast.extend(["Gilliam","Chapman"])
print(cast)

#Next the remove() method 
cast.remove("Chapman")
print(cast)

#Finally lets try the inset() method it takes 2 parameters insert(index_position, "string")
cast.insert(0,"Chapman")
print(cast)