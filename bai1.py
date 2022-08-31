
def func1(ngaysinh, thangsinh, namsinh):
    if ngaysinh >= 1 and ngaysinh <= 31 and thangsinh >= 1 and thangsinh <=12 and namsinh > 0:
        if thangsinh == 2:
            if namsinh % 4 == 0 and ngaysinh <=29:
                return True
            elif namsinh % 4 != 0 and ngaysinh <=28:
                return True
            else:
                print("Ngay thang nam khong hop le, moi nhap lai!")
        elif thangsinh == 4 or thangsinh == 6 or thangsinh == 9 or thangsinh == 11 and ngaysinh <=30:
                return True
        else:
            print("Ngay thang nam khong hop le, moi nhap lai!")
    else: 
        print("Ngay thang nam khong hop le, moi nhap lai!")
    return ngaysinh, thangsinh, namsinh

def ngay_thi(ngaythi, thangthi, namthi):
    if ngaythi >= 1 and ngaythi <= 31 and thangthi >= 1 and thangthi<=12 and namthi > 0:
        if thangthi == 2:
            if namthi % 4 == 0 and ngaythi <=29:
                return True
            elif namthi % 4 != 0 and ngaythi <=28:
                return True
            else:
                print("Ngay thang nam khong hop le, moi nhap lai!")
        elif thangthi == 4 or thangthi == 6 or thangthi == 9 or thangthi == 11 and ngaythi <=30:
                return True
        else:
            print("Ngay thang nam khong hop le, moi nhap lai!")
    else: 
        print("Ngay thang nam khong hop le, moi nhap lai!")
    return ngaythi, thangthi, namthi

if __name__=="__main__":
    ten = input("Hay nhap ho va ten cua ban: ")
    monhoc = input("Hay nhap mon hoc cua ban: ")
    print("Hay nhap ngay thang nam sinh cua ban:")
    ngaysinh =int(input)
    thangsinh = int(input("Thangsinh: "))
    namsinh = int(input("namsinh: "))
    print("Hay nhap ngay thi: ")
    ngaythi =int(input("Ngay sinh: "))
    thangthi = int(input("Thang: "))
    namthi = int(input()) 
    func1(ngaysinh, thangsinh, namsinh)
    ngay_thi(ngaythi, thangthi, namthi)
    print("Name: ", ten)
    print("DoB: ",ngaysinh, thangsinh, namsinh)
    print("Subject: ", monhoc) 
    print("Date: ", ngaythi, thangthi, namthi)

   


