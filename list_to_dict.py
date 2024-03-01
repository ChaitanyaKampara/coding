# convert 2 lists into dictionary

def list_to_dict():
    keys = [1,2,3]
    values = ["one" , "two" , "three"]
    res=dict(zip(keys,values))
    print(res)

list_to_dict()