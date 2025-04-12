import numpy as np
import math
a=np.array([1,2,3,4])
def check_1():
    print(a)
    print(a.ndim)

b=np.array([[1,2,4],[3,4,5],[3,4,4]])

def check_2():
    print(b)
    print(b.ndim)
    print(b.shape)
    print(b.dtype)
    print(b.dtype.name)

c=np.zeros((2,6))    #two brackets
d=np.ones((3,2))
e=np.full((3,2),7)    #important
f=np.random.rand(2,3)   #one bracket
g=np.arange(10,20,3)    # start, stop, range
h=np.linspace(10,20,4)
def check_3():
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)

a1=np.array([[1,2],[3,4],[3,4]])
a2=np.array([[4,6],[4,7],[3,4]])
a3=np.array([[1,2,3],[2,3,1]])
def check_4():
    print(a1+a2)
    print(a1*a2)
    print(a1.shape)
    print(a3.shape)
    print(a1 @ a3)   #matrix multiplication

fahrenheit=np.array([0,-2,-10,-5,15])
celsius= (fahrenheit-32)*5/9
def check_5():
    print(celsius)
    print(celsius>-20)    #boolean
    print(celsius%2==0)   #boolean

b1=np.array([1,0.5,9.0])
b2=np.array([0,4,5])
b3=b1+b2
b4=b1*b2

b5=np.array([[1,2.0],[3,4],[3,4]])
b6=np.array([[1,2,3],[2,3,1]])
b7=b5@b6
def check_6():
    print(b1.dtype)
    print(b2.dtype)
    print(b3.dtype)
    print(b4.dtype)
    print(b5.dtype)
    print(b7.dtype)

c1=np.array([[4,2,3],[1,5,6]])
def check_7():
    print(c1.sum())
    print(c1.min())
    print(c1.max())
    print(c1.mean())

d1=np.arange(10,50,5)
d2=d1.reshape(2,4)
def check_8():
    print(d1)
    print(d2)

from PIL import Image
def array_to_image():
    im = Image.open(r"C:\Users\THINKPAD\Downloads\FB_IMG_1739677603238.jpg")
    # im.show()
    array = np.array(im)
    print(array.shape)
    print(array)

    # mask=np.full((array.shape),255)

    modified_array = 255 - array  # invert
    modified_mask_image = Image.fromarray(modified_array.astype("uint8"))
    # modified_mask_image.show()

    reshaped = np.resize(modified_array, (692, 173, 3))
    print(reshaped.shape)
    Image.fromarray(reshaped).show()

b5=np.array([[1,2.0],[3,4],[3,4]])
b6=np.array([[1,2,3],[2,3,1]])
def check_9():
    print(b5[1, 0])
    print([b5[1, 0], b6[0, 2], b6[1, 1]])
    print(b5[[0, 2, 1], [1, 0, 1]])  # important

def check_10():
    print(b5>2)
    print(b5[b5>2])    #important

c1=np.array([5,1,6,9,7])
c2=np.array([[5,1,6,9,7],[1,2,4,2,7],[0,2,4,2,5]])
def check_11():
    print(c1[1:4])   #onedimentional
    print(c2[:2])     #multidimentional
    print(c2[:2,1:4])   #multidimentional

def check_12():
    subarray2=c2[:2,1:4]
    print(subarray2)
    c1[2]=4         #changing a value
    print(c1)
    subarray2[0,1]=10
    print(subarray2)
    print(c2)     #changing subarray changes the original array
#check_12()
wines=np.genfromtxt(r"C:\Users\THINKPAD\Downloads\winequality-red.csv",delimiter=";",skip_header=1)
#np.set_printoptions(threshold=np.inf)   # to see full data

def check_13():
    print(wines)
    print(wines[0, :2])

    print(wines[:, :1])
    print(wines[:, 1:4])
    print(wines[:, -3])
    print(wines[:, [0, 2, 4]])
    print(wines[[0, 2, 4], :])
    print(wines[:, -3].mean())
    print(wines[:, 3].mean())

graduate_admission = np.genfromtxt(r"C:\Users\THINKPAD\Downloads\Admission_Predict.csv",dtype=None, delimiter=',', skip_header=1,names=('Serial No','GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
                                          'LOR','CGPA','Research', 'Chance of Admit'))
#using "dtype=None" creates structured array(tuple rows)
#print(wines)
def check_14():
    print(graduate_admission)
    print(graduate_admission.shape)
    print(graduate_admission["CGPA"][:4])
    graduate_admission["CGPA"] = (graduate_admission["CGPA"] / 10) * 4  # changes the data, changes CGPA into out of 4
    print(graduate_admission["CGPA"])
    print(graduate_admission)   #data is changed
    print(graduate_admission[graduate_admission["Research"]==1])  # sorting the students how have research
    print(len(graduate_admission[graduate_admission["Research"]==1]))
    print(graduate_admission[graduate_admission["Chance_of_Admit"] > 0.8])
    # dtype=None changes the space into "_", so we need to write this
    print(graduate_admission["GRE_Score"].mean())
    print(graduate_admission[graduate_admission["Chance_of_Admit"]<0.4]["GRE_Score"].mean())
    print(graduate_admission[graduate_admission["Chance_of_Admit"]<0.8]["CGPA"].mean())
    print(graduate_admission[graduate_admission["Chance_of_Admit"]<0.4]["CGPA"].mean())
