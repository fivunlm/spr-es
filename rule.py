class Rule:
    def __init__(self):
        self.last_choice = 0
        self.second_to_last_choice = 0
        self.consequent = 0
        self.weight = 0
        self.valid = False

    def set(self, last, second_to_last, consequent):
        self.last_choice = last
        self.second_to_last_choice = second_to_last
        self.consequent = consequent

    def validate(self, last, second_to_last):
        self.valid = self.last_choice == last and self.second_to_last_choice == second_to_last

    def set_succeed(self, succeed):
        self.weight = self.weight + 1 if succeed else self.weight - 1