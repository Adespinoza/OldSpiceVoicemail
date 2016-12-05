# OldSpice Commerical Python Project

## Description:
Assignment for is to write a Python program that outputs an mp3 file voice mail message for the users' own phone number. There are two ways the program is supposed to run: (1.) Take command line arguments with flags (2.) Run with a menu style format, asking users for their input along the way. The program only takes in __one reason and one ending__ as input.

[Here's the Link to the OldSpice Ad](https://www.youtube.com/watch?v=-8JsvwUcok0)

## User Input:
When a user wants to input values, they have to choose from the following based on the gender that they identify with. Unfortunately they have to choose between either male or female, but with more time, I'm sure I can add another option for gender non-binary.

### Male Input

#### Reasons:

* [1]: Building an orphanage for children with their bare hands while playing a sweet, sweet lullaby for those children with two mallets against their abs xylophone.
* [2]: Cracking walnuts with their man mind.
* [3]: Polishing their monocle smile.
* [4]: Ripping out mass loads of weights.

#### Endings:
* [1]: I'm on a horse.
* [2]: I'm on a phone.
* [3]: SWAN DIVE.
* [4]: This voicemail is now diamonds.

### Female Input

#### Reasons:
* [1]: Ingesting my delicious Old Spice man smell.
* [2]: Listening to me read romantic poetry while I make a bouquet of paper flowers from each read page.
* [3]: Enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested aters.
* [4]: Being serenaded on the moon with the view of the earth while surviving off the oxygen in my lungs via a passionate kiss.
* [5]: Riding a horse backwards with me.

#### Endings:
* [1]: But she'll get back to you as soon as she can.
* [2]: Thanks for calling.

## Command Line Arguments:
Using the Command Line, users have to follow a certain format listed below:

`myproject.py -g m -n 012.345.6789 -r 2 -e 3 -o voicemail.mp3`

* -g (male/female) 
* -n (phone number) 
* -r (reasons) 
* -e (endings)
* -o (output name)

At the end, the program will prompt users if they'd like to add the OldSpice logo. Then it will ask if they would like to confirm and then output the information.

## Output 
In the end the program will output the name of the MP3 file that they want written out. It will also provide a text file for the user to look at if they so choose. Refrenced code from @itsbendunn and @maciesielka.
