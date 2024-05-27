# Importing random module
import random


#Sentence_starter – This list gives an idea about the time of the event.
#character – This list tells about the main character of this story.
#time – This list defines the exact day on which some incident has occurred.
#story_plot – This list defines the plot of the story.
#place – This list defines the place at which the incident occurred.
#second_character – This list defines the second character of the story.
#age – This list defines the age of the second character.
#work – This list tells about the work the second character was doing.



# Defining list of phrases which will help to build a story

Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Jack.',
			' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to ']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.']



# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))