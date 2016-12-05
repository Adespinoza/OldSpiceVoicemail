#Library Import Files
import getopt, sys
import os
import platform
import shutil
import urllib
from subprocess import call

#Array of text that the files output. Used to grab information.
phoneNumbers = ['0.mp3', '1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3', '6.mp3', '7.mp3', '8.mp3', '9.mp3']
maleMP3reasons = ['m-r1-building.mp3', 'm-r2-cracking_walnuts.mp3', 'm-r3-polishing_monocole.mp3', 'm-r4-ripping_weights.mp3']
maleMP3endings = ['m-e1-horse.mp3', 'm-e3-on_phone.mp3', 'm-e4-swan_dive.mp3', 'm-e5-voicemail.mp3', 'm-e2-jingle.mp3']

femaleMP3reasons = ['f-r1-ingesting_old_spice.mp3', 'f-r2-listening_to_reading.mp3', 'f-r3-lobster_dinner.mp3', 'f-r4-moon_kiss.mp3', 'f-r5-riding_a_horse.mp3']
femaleMP3endings = ['f-e1-she_will_get_back_to_you.mp3', 'f-e2-thanks_for_calling.mp3']

otherMP3 = ['m-b1-hello.mp3', 'm-b2-have_dialed.mp3', 'f-b1-hello_caller.mp3', 'f-b2-lady_at.mp3', 'm-r0-cannot_come_to_phone.mp3',
'f-r0.1-unable_to_take_call.mp3', 'f-r0.2-she_is_busy.mp3', 'm-leave_a_message.mp3', 'm-youre_welcome.mp3']

maleReasons = [
	    '[1]: Building an orphanage for children with their bare hands while playing a sweet, sweet lullaby for those children with two mallets against their abs xylophone.',
	    '[2]: Cracking walnuts with their man mind.',
	    '[3]: Polishing their monocle smile.',
	    '[4]: Ripping out mass loads of weights.'
    ]
femaleReasons = [
	    '[1]: Ingesting my delicious Old Spice man smell.',
	    '[2]: Listening to me read romantic poetry while I make a bouquet of paper flowers from each read page.',
	    '[3]: Enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested aters.',
	    '[4]: Being serenaded on the moon with the view of the earth while surviving off the oxygen in my lungs via a passionate kiss.',
	    '[5]: Riding a horse backwards with me.'
    ]
maleEndingLine = [
	    '[1]: I\'m on a horse.',
	    '[2]: I\'m on a phone.',
	    '[3]: SWAN DIVE.',
	    '[4]: This voicemail is now diamonds.'
    ]
femaleEndingLine= [
	    '[1]: But she\'ll get back to you as soon as she can.',
	    '[2]: Thanks for calling.'
    ]

#Does the user define as 'male' or 'female'
def defineGender():
	genderInput = str(raw_input("Do you want a cis-gendered Male or Female response (M/F)? ")).upper()
	invalidInput = True

	#Keep asking for valid
	while (invalidInput):
		if genderInput == "M":
			invalidInput =  False
		elif genderInput == "F":
			invalidInput = False
		else:
			print ""
			print "Error. The input your povided is incorrect"
			genderInput = str(raw_input("Do you want a cis-gendered Male or Female response (M/F)? ")).upper()

	return genderInput

#Grab the user's phone number
def slideIntoDMs():
	phoneNum = ""
	print ""
	phoneInput = str(raw_input("Can I have your phone number please: "))
	invalidInput = True

	#Keep asking for input
	while (invalidInput):
		
		for digit in phoneInput:
			if digit.isdigit():
				phoneNum += digit

		#Check to see if it is long enough
		if len(phoneNum) != 10:
			print ""
			print "INVALID INPUT. Phone number you entered isn't long enough"
			phoneInput = str(raw_input("Can I have your phone number please: "))
			phoneNum = ""
		else:
			invalidInput = False

	return phoneNum

#Prints the Male Reasons for not being at the phone
def printMaleReasons():
	for number in maleReasons:
			print number

#Prints the female reasons for not being at the phone
def printFemaleReasons():
	for number in femaleReasons:
			print number

#Prints dashes, helpful for presentation 
def printDashes():
	print "====================================================================="

#Prints the male endings 
def printMaleEndings():
	for reason in maleEndingLine:
		print reason 

#Prints the male endings 
def printFemaleEndings():
	for reason in femaleEndingLine:
		print reason

