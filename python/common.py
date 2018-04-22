def wait_for_start(serial):
    line = serial.readline()

    if "Hello Audio 1.0" in line.decode("utf8"):
        print("Connected!")
        return
    else:
        raise Exception("Wrong start message: " + line.decode("utf8"))


def get_value(line):
    return int(line.decode("utf8")[1:].strip())


def first_button(line):
    return line.decode("utf8").startswith("A")


def second_button(line):
    return line.decode("utf8").startswith("B")