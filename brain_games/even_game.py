import random
import prompt


def is_even(number):
    return number % 2 == 0


def get_random_number(start_of_range=0, end_of_range=1000):
    return random.randint(start_of_range, end_of_range)


def get_correct_answer(number):
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def even_game(players_name, number_of_correct_answers_to_win=3):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    correct_answers_counter = 0
    while (correct_answers_counter < number_of_correct_answers_to_win):
        current_number = get_random_number()
        correct_answer = get_correct_answer(current_number)
        print(f"Question: {current_number}")
        players_answer = prompt.string("Your answer: ")
        if players_answer == correct_answer:
            print("Correct!")
            correct_answers_counter += 1
            if correct_answers_counter == 3:
                print(f"Congratulations, {players_name}!")
        else:
            print(f"\'{players_answer}\' is wrong answer ;(.Correct answer was \'{correct_answer}\'.\n"
                  + f"Let's try again, {players_name}!")
            break
