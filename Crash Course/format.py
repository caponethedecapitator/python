for i in range(1, 10):
    for j in range(1, i + 1):
        print("%s = %s * %s" % (i * j, i, j), end = "\t")
        print("{0} = {1} * {2}".format(i * j, i, j), end = "\t")
        print(f"{i * j} = {i} * {j}", end = "\t")
    print("\n")