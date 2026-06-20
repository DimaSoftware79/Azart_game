from random import *
from AzartClass import AzartClass

def CleanScreen():
        char = "\033[2J\033[H"  
        return char


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
                                # print(CleanScreen()) 
                                print(f"balanse:{mony_str}") 
                                number =input("enter yor nember:")
                                if number.isdigit():
                                        if int(number)  == secret_number:
                                                print(CleanScreen())
                                                mony += 10 
                                                print ("you win $10")
                                        else:
                                                print(CleanScreen())
                                                mony -= 5
                                                print("you lose mony $5")
                                elif number == "e":
                                        exit()
                                elif number  == "menu":
                                        break
                                elif number == "test":
                                        print(CleanScreen())
                                        result = Azart.main(mony)
                                        # print (f"DEBUG: now success is {result[1]} need be True, now nwe_mony is {result[0]}: ")

                                        if result[1]:
                                                print ("you need to repay your bank loan!")
                                                mony = result[0]
                                                
                                        print(mony)
                                else:
                                        print("it is not digit!") 

main()
