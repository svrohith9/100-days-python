class Quiz:
    def __init__(self, question_list):
        self.questions = question_list
        self.question_number = 0
        self.score = 0
    
    def has_next_question(self):
        if self.question_number < len(self.questions):
            return True
        return False
    
    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1  # increment question so next question comes at next iteration and Q.no displays correct
        user_input = input(f"Q.{self.question_number} {current_question.question} (True/ False)?: ")
        if self.check_answer(user_input):
            self.score += 1
        print(f"Current Score: {self.score}")
        print("\n")
    
    def check_answer(self, answer):
        return answer.lower() == self.questions[self.question_number - 1].answer.lower()
