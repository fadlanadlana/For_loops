num = int(input('p: '))
for i in range (num+1):
    for j in range (0,num+1):
        #buat sisi atas sama sisi samping kiri
        if (i >= 0 and j <=0 ) :
            print (i,end=" ")
        #biar rapi baris nya gaada 0 dan baris nya ga nyebar 
        if (i <=0  and j!=0) :
            print (j,end=" ")
        #bikin sisi bawah
        if i==num and j==num :
            for x in range (num,-1,-1):
                if x != num:
                    print(x,end=" ")
    print() 