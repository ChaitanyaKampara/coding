def common_letters():
    str1 = input("Enter 1st string: ")
    str2 = input("Enter 2nd string: ")
    s1=set(str1)
    s2=set(str2)
    # print(s1) 
    # print(s2)
    lst = s1 & s2
    print(lst)

common_letters()
