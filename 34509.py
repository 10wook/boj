for i in range(10,100):
    a = str(i)[1]+str(i)[0]
    b = int(a)
    if b %4 ==0:
        if (int(a[0])+int(a[1]))%6 ==0:
            if '8' not in a:
                print(i)
            else:
                continue
        else :
            continue
        pass
        
    else:
        continue