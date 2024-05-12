def missing_number(str):
    n = str[::-1]
    a = 0
    a = sum(str)
    k = (n*(n+1))//2
    print(k-a)
    print(n)
 
   # lst = str.split()
   # n = lst.length()
   # k = ((n+1)(n+2))/2
str = [1, 2, 3, 5, 6, 7]
missing_number(str)
