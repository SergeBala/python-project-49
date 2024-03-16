from random import randint
from brain_games.constants import RANGE_START, RANGE_END


PROG_RULES = "What number is missing in the progression?"
MIN_NB_OF_ELEMS = 5
MAX_NB_OF_ELEMS = 10
MIN_STEP = -50
MAX_STEP = 50


def format_prog_list_into_str(prog_list, index_to_omit):
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


def get_quest_and_answ_prog():
    prog_len = randint(MIN_NB_OF_ELEMS, MAX_NB_OF_ELEMS)
    prog_step = randint(MIN_STEP, MAX_STEP)
    prog_start = randint(RANGE_START, RANGE_END)
    prog_list = []
    for i in range(prog_len):
        prog_list.append(prog_start + (i * prog_step))
    index_to_omit = randint(0, prog_len - 1)
    prog_str = format_prog_list_into_str(prog_list, index_to_omit)
    answer = str(prog_list[index_to_omit])
    return prog_str, answer
