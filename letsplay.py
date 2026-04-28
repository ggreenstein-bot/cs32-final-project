
import random
import re
#will need for later when we have

story_files = [
    "stories/story1.txt",
    "stories/story2.txt",
    "stories/story3.txt",
]

def random_story():
    return random.choice(story_files)

def find_placeholders(text):
    return re.findall(r"{(.*?)}", text)
#find all placeholders in the story

#ask user for inputs to replace the {placeholder}
def grab_user_inputs(placeholders):
    answers = {} # create a place for the user inputs to live
    for word in placeholders: #for the word inside the placeholder
        user_input = input(f"Enter a {word}: ") #want it to tell the user what the placeholder word is
        answers[word] = user_input
    return answers

#fill in the story
def fill_story(template, answers):
    return template.format(**answers)

#load the stories
def load_story(filename):
    with open(filename, "r") as file:
        return file.read()

def intro():
    print('## Welcome to Fill-In-The-Blank! ##')
    #ask player if they are ready to play, if they are, print the rules
    while True:
        guess = input('Are you ready to play (yes/no): ').lower()
        if guess == "no":
            return False
        if guess == "yes":
            print("The rules are simple: \n answer the prompts, \n wait for the story, \n and prepare to laugh")
            print("This is a family friendly game. Please keep your answers appropriate")
            return True
def save_final_story(text):
    filename = input("what do you want to name your story?")
    path = f"finalstories/{filename}.txt"
    with open(path, "w") as f:
        f.write(text)
    print(f"\n Your story has been saved to {path}")

def main():
    if not intro():
        return
    #pick a random story
    story_filename = random_story()
    story_text = load_story(story_filename)

    placeholders = find_placeholders(story_text)
    answers = grab_user_inputs(placeholders)

    final_story = fill_story(story_text, answers)

    print("\n Your final story:\n")
    print(final_story)

if __name__ == '__main__':
    main()
