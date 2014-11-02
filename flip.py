def flip(a):
    print "range of indices:",range(0,len(a)-1)
    print "initial array:",a
    for i in range(0,len(a)-1):
        a.insert(0,a[-1])
        a[-1]=[]
        print a
    return a
