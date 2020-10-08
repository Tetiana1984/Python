def check_range(left,right):
    nl=[]
    for x in range(left, right+1):
        if (x%7==0) and (x%5!=0):
            nl.append(str(x))
    print (','.join(nl))

while True:
    try:
        left_bounder = int(input("Give the left bounder: "))
        righ_bounder = int(input("Give the right bounder: "))
        if left_bounder > righ_bounder:
            raise Exception("Еhe left border cannot be larger than the right ")
        check_range(left_bounder, righ_bounder)
        cont = input("Want to add another? (N or Enter)")
        if cont.lower().strip() == "n":
            break;
    except Exception as e:
        print("Error: %s" % e )
