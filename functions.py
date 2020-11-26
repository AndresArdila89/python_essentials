"""
    Creating Functions and recursion
    Author:Andres Ardila 
    Textbook Guide: Head First Python
    Date: nov-25-2020 16:00h
"""


# A function in Python is a named suite of code, which can also take an OPTIONAL list of arguments if required.
# def function_name (argument(s)):


fav_movies = [
    "The Holy Grail",1975, "Terry jones & Terry Gilliam",91 ,
        ['Graham Chapman',
            ['Michel Palin', 'John Cleese', 'Terry Gilliam','Eric Idle','Terry Jones']]]


def print_lol(the_list):

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)


print_lol(fav_movies)