import random


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
    prog_len = random.randint(5, 10)
    prog_step = random.randint(-50, 50)
    prog_start = random.randint(0, 20)
    prog_list = []
    for i in range(prog_len):
        prog_list.append(prog_start + (i * prog_step))
    index_to_omit = random.randint(0, prog_len - 1)
    prog_str = format_prog_list_into_str(prog_list, index_to_omit)
    answer = str(prog_list[index_to_omit])
    return prog_str, answer
