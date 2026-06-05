secret_number = 841
for i in range(5):
	guess = int(input("Guess the number: "))
	if guess > secret_number:
		print("Bro that's ahead of your Guess!")
	elif guess < secret_number:
		print("BRO...not even close!")
	else:
		print("You Win!")
