def count(path,ext):
    import os

    if os.path.isfile(path):
        return _count_lines(path),1
    elif os.path.isdir(path):
        file_counter = 0
        line_counter = 0
        for root,folders,files in os.walk(path):
            for file_name in files:
                if file_name.lower().endswith(ext):
                    file_path = os.path.join(root,file_name)
                    file_counter += 1
                    line_counter += _count_lines(file_path)

        return line_counter,file_counter
    else:
        raise Exception("Wrong path!")

def _count_lines(path):
    with open(path,"r") as fp:
        contents = fp.readlines()

    line_counter = 0
    for line in contents:
        if line.strip() != "":
            line_counter += 1

    return line_counter

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Counts lines in text files')
    parser.add_argument('-i', dest='input', type=str, help='Input folder or file')
    parser.add_argument('-e', dest='ext', type=str, required=False, default="py", help='File extension. Default is "py"')

    args = parser.parse_args()

    lines,files = count(args.input,args.ext)

    print "Counted " + str(lines) + " line(s) in " + str(files) + " file(s)."