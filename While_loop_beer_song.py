def num_beers(n):
    while n >= 1:
        print n, "Bottles of beer on the wall "
        print n, "Bottles of beer"
        print "If one of those bottles should happen to fall"
        print (n - 1), "Bottles of beer on the wall\n"
        n -= 1

if num_beers == 0:
    print " 0 Bottles of beer on the wall"



num_beers(99)
