class Test:
    key = ""
    name = ""
    description = ""
    questions = dict()
    def add_question(self, name, questions, rightQuestion):
        self.questions[name] = [
            name,
            questions,
            rightQuestion
        ]
    def get_question(self, key):
        for question in self.questions:
            if(question == key):
                return self.questions[question]
    def start(self):
        print("Start of test: " + self.name)