# Step 2: Import data list and question model

from question_model import Question
from data import question_data

# Step 5: Import QuizBrain
from quiz_brain import QuizBrain

# Step 3: Create question bank using the question_data that has been imported (hint: loops)

# 3a. Place to store our question in the question bank
question_bank = []
print(question_bank)

# 3b. Loop through the question_data
for question in question_data:
        # 3c. Get question text and question answers from teh question_data list
        question_text = question["question"]
        question_answer = question["correct_answer"]
        # 3d. Create a new question using imported Class
        new_question = Question(question_text, question_answer)
        # 3e. Add question to the question_bank list
        question_bank.append(new_question)

# 3f. Test to see if the loop is working
# print(question_bank[1].text)
# Prints a list of Question objects

# Step 6: Create new QuizBrain object using the QuizBrain Class and pass in the question_bank
quiz = QuizBrain(question_bank)
# 6a. Run the next_quesiton method on the object we created
quiz.next_question()

# 7a. Create a "game loop" (while loop) to run the game
while quiz.still_has_questions():
    # 7b. Move the quiz.next_question() from step 6a. into the while loop
    quiz.next_question()

# Step 9. Notify the user when the quiz is completed and show the 
print("You have completed the quiz!", f"Your final score was: {quiz.score}/{quiz.question_number}")