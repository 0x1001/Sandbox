if __name__ == "__main__":
    import multiprocessing
    import time

    p = multiprocessing.Pool(10)

    for i in range(20):
        print "Task: " + str(i)
        p.apply_async(time.sleep,(2,))

    print "Waiting..."
    p.close()
    p.join()
