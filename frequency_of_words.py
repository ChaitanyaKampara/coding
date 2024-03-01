# count word frequency appearing in a string 

def frequency():
    str = input("Enter a string")
    lst = str.split()
    dict = {}

    for i in lst:
        if i not in dict.keys():
            dict[i]=0
        dict[i] = dict[i] +1
    print(dict)

frequency()  



# def frequency():
#     str = input("Enter a string")
#     lst = str.split()
#     dict = {}

#     for i in lst:
#         dict[i] = dict.get(i,0) +1
#     print(dict)

# frequency()  