#Grabs the reasons that the user wants to input 
def getUserReasons():
	invalidInput = True 

	#Genders will get different responses 
	if genderVoice == "M":
		print ""
		print "REASONS TO NOT BE AT PHONE:"
		printDashes()
		printMaleReasons()
		printDashes()
		reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))

		#Check for invalid input 
		while invalidInput:
			if len(reasonInput) > 1:
				reasonInput = ""
				print ""
				print "You can only have ONE REASON to be away from the phone. Try again"
				printDashes()
				printMaleReasons()
				printDashes()
				reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))
			elif len(reasonInput) == 1 and reasonInput.isdigit():
				if  int(reasonInput) > 0 and int(reasonInput) <= 4:
					invalidInput = False
				else:
					print ""
					print "YOUR NUMBER WAS TOO BIG. Try again"
					printDashes()
					printMaleReasons()
					printDashes()
					reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))
			else:
				reasonInput = ""
				print ""
				print "Error. Try again"
				printDashes()
				printMaleReasons()
				printDashes()
				reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))

		return reasonInput

	elif genderVoice == "F":
		print ""
		print "REASONS TO NOT BE AT PHONE:"
		printDashes()
		printFemaleReasons()
		printDashes()
		reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))

		#Check for invalid input 
		while invalidInput:
			if len(reasonInput) > 1:
				reasonInput = ""
				print ""
				print "You can only have ONE REASON to be away from the phone. Try again"
				printDashes()
				printFemaleReasons()
				printDashes()
				reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))
			elif len(reasonInput) == 1 and reasonInput.isdigit():
				if  int(reasonInput) > 0 and int(reasonInput) <= 5:
					invalidInput = False
				else:
					print ""
					print "YOUR NUMBER WAS TOO BIG. Try again"
					printDashes()
					printFemaleReasons()
					printDashes()
					reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))
			else:
				reasonInput = ""
				print ""
				print "Error. Try again"
				printDashes()
				printFemaleReasons()
				printDashes()
				reasonInput = str(raw_input("Please enter a reason listed above for not at phone: "))

		return reasonInput

#Grab the endings fo rthe user
def sayingGoodbye():
	invalidInput = True

	if genderVoice == "M":
		print ""
		print "Endings To Choose From:"
		printDashes()
		printMaleEndings()
		printDashes()
		endingInput = str(raw_input("Enter an ending (only one): "))

		#Run while invalid input
		while invalidInput:
			if len(endingInput) > 1:
				endingInput = ""
				print ""
				print "You can only have ONE WAY to be end the voicemail. Try again"
				printDashes()
				printMaleEndings()
				printDashes()
				endingInput = str(raw_input("Enter an ending (only one): "))
			elif len(endingInput) == 1 and endingInput.isdigit():
				if  int(endingInput) > 0 and int(endingInput) <= 4:
					invalidInput = False
				else:
					print ""
					print "YOUR NUMBER WAS TOO BIG. Try again"
					printDashes()
					printMaleEndings()
					printDashes()
					endingInput = str(raw_input("Enter an ending (only one): "))
			else:
				endingInput = ""
				print ""
				print "Error. Try again"
				printDashes()
				printMaleEndings()
				printDashes()
				endingInput = str(raw_input("Enter an ending (only one): "))

		return endingInput
	elif genderVoice == "F":
		print ""
		print "Endings To Choose From:"
		printDashes()
		printFemaleEndings()
		printDashes()
		endingInput = str(raw_input("Enter an ending (only one): "))

		#Run while invalid input
		while invalidInput:
			if len(endingInput) > 1:
				endingInput = ""
				print ""
				print "You can only have ONE WAY to be end the voicemail. Try again"
				printDashes()
				printFemaleEndings()
				printDashes()
				endingInput = str(raw_input("Enter an ending (only one): "))
			elif len(endingInput) == 1 and endingInput.isdigit():
				if  int(endingInput) > 0 and int(endingInput) <= 2:
					invalidInput = False
				else:
					print ""
					print "YOUR NUMBER WAS TOO BIG. Try again"
					printDashes()
					printFemaleEndings()
					printDashes()
					endingInput = str(raw_input("Enter an ending (only one): "))
			else:
				endingInput = ""
				print ""
				print "Error. Try again"
				printDashes()
				printFemaleEndings()
				printDashes()
				endingInput = str(raw_input("Enter an ending (only one): "))
		return endingInput

