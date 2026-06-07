from random import *
from AzartClass import AzartClass
import pygame
def main():
	DifficultyFusion = []
	while True:
		taking = False
		c = True 
		mony = 100
		Azart = AzartClass()
		difficulty = input("Enter what difficult do you want: ")
		while True:
			print(f"var = {difficulty}, list = {DifficultyFusion}")
			mony_str = "$"+ str(mony)
			if difficulty == "cheats":
				print("WARNING: Add in DifficultyFusion cheats")
				DifficultyFusion.append(difficulty)
				print(f"DifficultyFusion = {DifficultyFusion}")
				
				_= difficulty
				difficulty = ""
				
				
				
			elif "cheats" in DifficultyFusion:
				print("not implemeted yet!")
				DifficultyFusion =[]
				break
			elif difficulty == "easi":
				secret_number  = randint(1, 3) 
				taking = True
			elif difficulty == "hard":
				secret_number = randint(1,10) 
				taking = True
			elif difficulty == "extrim":
				secret_number  = randint(1,50) 
				taking = True
			else:
				print("choose difficulty") 
				break
			if taking:
				print(f"balanse:{mony_str}") 
				number =input("enter yor nember:")
				if number.isdigit():
					if int(number)  == secret_number:
						mony += 10 
						print ("you win $10") 
					else:
						mony -= 5
						print("you lose mony $5")
				elif number == "e":
					exit()
				elif number  == "menu":
					break
				elif number == "test":
					print(Azart.main()) 
				else:
					print("it is not digit!") 

main()
