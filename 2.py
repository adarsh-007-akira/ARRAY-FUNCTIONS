elems=int(input("Number Of Elements In Array : \n"))
lst = []
for i in range(elems):
    lst.append(int(input(f"What is the {i+1} element :\n")))
print(f"The Greatest Integer Im the Array is {max(lst)}")