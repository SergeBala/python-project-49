import prompt
import brain_games.cli as cli


NUMBER_OF_ANSWERS_TO_WIN = 3


def run_game(rules, get_quest_and_answ):
    player_name = cli.welcome_user()
    print(rules)
    correct_answers_counter = 0
    while correct_answers_counter < NUMBER_OF_ANSWERS_TO_WIN:
        current_question, correct_answer = get_quest_and_answ()
        print(f"Question: {current_question}")
        players_answer = prompt.string("Your answer: ")
        if players_answer == str(correct_answer):
            print("Correct!")
            correct_answers_counter += 1
        else:
            print(f"\'{players_answer}\' is wrong answer ;(."
                  + f"Correct answer was \'{correct_answer}\'.\n"
                  + f"Let's try again, {player_name}!")
            return
    print(f"Congratulations, {player_name}!")
