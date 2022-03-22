# for y in range(1, 10):
#     for x in range(1, 10):
#        print("{:3},".format(y * x), end="")
#    print("")

for y in range(1, 10):
    a = ["{:3}".format(x * y) for x in range(1,10)]
    print(",".join(a))
