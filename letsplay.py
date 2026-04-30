
import random
import re
#will need for later when we have

#list all of the story files that the random_story function can pick from
story_files = [
    "stories/story1.txt",
    "stories/story2.txt",
    "stories/story3.txt",
    "stories/story4.txt",
    "stories/story5.txt",
    "stories/story6.txt",
    "stories/story7.txt",
]
#pick a random story from the list above
def random_story():
    return random.choice(story_files)

#find all placeholders in the story as market by {} and get anything inside of those brackets
def find_placeholders(text):
    return re.findall(r"{(.*?)}", text)

#ask user for inputs to replace the {placeholder}
def grab_user_inputs(placeholders):
    answers = {} # create a place for the user inputs to live
    for word in placeholders: #for the word inside the placeholder
        user_input = input(f"Enter a {word}: ") #want it to tell the user what the placeholder word is
        answers[word] = user_input
    return answers #save the input to answers and return answers

#fill in the story using the template (story file) and answers (user input)
def fill_story(template, answers):
    return template.format(**answers)

#read the story
def load_story(filename):
    with open(filename, "r") as file: #open the file in read mode (which automatically closes when done)
        return file.read() #return the read story
    
#ask the player what they want to name their final story and save it
def save_final_story(text):
    filename = input("what do you want to name your story?") #ask user for input
    path = f"finalstories/{filename}.txt" #how to find/where the story will be saved
    with open(path, "w") as f: #create a file
        f.write(text) #write the text of the final story into the file
    print(f"\n Your story has been saved to {path}") #print the path so the user knows where it is


#ask the player if they are ready to play and give them the rules
def intro():
    print('## Welcome to Fill-In-The-Blank! ##')
    #ask player if they are ready to play, if they are, print the rules
    while True:
        guess = input('Are you ready to play (yes/no): ').lower()
        if guess == "no": #if the player does not want to play break
            return False
        if guess == "yes": #if they want to play, print the rules
            print("The rules are simple: \n answer the prompts, \n wait for the story, \n and prepare to laugh")
            print("This is a family friendly game. Please keep your answers appropriate")
            return True

def main():
    #make sure that the input is not part of the intro input
    if not intro():
        return
    #pick a random story
    story_filename = random_story()
    #read the story it picked
    story_text = load_story(story_filename)
#find placeholders in the text
    placeholders = find_placeholders(story_text)
#get user inputs to the placeholders
    answers = grab_user_inputs(placeholders)
# fill the story using the story text and user inputs
    final_story = fill_story(story_text, answers)

    print("\n Your final story:\n")
    print(final_story)

#call the function to save final story to folder
    save_final_story(final_story)

if __name__ == '__main__':
    main()
