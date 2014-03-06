for idx in range(3):
    try:
        print "Raising Exception"
        raise Exception
    except:
        print "Catching exception and continue"
        continue
    else:
        print "You should not see this"
        break
    finally:
        print "Finally clause"
else:
    print "You should see this as last line"