#Prases toether the information needed to output the text file 
def writeFile(genderVoice, phoneNum, reason, ending, outputFile):

	outputParam = [] 
	textToPrint = ""

	#Answer the call
	if genderVoice == "M":
		outputParam.append(otherMP3[0])
		outputParam.append(otherMP3[1])	
		textToPrint += "Hello, you have dialed "
	elif genderVoice == "F":
		outputParam.append(otherMP3[2])
		outputParam.append(otherMP3[3])
		textToPrint += "Hello callers, the lovely/talented/intelligent and beautiful/sophisticated lady at "

	#Get phone number
	for num in phoneNum:
		outputParam.append(phoneNumbers[int(num)])
		textToPrint += num

	#Grab reasons for not being at the phone
	if genderVoice == "M":
		outputParam.append(otherMP3[4])
		textToPrint += ". The tall, accomplished man you're calling can't come to the phone right now because they're "

		if reason == "1":
			outputParam.append(maleMP3reasons[0])
			textToPrint += "Building an orphanage for children with their barehands while playing a sweet, sweet lullaby for those children with two mallets against their ab xylophone. "
		elif reason == "2":
			outputParam.append(maleMP3reasons[1])
			textToPrint += "Cracking walnuts with their man mind. "
		elif reason == "3":
			outputParam.append(maleMP3reasons[2])
			textToPrint += "Polishing their monocle smile. "
		elif reason == "4":
			outputParam.append(maleMP3reasons[3])
			textToPrint += "Ripping out mass loads of weights. "

		outputParam.append(otherMP3[7])
		textToPrint +=  "But leave a message and they'll return your call as soon as possible. "

		if ending == "1":
			outputParam.append(maleMP3endings[0])
			textToPrint += "I'm on a horse. "
		elif ending == "2":
			outputParam.append(maleMP3endings[1])
			textToPrint += "I'm on a phone. "
		elif ending == "3":
			outputParam.append(maleMP3endings[2])
			textToPrint += "SWAN DIVE. "
		elif ending == "4":
			outputParam.append(maleMP3endings[3])
			textToPrint += "This voicemail is now diamonds. "

	elif genderVoice == "F":
		outputParam.append(otherMP3[5])
		outputParam.append(otherMP3[6])
		textToPrint += " Is unable to take your call. She's busy "

		if reason == "1":
			outputParam.append(femaleMP3reasons[0])
			textToPrint += "ingesting my delicious Old Spice man smell, "
		elif reason == "2":
			outputParam.append(femaleMP3reasons[1])
			textToPrint += "listening to me read romantic poetry while I make a bouquet of paper flowers from each read page, "
		elif reason == "3":
			outputParam.append(femaleMP3reasons[2])
			textToPrint += "enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested waters, "
		elif reason == "4":
			outputParam.append(femaleMP3reasons[3])
			textToPrint += "being serenaded on the moon with the view of the earth while surviving off the oxygen in my lungs via a passionate kiss, "
		elif reason == "5":
			outputParam.append(femaleMP3reasons[4])
			textToPrint += "riding a horse backwards with me, "

		if ending == "1":
			outputParam.append(femaleMP3endings[0])
			textToPrint += "But she'll get back to you as soon as she can. "
		elif ending == "2":
			outputParam.append(femaleMP3endings[1])
			textToPrint += "Thanks for calling. "

	#Keep asking user if they want to add the jingle
	while True:
		jingleResponse = str(raw_input("Would you like to add the jingle (Y/N): ")).upper()
		if jingleResponse == "Y":
			outputParam.append(maleMP3endings[4])
			textToPrint += "Do do do doot doo do do dooot. "
			break
		elif jingleResponse == "N": 
			break

	print "Is this what you want us to output? "
	printDashes()
	print textToPrint
	printDashes()

	while True:
		confirmation = str(raw_input("Is the above correct (Y/N): ")).upper()
		if confirmation == "Y":
			if outputFile == "":
				outputFile = str(raw_input("Please enter a filename. Default will be 'untitled': "))
			outputMP3(outputParam, outputFile)
		elif confirmation == "N":
			print "RESTARTING..."
			
			#exit the program if there are command lines
			if len(sys.argv) == 11:
				exit(1)
			main()
		else:
			print "That isn't correct input and you know it. Try again."

