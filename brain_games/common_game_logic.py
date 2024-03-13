import prompt
import brain_games.cli as cli


def play_a_game(rules, get_quest_and_answ, nb_of_answ_to_win=3):
    player_name = cli.welcome_user()
    print(rules)
    correct_answers_counter = 0
    while (correct_answers_counter < nb_of_answ_to_win):
        current_question, correct_answer = get_quest_and_answ()
        print(f"Question: {current_question}")
        players_answer = prompt.string("Your answer: ")
        if players_answer == str(correct_answer):
            print("Correct!")
            correct_answers_counter += 1
            if correct_answers_counter == 3:
                print(f"Congratulations, {player_name}!")
        else:
            print(f"\'{players_answer}\' is wrong answer ;(."
                  + f"Correct answer was \'{correct_answer}\'.\n"
                  + f"Let's try again, {player_name}!")
            break
