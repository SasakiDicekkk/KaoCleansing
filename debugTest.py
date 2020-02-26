def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbolは１文字の文字列でなければならない')