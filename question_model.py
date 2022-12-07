# Step 1: Create a question model (Class)

# Create a Class that can be used as a constructor to build new questions within the game

class Question:
    # Use the __init__ dunder method to indicate the function is a constructor
    # Set up 2 attributes for the question text and answer

    def __init__(self, q_text, q_answer):
        # Use the "self"
        self.text = q_text
        self.answer = q_answer

# Test to make sure it is functioning properly
# new_q = Question("Are you ready for this quiz?!?!?!?!?!?", "False")
# print(new_q.text)
# print(new_q.answer)