import random
# list of books is stored in the list -'books'
books = ['Brave', 'Good night kiss', 'Tikki Tikki Tembo']

# An item from the list 'books' is selected
# by random.choice()
print(random.choice(books))
# Defining list of phrases which will help to build a story
Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
  
character = [' there lived a king.',' there was a man named Rishi.', ' there lived a fighter.']
  
time = [' One day', ' One full-moon night']
  
story_plot = [' he was passing by', ' he was going for a kindergarten ']
  
place = ['in the alps', ' to the ocean']
  
second_character = [' he saw a beautiful woman', ' he saw an young man']
  
age = [' who seemed to be in early 20s', ' who seemed very active and full of energy']
  
work = [' searching something.', ' digging a well on roadside.']
# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_character)+random.choice(age)+random.choice(work))

# Importing random module
import random

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_character)+random.choice(age)+random.choice(work))
