import re
text_1="This is a good 2 day"
def check_1():
    if re.match("good", text_1):  # match checks only the 1st string
        print("yes")
    else:
        print("no")
def check_2():
    if re.search("good", text_1):  # match checks only the 1st string
        print("yes")
    else:
        print("no")

text_2= "Amy works diligently. Amy gets good grades. Our student Amy is successful."
text_3= "works Amy diligently. Amy gets good grades. Our student Amy is successful."

def check_3():
    print(type(re.split("Amy", text_2)))
    print(re.split("Amy", text_2))
    print(re.split("Amy", text_3))
    print(re.findall("Amy", text_2))
    print(re.search("^Amy", text_2))  # check the output
    print(re.search("works", text_2))  # check the output
    print(re.search("grades.$", text_2))
    print((re.search("successful", text_2)))
    print((re.search("successful.$", text_2)))
    print((re.search("successful$", text_2)))

grades="ACAAAABCBCBAA"
def check_4():
    print(re.findall("B", grades))
    print((re.findall("AB", grades)))
    print((re.findall("[AB]", grades)))
    print((re.findall("A[B-C]", grades)))
    print((re.findall("AB|AC", grades)))  # pipe operator, "or"
    print(re.findall("[^A]", grades))
    print(re.findall("^[^A]", grades))
def check_5():
    print(re.findall("A{2,3}",grades))
    print(re.findall("A{1,1}A{1,1}", grades))  # overlapping is not considered
    print(re.findall("A{2,2}", grades))
    print(re.findall("A{2}", grades))
    print(re.findall("A{1,10}B{1,10}C{1,10}",grades))

with open(r"C:\Users\THINKPAD\Downloads\ferpa.txt") as file:
    wiki=file.read()
def check_6():
    print(re.findall("[A-Za-z]{1,100}", wiki))
    print(re.findall("[A-Za-z]", wiki))
    print(re.findall(r"[A-Za-z]{1,100}\[edit\]",wiki))      #which is print(re.findall("[A-Za-z]{1,100}\[edit\]",wiki))
    #print(re.findall("[A-Za-z]{1,100}\[edit\]", wiki))  # warning will be shown here
    print(re.findall(r"[\w]{1,100}\[edit\]", wiki))
    print(re.findall(r"[\w]*\[edit\]", wiki))
    print(re.findall(r"[\w ]*\[edit\]", wiki))
def check_7():
    for title in re.findall(r"[\w ]*\[edit\]", wiki):
        print(title)
    for title in re.findall(r"[\w ]*\[edit\]", wiki):
        print(re.split(r"[\[]", title))
    for title in re.findall(r"[\w ]*\[edit\]", wiki):
        print(re.split(r"[\[]", title)[0])
