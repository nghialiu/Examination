def func5(n):
    uoc_so = []
    bientam = ""
    if n >= 100 and n <= 9999:
        for i in range(1, n+1, 1):
            if n % i == 0:
                uoc_so.append(i)
        str_n = str(n)
        for c in range (len(str_n)):
            bientam = str(c) + bientam
            if c == 0: 
                print('So co ton tai so 0')
    else:
        print("hay nhap mot so co 3-5 chu so")
    print("uoc so cua n la: " , uoc_so)
    print(int(bientam))
    return uoc_so, int(bientam)
if __name__=="__main__":
    n = int(input("Hay nhap mot so co 3-5 chu so: "))
    func5(n)
