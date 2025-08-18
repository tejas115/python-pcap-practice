from os import strerror


def lipogram(letter):
    letter.lower()
    # Write a try/except block to open the oulipo file
    # use the absolute path /root/code/oulipo.txt
    # and handle an IOError
    try:
        txt = open("./oulipo.txt", "r")
    except IOError as e:
        # print the error with the use of strerror and errno
        print("I/O error: ". strerror(e.errno))
        txt = None
    except Exception as e:
        print(e)
    else:
        # Do the count here using sum(), map(), lambda
        # to count occurences of the letter
        count = sum(map(lambda x: 1 if letter in x else 0, txt))
        print(letter, "appears", count, "times")
    finally:
        if txt:
            txt.close()


lipogram("E")