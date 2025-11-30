#video bai 3 ytb 
a=int(input("Nhập vào a:"))
Nhập vào a:90
>>> a=int(a)
>>> a=a+3
>>> print("giá trị sau khi cộng của a:",a)
giá trị sau khi cộng của a: 93
>>> if a>0: print (a, "là số dương.")
... else:
...     print(a, "là số âm.")
...
93 là số dương.
>>> a=int(input("Nhập vào a:"))
Nhập vào a:-90
>>> while True: #vòng lặp vô hạn
...     a=int(input("Nhập vào a:"))
...     a=a-9
...     print("Giá trị sau cùng:",a)
...     if a>0: print(a,"là số dương")
...     else: print(a, "là số âm.")
...     print()
...
Nhập vào a:0
Giá trị sau cùng: -9
-9 là số âm.

Nhập vào a:100
Giá trị sau cùng: 91
91 là số dương

#video bai 4 ytb
>>> print()# in ra dòng trống

>>> print(36); print("Rau ma thanh hoa!") # dấu ; để tách các câu lệnh
36
Rau ma thanh hoa!
>>> print("Con","Cho","Ni",36)
Con Cho Ni 36
#) thêm sep để phân cách các đối số(thêm dấu phẩy ngăn cách)
>>> print("Con","Cho","Ni",36, sep=",")
Con,Cho,Ni,36
 print('me','may','beo', end=':')   ; print("120kg") # end là kết thúc dòng bằng dầu nào đó
me may beo:120kg
print('Tên={0}, họ={1}'. format('Dang tran', 'dong')) #format là định dạng chuỗi (str), để mà đưa(chèn) dữ liệu vào trong chuỗi
Tên=Dang tran, họ=dong
 print("hello {name}, i'm {age} years old". format(name='Huy',age='18'))
hello Huy, i'm 18 years old
#video bai 5 ytb
 ho=input("Nhap vao ho:"); ten=input("Nhap vao ten:");
Nhap vao ho:DInh tran
Nhap vao ten:tuan kiet
>>> print("Xin chao", ho, ten)
Xin chao DInh tran tuan kiet

a=input("Nhập vào a:")
Nhập vào a:35 # input tra ve
print("a={0}".format(a))
a=35

input("chon 1 so bat ky: ")
chon 1 so bat ky: 35
'35'
#video bai 6 ytb
>>> x=5
>>> print(x)
5
>>> z=7
>>> z=36
>>> print(z)
36
>>> x,y,z=37,36,"Hello"
>>> print(x)
37
>>> print(x,y,z)
37 36 Hello
>>> x=y=z=36
>>> print(x,y,z)
36 36 36
>>> print(x)
36
>>> PI=3.14
>>> print(PI)
3.14
>>> PI=3.14159265
>>> print(PI)
3.14159265
>>> import math
>>> print(math.pi)
3.141592653589793

>>> full_name ="Nguyen Van Cu" # đặt tên biến tử tế 1 tý phù hợp với nội dung
>>> print(full_name)
Nguyen Van Cu
>>> fullname=" Nguyen van CU" # dùng _ và chữ in hoa thay cho dấu cách
>>> print(fullname)
 Nguyen van CU

#video bai 7 ytb
>>> x=1
>>> print(type(x)) #in ra kiểu dữ liệu của biến x
<class 'int'>

>>> e= 2.72
>>> print(type(e))
<class 'float'>
>>> PI= 3.14
>>> print(type(PI))
<class 'float'>
>>> x=("Hello world")
>>> print(type(x))
<class 'str'>
>>> text=" Xin chao"
>>> print(type(text))
<class 'str'>

#video bai 8 ytb 
#ép kiểu dữ liệu
>>> n=100
>>> m="36"
>>> #chuyển n sang số thực
>>> print(str(n)+m)
10036
>>> print(int(m)+n) # chuyển m sang số nguyên
136


#video bai 9 ytb
+, -,*, /, //, %, **

>>> a=input("Nhập vào số a:")
Nhập vào số a:36
>>> b=input("Nhập vào số b:")
Nhập vào số b:18
>>> a=float(a)
>>> b=float(b)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'float'>
>>> print("{0}+{1}={2}".format(a, b, a+b))
36.0+18.0=54.0
>>> print("{0}-{1}={2}".format(a, b, a-b))
36.0-18.0=18.0
>>> print("{0}*{1}={2}".format(a, b, a*b))
36.0*18.0=648.0
>>> print("{0}/{1}={2}".format(a, b, a/b))
36.0/18.0=2.0
>>> print("{0}%{1}={2}".format(a, b, a%b))
36.0%18.0=0.0
>>> print("{0}**{1}={2}".format(a, b, a**b))
36.0**18.0=1.0314424798490537e+28
>>> print("{0}//{1}={2}".format(a, b, a//b))
36.0//18.0=2.0
>>> a=int(a)
>>> b=int(b)
>>> print("{0}+{1}={2}".format(a, b, a+b))
36+18=54

#video bai 10 ytb
>>> x=input("x:")
x:25
>>> y=input("y:")
y:36
>>> print("{0}<{1} là {2}". format(x, y, x<y))
25<36 là True
>>> print("{0}>{1} là {2}". format(x, y, x>y))
25>36 là False
>>> print("{0}=={1} là {2}". format(x, y, x==y))
25==36 là False
>>> print("{0}!={1} là {2}". format(x, y, x!=y))
25!=36 là True
>>> print("{0}>={1} là {2}". format(x, y, x>=y))
25>=36 là False
>>> print("{0}<={1} là {2}". format(x, y, x<=y))
25<=36 là True
>>> z=input("z:")
z:10
>>> print((x>y) and (y<x))
False
>>> print((x<y) or (y<x))
True
>>> print(not(x>y>z)) # có not ở đằng trước có nghĩa là  không phải x lớn hơn y và y lớn hơn z 
True
>>> print(not(y>z)) # không phải y lớn hơn z
False
>>> print("({0}<{1}) and ({2}<{3}) = {4}". format(x,y,y,z, (x<y) and (y<z)))
(25<36) and (36<10) = False
>>> print("({0}<{1}) or ({2}<{3}) = {4}". format(x,y,y,z, (x<y) or (y<z)))
(25<36) or (36<10) = True
>>> print(" not ({0}<{1}) = {2}".format(x,z,not (x>z)))
 not (25<10) = False

 #video bai 11 ytb 
 #toan tu gan
 >>> a=5
>>> a+=3 # a=a+3
>>> print(a)
8

#video bai 12 ytb
#toan hoc math
import math
x==float(input("x:"))
print("pi=", math.pi)
pi= 3.141592653589793
print("|x|=", math.fabs(x))
|x|= 36.0
>>> print("sqrt(x)=", math.sqrt(x))
sqrt(x)= 6.0
>>> print("ceil(x)=", math.ceil(x))
ceil(x)= 36
