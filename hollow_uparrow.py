for kolom in range (9):
    for baris in range(7):
        if (kolom==3) or (kolom+baris==3) or (baris-kolom==3) or (baris==3 and kolom>=4) :
            print ('*',end=' ')
        else :
            print(" ",end=' ')
    print()