import sys
from tabulate import tabulate

from rule_manager import RuleManager, option_to_str
from random import randint

HEADERS = ['Last Choice', 'Second to Last Choice', 'Consequent', 'Weight', 'Valid']


def main(debug=False):
    rules_manager = RuleManager()
    last_choice = 0
    second_to_last_choice = 0
    current_choice = -1
    computer_win = 0
    user_win = 0
    ties = 0
    round = 1

    while True:
        print("\nRound: %d" % round)

        # First make computer's choice so there is no way to know users input before it makes its decision
        if round <= 2:
            computer_choice = randint(1, 3)
        else:
            rules_manager.check_rules(second_to_last_choice, last_choice, debug)
            computer_choice = rules_manager.select_rule_and_get_consequent()

        # Ask for user input
        while current_choice < 0 or current_choice > 3:
            current_choice = int(input("Choose: 0-EXIT 1-STONE 2-PAPER 3-SCISSORS: "))

        if current_choice == 0:
            exit()

        if debug:
            print tabulate(rules_manager.debug_info, headers=HEADERS, tablefmt="fancy_grid")

        print('Your choice: %s My choice: %s' % (option_to_str(current_choice), option_to_str(computer_choice)))

        # User plays STONE
        if current_choice == 1 and computer_choice == 2:
            computer_win += 1
            rules_manager.set_success(True)
            print('I win!')
        elif current_choice == 1 and computer_choice == 3:
            user_win += 1
            rules_manager.set_success(False)
            print('You win!')
        elif current_choice == 1 and computer_choice == 1:
            ties += 1
            rules_manager.set_success(False)

        # User plays PAPER
        if current_choice == 2 and computer_choice == 1:
            user_win += 1
            rules_manager.set_success(False)
            print('You win!')
        elif current_choice == 2 and computer_choice == 3:
            computer_win += 1
            rules_manager.set_success(True)
            print('I win!')
        elif current_choice == 2 and computer_choice == 2:
            ties += 1
            rules_manager.set_success(False)

        # User plays SCISSORS
        if current_choice == 3 and computer_choice == 1:
            computer_win += 1
            rules_manager.set_success(True)
            print('I win!')
        elif current_choice == 3 and computer_choice == 2:
            user_win += 1
            rules_manager.set_success(False)
            print('You win!')
        elif current_choice == 3 and computer_choice == 3:
            ties += 1
            rules_manager.set_success(False)

        print('-----------------------------------------------------------------------------------------')
        print('You won: %d I won: %d Ties: %d' % (user_win, computer_win, ties))
        print('-----------------------------------------------------------------------------------------')

        second_to_last_choice = last_choice
        last_choice = current_choice
        current_choice = -1
        round += 1


if __name__ == '__main__':
    debug = False

    if '--debug' in sys.argv:
        debug = True

    main(debug)
