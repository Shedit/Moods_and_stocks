
# Use case for AI

- **Purpose:**
Inducing art in technology, mood and stock prices
	
- **Product:**
A visualization that updates in realtime showing some abstract represesntation of the stock market 	status of personal stocks.
	
- **Goals:**

  * Figure out how realtime stock API's work 
  * Figure out how to generate abstract graphich
  * Figure out how graphics work 
  * Figure our how to combine fluctuations in stocks with color representations 
	
---

## **1.	Figure out how realtime stock API's work**
	Free api key (pyrt.91@gmail.com):  
	Q2AJO6LYW66V9B0J

3 hours in, stuck at sorting out paths.... FML 


Finally sorted out som kind of measurement value to represent the change in color by taking a different between the current imported data, (current min)
	then taking the difference with the later min. Saving that difference, then adding the differences to represent the change in color. 

Now off to trying to see how to get this represented as a gui change. Tkinter time! 

## **2. Figure out how to generate abstract graphic** 

Alright, Tkinter is probaly the package for this type of work. What i want to do is tto try to print a color, 
and be able to change this colors properties with a number. 

    Found out the current version of Mojave (14.6 something) causes Tkinter to malfunction, 
	when running it it logs out from the computer and restarts some of the exists programs (not all, some closes for good).
	Basically causes an outmatic log out.  *To be continued ...* **(2019.09.01)**

**(2019.09.01)**
	Back again.. Hello there.. Tried first thing to establish a git for the Moods_and_Stocks folder. 
	TOTAL failure. Sais there are too many files. I guess it is a challange to run git in a virtual env?
	Seems to be that it takes a copy of all packages aswell. Leave that for now. Now it is time for trying to get some animations going.. 

Turtle and tKinter both cause same type of crash with mojave 14.6... 

Matplob lib works. Seems a bit farfetched though.. 

Not finding any solutions. Drifitng around wondering if it would be an idea to dive into learning how blender works.. Anyway.. thats it for today. 
Learned somewaht how plotly works a bit. *To be continued ...* 
