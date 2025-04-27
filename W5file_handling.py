
#Q1
# Your aim is to read in a text file, and calculate how many words are in it.
# You should:
#    - ask the user to enter the file name
#    - read the file in
#    - count how many words are in the file - there are multiple ways of doing this.


with open ("story.txt", "r") as file:
    data = file.read()
    words = data.split()   
    word_count = len(words)   
    print(word_count)

# get the file name
# open and read the file
# calculate the number of words
# hint: you could use .split() to break up by spaces
# display the wordcount

# Here are the word counts you should get:
# story.txt - 290

"""In a dense, magical forest lived a snail named Oliver and a badger named Luna. Oliver moved at a slow pace, always taking in the smallest details around him. Luna, on the other hand, was swift and curious, yet very patient with her little friend.
One sunny morning, the two decided to explore a new part of the woods. They wandered through sun-dappled paths, where Oliver marveled at the patterns the sunlight made on the forest floor, while Luna sniffed out new scents in the air. They stopped by a bubbling brook where Luna caught a glimpse of a fish, and Oliver admired the way the water sparkled like tiny diamonds.
As they continued, they encountered an ancient oak tree, its branches heavy with acorns. "Look, Oliver," Luna said, "this tree must be hundreds of years old. Imagine all the things it has seen." Oliver nodded slowly, his tiny antennae twitching in agreement. The ancient oak seemed to nod back, as if acknowledging their presence.
They walked further into a clearing, where wildflowers bloomed in a riot of colors. Oliver stopped to admire a particularly vibrant bluebell, while Luna chased after a butterfly, laughing as she did.
As the day turned to dusk, they made their way back home, the path now lit by the soft glow of fireflies. Oliver and Luna, side by side, reflected on their adventure. "Thank you for today, Luna," Oliver said in his quiet, measured voice. "I saw so many wonderful things."
"Anytime, Oliver," Luna replied. "There's always something magical in the world if we just take the time to look."
And so, they walked on, under the twinkling stars, grateful for the beauty of their friendship and the enchanting forest that was their home."""
