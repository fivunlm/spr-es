import sys

from rule import Rule


def option_to_str(option):
    if option == 1:
        return "STONE"
    if option == 2:
        return "PAPER"
    if option == 3:
        return "SCISSORS"
    return '[%d]' % option


class RuleManager:

    def __init__(self):
        self.rules = []
        self.debug_info = []
        self.selected_rule_index = 0

        # Init rules, this domain is simple and known so we can define each one of the rules
        for last in range(1, 4):
            for second_to_last in range(1, 4):
                for consequent in range(1, 4):
                    rule = Rule()
                    rule.set(last, second_to_last, int(consequent))
                    self.rules.append(rule)

    def check_rules(self, last, second_to_last, debug=False):
        self.debug_info = []

        for rule in self.rules:
            rule.validate(last, second_to_last)

            if debug:
                self.debug_info.append([option_to_str(rule.last_choice), option_to_str(rule.second_to_last_choice),
                    option_to_str(rule.consequent), rule.weight, str(rule.valid)])

    def select_rule_and_get_consequent(self):
        """
        Will go trough all valid rules and will select the heaviest one
        :return:
        """
        aux_weight = - sys.maxint
        consequent = 0
        for index, rule in enumerate(self.rules):
            if rule.valid and rule.weight > aux_weight:
                aux_weight = rule.weight
                consequent = rule.consequent
                self.selected_rule_index = index

        return consequent

    def set_success(self, result):
        self.rules[self.selected_rule_index].set_succeed(result)
