string = input("Enter a string: ")
mylist, mylist2 = [], []
for i in string:
	mylist.append(i)
for j in range(len(string)-1, -1, -1):
	mylist2.append(string[j])
if mylist == mylist2:
	print("Palindrome!")
else:
	print("Not Palindrome!")
