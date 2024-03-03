import prompt


def play_a_game(player_name, rules, get_quest, get_answ, nb_of_answ_to_win=3):
    print(rules)
    correct_answers_counter = 0
    while (correct_answers_counter < nb_of_answ_to_win):
        current_question = get_quest()
        correct_answer = get_answ(current_question)
        print(f"Question: {current_question}")
        players_answer = prompt.string("Your answer: ")
        if players_answer == correct_answer:
            print("Correct!")
            correct_answers_counter += 1
            if correct_answers_counter == 3:
                print(f"Congratulations, {player_name}!")
        else:
            print(f"\'{players_answer}\' is wrong answer ;(."
                  + f"Correct answer was \'{correct_answer}\'.\n"
                  + f"Let's try again, {player_name}!")
            break
