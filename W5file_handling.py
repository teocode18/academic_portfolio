
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




#Q2

'''Grade Analyser
In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file 
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be acheived by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.'''


filename = input("Enter the filename of the student file: ")

with open(filename, "r") as file:
  
    lines = file.readlines()


    output_filename = filename + "_out.csv"


with open(output_filename, "w") as output_file:
   
    for line in lines[1:]:  
       
        data = line.strip().split(",")

        student_id = data[0]

        try:
            grades = [int(grade) for grade in data[1:] if grade]
        except ValueError:
            print(f"Skipping line due to invalid grade data: {line}")
            continue

      
        if grades:
            average_grade = sum(grades) / len(grades)
            average_grade = round(average_grade, 2)  
        else:
            average_grade = 0  
        if average_grade >= 70:
            classification = "1"
        elif average_grade >= 60:
            classification = "2:1"
        elif average_grade >= 50:
            classification = "2:2"
        elif average_grade >= 40:
            classification = "3"
        else:
            classification = "F"

        output_file.write(f"{student_id},{average_grade:.2f},{classification}\n")
