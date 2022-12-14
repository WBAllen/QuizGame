# Step 4: Bring up question and ask the user to answer the question
# All of quiz functionality will be in this file

# 4a. Create a class called QuizBrain
class QuizBrain:
    # 4b. Create constructor to initialize the necessary attributes: question number and user score which will have default values and question list which will be passed into the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    # 4c. Create a Method that retrieves the question from the question list (Created in main.py)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # 4d. Lists start at 0, so to display the correct question number for the next step increase question number by 1
        self.question_number += 1
        # 4e. Show the number, text 
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        # 8e. When advancing to the next question, check the user's answer

    # Step 7: Create a Method that advances the questions after user has answered
    def still_has_questions(self):
        # This method will return a Boolean
        return self.question_number < len(self.question_list)
    
    # Step 8: Create a Method that checks the user's answer
    def check_answer(self, user_answer, correct_answer):
            # 8a. Create if/else statement that compares user and correct answer, be sure to account for varying cases in user's answer
            if user_answer.lower() == correct_answer.lower():
                # 8b. Increase 
                self.score += 1
                # 8c. Let the user know they are correct
                print("You got it right! WOOOO! :) <3")
            # 8d. Create else statement for when the user gets the answer wrong
            else:
                print("You answer is incorrect :(")
            

            # 8f. Display correct answer
            print(f"The correct answer is: {correct_answer}")
            # 8g. Displays the users score out of how many questions have been asked
            print(f"Your current score is: {self.score}/{self.question_number}")
            # 8h. Create a space between the question for readability
            print("\n")

            
