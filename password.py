# This is password trying program
# Use only has three chance to guess the password

password = 'a123456'
i = 0
chance = 3 # how many chances to try the password
while i <= 2:
	password_guess = input('please insert the password: ')
	if password_guess == password:
		print('access success')
		break # escape while loop
	else:
	    chance = chance - 1
	if chance == 0:
		break # only has 3 chances, stop the program
	else:
		print('password error, you still have', chance, 'chance')
	i = i + 1	