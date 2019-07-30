import random
#import prac as gui
#import tkinter
class hangman():
	key="ABC"
	score=0
	dict1={1:"CAT",2:"DOG",3:"KOALA",4:"TIGER",5:"PEACOCK",6:"RABBIT",7:"BLUE WHALE",8:"ANACONDA",9:"LION",10:"Python"}
	dict2={"CAT":"A lazy animal who hate dogs","DOG":"An animal termed as man's best friend","KOALA":"An animal that sleeps all the time","TIGER":"National animal","PEACOCK":"National Bird","RABBIT":"Bugs bunny","BLUE WHALE":"Largest mammal","ANACONDA":"Heaviest Snake","LION":"King of the jungle","Python":"A name of a reptile which is also a programming language"}
	def display(self):
		rand_no=random.randint(1,10)
		#rand_no=2
		hangman.key=hangman.dict1[rand_no]
		hint=hangman.dict2[hangman.key]
		return hint
	def read(self,character):
			counter=5
			newkey=hangman.key
                        #while(counter>0):
			#print("Enter the name of the animal")
			#name=input()
			iteration=0
			print("enter a word\n")
			while(iteration!=len(newkey)):
                                #'''and counter>0'''

				flag=0
				#flag_2=0
				#print(len(newkey))
				#print("enter a letter at a time\n")
				character=input()
				for letter in newkey:
					if character.lower()==letter.lower():
						iteration+=1
						flag=1
						newkey=newkey.replace(letter,"0",1)
						break
				if flag==0:
					counter-=1
					print("remaining lives"+str(counter))
				for letter in newkey:
					flag_2=0
					if letter=='0':
						flag_2=1
					flag_2=flag_2 and 1
				if flag_2==1:
					hangman.score+=1
			'''if name!=hangman.key:
				counter=counter-1
				print("WRONG ANSWER TYPE AGAIN :(\n")
				print("lives : "+ str(counter))
			else:
				hangman.score=hangman.score+1
				break
			'''
			if counter==0:
				print("game over")
				print("score = " +str(hangman.score))
			return counter
				
#ob1=hangman()
#ob2=gui.test_gui()
#while True:
#	ob1.display()
#	ob1.read()
	
#	print("Do u want to QUIT ?(y/n)\n")
#	ans=input()
#	if ans=='y'or ans=='Y':
#		break
#print(ob1.score)
