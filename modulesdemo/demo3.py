from searchandsort import search as s

print(s.is_present([100, 40, 68, 71, 32, 54, 89], 71))

n = int(input('ENTER NUMBER OF ELEMENTS FOR LIST'))
mylist = []
for i in range(n):
    mylist.append(int(input()))

key = int(input('ENTER SEARCH KEY FOR LIST - '))

print(s.is_present(mylist, key))
