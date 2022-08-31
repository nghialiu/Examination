def func3(mang):
    sole = []
    songuyento = []
    chimuc = 0
    for i in mang:
        if i % 2 != 0:
            sole.append(i)
    for i in range (3, mang[chimuc], 1):
        if mang[chimuc] % i == 0:
                tmp = False
        else:
            songuyento.append(i)

    print("So nguyen to la: {}". format(songuyento))
    print("So le la: {}". format(sole))    
    return sole, songuyento

if __name__=="__main__":
    mang = [1, 2, 3, 4, 5, 10, 14, 15, 17, 18, 21, 22, 23, 33, 34, 45, 91, 95]
    print(func3(mang))

        
