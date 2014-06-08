import re

with open("2014-06-07_0100.log") as fp:
    contents = fp.readlines()

regex = re.compile("Next day prediction: (?P<predict>[-0-9\.]*)\% Real data: (?P<real>[-0-9\.]*)\%")

for line in contents:
    match = regex.search(line)
    print "{0:.2f}".format(float(match.group("predict"))) + " ; "  + match.group("real")
