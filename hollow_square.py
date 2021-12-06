n = int(input("how large? : "))

for kolom in range (n):
    for baris in range (n):
        if baris==0 or kolom %(n-1)==0 or kolom==0 or baris %(n-1)==0:
#the space in end is n
            print('*',end=' ')
#the print in the else code needs n+1 form the print in if syntax to make a perfect square
        else :
            print('  ',end='')
    print(" ")
