def depict_abacus(number):
    number = str(number) # mozda i je string
    print(f"Abacus for number: {number}")

    for i in range(0,4):

        line = int(number[i])

        # start and end point
        wall = "|"

        # left part
        left_integer = 9 - line
        left_depicted = "x" * left_integer

        # middle part
        middle_depicted = "-" * 6

        # right part
        right_depicted = "x" * line

        full_line = wall+left_depicted+middle_depicted+right_depicted+wall

        print(full_line)

depict_abacus(1678)