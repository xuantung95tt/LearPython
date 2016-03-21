__author__ = 'crypto5'
import math
import random

#Bai toan: tim x trong khoang [-1,2] de f co gia tri lon nhat#
#voi f = x * sin(10pi * x) + 1
#------------------------------------------------------------#

#Thuat toan su dung: Thuat giai di truyen#

#Buoc 1: Bieu dien                       #
#Su dung vecto nhi phan lam nhiem sac the de bieu dien cac gia#
#tri thuc cua bien x. Chieu dai vecto phu thuoc vao do chinh  #
#xac can co, o day gia su la 6 so le.
#Mien gia tri bang 3 nen phai chia khoang gia tri thanh 3*10^6#
#khoang co kich thuoc bang nhau, co nghia la can 22 bit cho   #
#vecto nhi phan. Anh xa chuoi nhi phan thanh so x can qua hai #
#buoc:

def BieuDien(src):
    #doi chuoi nhi phan sang co so 10:
    _x = int(src,base=2)
    #tim so thu x tuong ung
    x= -1 + float(_x)*3/(pow(2,22)*3)
    f=x*math.sin(10*math.pi*x)+1
    return f
#Buoc 2: Khoi tao quan the
#Tao gia tri ngau nhien cho cho quan the, moi NST la vecto nhi #
#22bit voi kich thuoc quan the la 50

#Tao chuoi nhi phan:
def TaoChuoiADN():
    kq=""
    for i in range(22):
        kq+=str(random.randint(0,1))
    return kq

quanThe=[]
for i in range(5):
    quanThe.append(TaoChuoiADN())

#Buoc 3: Ham luong gia trinh la ham f
#Buoc 4: Cac phep toan di truyen
#Xac suat lai tao la 25%, xac suat dot bien la 1%, tong so ca the#
#la 50

p_c=0.25    #xac suat lai tao
p_m=0.01    #xac suat dot bien
pop_size=5  #kich tuoc quan the

quanTheThichNghi=quanThe
print(quanThe)
dem=0       #dem so lan lap
while (dem <= 1):

    quanTheMoi=quanTheThichNghi

    #quan trinh dot bien la p_m % 1 bit bat ki trong 1 ca the bi dot bien#
    for indexQuanThe in range(pop_size):
        if int(p_m*22*pop_size)<1: break
        for i in range(int(p_m*22*pop_size)):
            indexADN=random.randint(0,21)
            temp = quanTheMoi[indexQuanThe][indexADN]

            if temp=='1':
                quanTheMoi[indexQuanThe]=quanTheMoi[indexQuanThe][0:indexADN-1]+"0"+quanTheMoi[indexQuanThe][indexADN+1:21]
            else: quanTheMoi[indexQuanThe]=quanTheMoi[indexQuanThe][0:indexADN-1]+"1"+quanTheMoi[indexQuanThe][indexADN+1:21]

            #dot bien xong thi cong vao quan the moi
            quanTheMoi.append(quanThe[indexQuanThe][indexADN])
    print(quanTheMoi.__len__())
    #qua trinh lai tao la p_c % ca the v duoc chhon de lai tao
    quanTheLai=[]

    def PhepLai(src1, src2):
        indexLai=random.randint(0,21)
        #sinh ra hai con moi
        _src1=src1[0:indexLai-1]+src2[indexLai:len(src2)-1]
        _src2=src2[0:indexLai-1]+src1[indexLai:len(src2)-1]
        quanTheMoi.append(_src1)
        quanTheMoi.append(_src2)
        return

    #tao quan the lai
    for i in range(int(p_c*pop_size)):
        j=random.randint(0,pop_size-1)
        #print(j, quanTheThichNghi.__len__())
        quanTheLai.append(quanTheThichNghi[j])


    #lai tao
    while j == len(quanTheLai):
        #phan tu j lai voi mot phan tu ngau nhien
        #sau khi lai thi tach ra khoi quan the lai
        j=0
        if len(quanTheLai)==1 or len(quanTheLai)==0: break
        index1=j
        index2=j
        while index2==index1:
            index2=random.randint(0,quanTheLai.__len__()-1)
        print(index1, index2)
        PhepLai(quanTheLai[index1],quanTheLai[index2])
        name1=quanTheLai[index1]
        name2=quanTheLai[index2]
        quanTheLai.remove(name1)
        quanTheLai.remove(name2)

    #sap xep va loai bo
    doThichNghi={}
    for cathe in quanTheMoi:
        doThichNghi[cathe]=BieuDien(cathe)
    index=0
    for i in range(quanTheMoi.__len__(),0,-1):
        if index==50: break
        for j in range(0,i-1,1):
            if(doThichNghi[quanTheMoi[j]] < doThichNghi[quanTheMoi[j+1]]):
                #print(doThichNghi.__len__())
                quanTheThichNghi[index]=quanTheMoi[j+1]
                index+=1


    print(BieuDien(quanTheThichNghi[0]))
    dem+=1



