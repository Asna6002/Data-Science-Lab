def common_num(a, b):
    result=False
    for i in a:
        for j in b:
            if i == j:
                result=True
                return result
    return result


list1 = []
n=int(input('Enter number of elements'))
for i in range (1,n+1):
    ele=input('Enter element')
    list1.append(ele)

list2 = []
m=int(input('Enter number of elements'))
for i in range (1,m+1):
    ele1=input('Enter element')
    list2.append(ele1)
print(common_num(list1,list2))
