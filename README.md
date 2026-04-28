# cs32-final-project
# cs32-final-project
Project Overview: Do you have special memories from growing up of filling out Mad Libs with your friends and hysterically laughing about the outcome? Me too! Well now that we are living in the digital age, what do you say we keep those memories alive but move it to the computer. For this project we will be creating your own stories using a similar fill in the blank model! The computer will ask you for an input whether that be a verb or food and then it will select from a folder filled with fill-in-the-blank stories... and be prepared to laugh with your friends. But in order to accomplish this goal, we need to move in steps

GAI USE: Harvard AI Sandbox has been vital to bringing this project together. I have used it to help me with the syntax on every single section. I wrote what my objective was into GAI and it provided me with the syntax. I did not just copy and past it. I made sure I understood the code. If it provided me with a method I did not know or we did not learn in class, I would attempt to do it as we had in class, however I often needed support debugging and would eventually need to greatly change the syntax. I also used it for help debugging

STEP 1:
Lets build out a folder with many different stories. This way, people can play more than once and stay on the edge of their seat.

STEP 2:
Import random functions
We will need the computer to select a random story to put the users inputs into
also import os and re

STEP 3:
define random story function. We will need the computer to pick a random story from the story folder

STEP 4:
Once we have a story folder we want to look for anything in the {} this means that the word is a placeholder for the input that the user provides. We want the computer to find all of these inputs

STEP 5:
Once we find all of the placeholders that will be replaced by the user inputs, we need to create a new function. This function will ask the user for an input and then save that input in a dictionary (with key and values). As such, we will need to create a dictionary for this function.
    The output of this section should look something like this: "pick a verb: "
    then it should save the input provided by the user

STEP 6:
Once we have identified the placeholders and collected the inputs, we will want to replace the placeholders with those inputs. The first step to do this would be to read the file

STEP 7:
Then we want to introduce the reader to the game, make sure they are ready to play, and tell them the rules.

Step 8:
We made it to the main funciton! First we need to make sure that the input that the user is putting in is not intended as an answer to the intro function.
- Then we need pick a random story using our random story function
- next we need to input the file name into the load_story function that will read it read the story (we need to read the story to look for placeholders)
- next we will want to find the placeholders in the text that we just read
- once we find the placeholders we want to  collect user inputs
- once we have our inputs and our placeholders, it is time to switch them out using the fill_story function
- once we have our new story we want to print that to the user! 
