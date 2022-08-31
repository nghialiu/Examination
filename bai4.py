from math import sqrt


def func4(chieudai, chieurong):
    chuvi = 0
    dientich = 0
    duongcheo = 0
    if chieudai > 0 and chieurong > 0:
        chuvi = (chieudai + chieurong) * 2
        dientich = chieudai * chieurong
        if chieudai == chieurong:
            print("Day la mot hinh vuong!")

        duongcheo = sqrt ((chieudai**2)+(chieurong**2))
    else:
        print("Chieu dai va chieu rong loi")
    return chuvi, dientich, duongcheo

if __name__ == "__main__":
    chieurong = float(input("hay nhap chieu rong: "))
    chieudai = float(input("Hay nhap chieu dai: "))
    print(func4(chieudai, chieurong))