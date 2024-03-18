from random import randint
from brain_games.constants import RANGE_START, RANGE_END


RULES = "What number is missing in the progression?"
MIN_NB_OF_ELEMS = 5
MAX_NB_OF_ELEMS = 10
MIN_STEP = -50
MAX_STEP = 50


def format_list_to_str(prog_list, index_to_omit):
    i = 0
    prog_len = len(prog_list)
    prog_str = ""
    for i in range(prog_len):
        if i != index_to_omit:
            prog_str += str(prog_list[i])
        else:
            prog_str += ".."
        if i != prog_len - 1:
            prog_str += " "
    return prog_str


def get_quest_and_answ():
    len = randint(MIN_NB_OF_ELEMS, MAX_NB_OF_ELEMS)
    step = randint(MIN_STEP, MAX_STEP)
    start = randint(RANGE_START, RANGE_END)
    list = []
    for i in range(len):
        list.append(start + (i * step))
    index_to_omit = randint(0, len - 1)
    list_as_string = format_list_to_str(list, index_to_omit)
    answer = str(list[index_to_omit])
    return list_as_string, answer
