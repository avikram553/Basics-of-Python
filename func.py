def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]: #str[left_pos]!=str[right_pos]
			return False
		left_pos += 1
		right_pos -= 1
	return True
a=input("Enter the string = ")
print(isPalindrome(a))

