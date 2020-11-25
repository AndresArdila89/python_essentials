

fav_movies = [
    "The Holy Grail",1975, "Terry jones & Terry Gilliam",91 ,
        ['Graham Chapman',
            ['Michel Palin', 'John Cleese', 'Terry Gilliam','Eric Idle','Terry Jones']]]


for each_item in fav_movies:
    if isinstance(each_item, list):
        for each_subitem in each_item:
            if isinstance(each_subitem, list):
                for each_subitem_item in each_subitem:
                    print(each_subitem_item)
            else:
                print(each_subitem)
    else:
        print(each_item)

