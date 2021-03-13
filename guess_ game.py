import random
winning_num=random.randint(1,100)
guess_count=0
while True:
	guess_num=int(input("enter a number between 1 to 100:  "))
	guess_count=(guess_count+1)
	if guess_num==winning_num:
		print(f"congratulations, well guess , your guess time {guess_count} guess number{winning_num}")
		break
	
	elif guess_num>winning_num:
		print ("too high")
	elif guess_num<winning_num:
		 print("too low")
		 
#except:
#	print ("enter a number"  )  			
		