#Outputs the mp3
def outputMP3(outputParam, filename):
	for files in outputParam:
		mp3 = urllib.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + files, files)

	mp3File = open(filename + ".mp3", "w")
	textFile = open(filename + ".txt", "w")

	for files in outputParam:
		shutil.copyfileobj(open(files, 'r'), mp3File)
		textFile.write(files + "\n")
	mp3File.close
	textFile.close

	for files in set(outputParam):
		os.remove(files)
	sys.exit()

# 	0			1 2  3     4         5  6  7  8  9  10
# myproject.py -g m -n 012.345.6789 -r 23 -e 13 -o voicemail.mp3

#Read input to see if there are 11 line arguments
def readInput(genderVoice, phoneNum, reason, ending, outputFile):
	if(len(sys.argv) != 11): 
		sys.stderr.write("ERROR. You did not provide the number of arguments. Please Try again." )
		print "\n"
		sys.stderr.flush()
		exit(2)
	else:
		#Assign Gender
		genderVoice = (sys.argv[2]).upper()

		#Vaidate Flag input 
		if sys.argv[1] != '-g' or sys.argv[3] != '-n' or sys.argv[5] != '-r' or sys.argv[7] != '-e' or sys.argv[9] != '-o':
			print "Error. You have provided do not do anything. Please try again. Please Check Below:"
			print "Correct Input: " + "-g"  + " " + "-n" + " " + "-r" + " " + "-e" + " " + "-o" 
			print "Your Input: " +sys.argv[1]  + " " + sys.argv[3] + " " + sys.argv[5] + " " + sys.argv[7] + " " + sys.argv[9] 
			exit(2)
		#Validate gender input
		if genderVoice != 'M' and genderVoice != 'F':
			print "Error. Select an appropriate gender for your voicemail. Die Cis-Scum."
			print sys.argv[2]
			exit(2)

		#Validate phone number
		for number in sys.argv[4]:
			if number.isdigit():
				phoneNum += number
		if len(phoneNum) != 10:
			print "Phone number you entered is too short/long enough. Try Again."
			print sys.argv[4]
			exit(2)

		#Validate reason
		if len(sys.argv[6]) > 1:
			print "You can only enter one reason, Try again."
			print sys.argv[6]
			exit(2)
		if not sys.argv[6].isdigit():
			print "Number you entered is not a digit"
			print sys.argv[6]
			exit(2)
		#Check reason for Male or Female
		if genderVoice == "M":
			if int(sys.argv[6]) < 0 or int(sys.argv[6]) > 4:
				print "Reason you entered is out of range for MEN. Try again"
				print sys.argv[6]
				exit(2)
		if genderVoice == "F":
			if int(sys.argv[6]) < 0 or int(sys.argv[6]) > 5:
				print "Reason you entered is out of range for FEMALES. Try again"
				print sys.argv[6]
				exit(2)

		#Assign value to reason
		reason = sys.argv[6]

		#Validate Ending
		if len(sys.argv[8]) > 1:
			print "You can only enter one ending, Try again."
			print sys.argv[8]
			exit(2)
		if not sys.argv[8].isdigit():
			print "Ending you entered is not a digit"
			print sys.argv[8]
			exit(2)
		if genderVoice == "M":
			if int(sys.argv[8]) < 0 or int(sys.argv[8]) > 4:
				print "Ending you entered is out of range for MEN. Try again"
				print sys.argv[6]
				exit(2)
		if genderVoice == "F":
			if int(sys.argv[8]) < 0 or int(sys.argv[8]) > 2:
				print "Ending you entered is out of range for FEMALES. Try again"
				print sys.argv[6]
				exit(2)

		#Assign value to ending 
		ending = sys.argv[8]

		for letters in sys.argv[10]:
			if letters != '.':
				outputFile += letters
			else:
				break 

		#Pass all the parsed information to output
		writeFile(genderVoice, phoneNum, reason, ending, outputFile)

#Main Function that does the work
def main():
	global genderVoice, phoneNumber, reason, ending, outputFile
	genderVoice = ""
	phoneNum = ""
	reason = ""
	ending = ""
	outputFile = ""

	#Need to check how many arguments are provided into the command line
	if len(sys.argv) > 1:
		#User Commandline Arguments
		readInput(genderVoice, phoneNum, reason, ending, outputFile)
	else:
		#Grab User inputs Normally
		genderVoice = defineGender()
		phoneNumber = slideIntoDMs()
		reason = getUserReasons()
		ending = sayingGoodbye()

		#Write the output File
		writeFile(genderVoice, phoneNumber, reason, ending, outputFile)

if __name__ == "__main__":
	main()


