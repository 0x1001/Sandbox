import cProfile
import random
import StringIO
import string
import pstats
import sys

if __name__ == "__main__":
    test_range = 10000

    init = ""
    for i in range(test_range):
        init += "a" + str(i) + " = {}\n"

    exec(init)

    cmd = "r = random.randint(0,10)\n"
    cmd += "r_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1000))\n"

    for i in range(test_range):
        cmd += "a" + str(i) + "[r_str]=r\n"

    p = cProfile.Profile()
    s = StringIO.StringIO()
    result = []
    print ""
    for i in range(10000):
        p.run(cmd)
        ps = pstats.Stats(p, stream=s)
        ps.print_stats()
        result.append(float(s.getvalue().split("\n")[0].strip().split(" ")[4]))
        sys.stdout.write(".")

    print ""
    avg = sum(result)/len(result) + 0.00001
    print "Avrage: " + str(avg)

    for i,n in enumerate(result):
        if n > avg:
            print str(i) + " : " + str(n)
