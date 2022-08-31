map_thang = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec"
}
def func2(ngay,thang,nam):
    if ngay >= 1 and ngay <= 31 and thang >= 1 and thang<=12 and nam > 0:
        if thang == 2:
            if nam % 4 == 0 and ngay <=29:
                return True
            elif nam % 4 != 0 and ngay <=28:
                return True
            else:
                print("Ngay thang nam khong hop le, moi nhap lai")
        elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
            if ngay <= 30:
                return True
            else: 
                print("Ngay thang khong hop le, moi nhap lai!")
        if ngay == 1 and thang == 1:
            print("ngay Tet")
        elif ngay == 30 and thang == 4:
            print("Ngay giai phong Dan toc ")
        elif ngay == 1 and thang == 5:
            print("ngay quoc te lao dong")
        elif ngay == 19 and thang == 5: 
            print("Ngay sinh nhat Bac Ho")
        elif ngay == 2 and thang == 9:
            print("Ngay quoc khanh")
    else: 
        print("Ngay thang nam khong hop le, moi nhap lai!")
    
    return ngay, thang, nam

if __name__ =="__main__":
    ngay = int(input("Hay nhap ngay: "))
    thang = int(input("Hay nhap thang: "))
    nam = int(input("Hay nhap nam: "))
    func2(ngay, thang, nam)
    print(ngay, map_thang[thang], nam)