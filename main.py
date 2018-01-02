
# iterate 1 to 100
for x in range(1, 101):

# try mod 3 & mod 5
    modThree = x % 3
    modFive = x % 5

# if both, print cracklepop
    if (modThree == 0 and modFive == 0):
        print "value: CracklePop"
# if mod 3 only, print crackle
    elif (modThree == 0 and modFive > 0):
        print "value: Crackle"
# if mod 5 only, print pop
    elif (modFive== 0 and modThree > 0):
        print "value: Pop"
# if neither print the number itself
    else:
        print "value: %d" % (x)
