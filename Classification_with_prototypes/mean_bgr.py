import os
import cv2
myfile=open("list.txt","r")
li1=myfile.readlines()
li=eval(li1[0])
myfile.close()
myfile=open("aveaccu.txt","a")
# print(li[0][1])
allt=0
allr=0
path="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Test"
categories=os.listdir(path)
for category in categories:
    cpath="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Test//"+category
    cimages=os.listdir(cpath)
    cc=0
    tc=0
    for image in cimages:
        img=cv2.imread("D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Test//"+category+"//"+image)
        c=0
        blue=0
        green=0
        red=0
        for i in range(100):
            for j in range(100):
                li2=img[i][j]
                if (li2[0]==255 and li2[1]==255 and li2[2]==255):
                    pass
                else:
                    blue+=li2[0]
                    green+=li2[1]
                    red+=li2[2]
                    c+=1
        blue=round(blue/c)
        green=round(green/c)
        red=round(red/c)
        le=len(li)
        dli=[]
        for i in range(le):
            b=li[i][0]
            g=li[i][1]
            r=li[i][2]
            dist=((blue-b)**(2)+(green-g)**(2)+(red-r)**(2))**(0.5)
            dli.append([dist,li[i][3]])
        dli.sort()
        if dli[0][1]==category:
            cc+=1
            allr+=1
        tc+=1
        allt+=1
    ans=(cc/tc)*100
    print("Accuracy of "+category+" is "+str(ans))
    myfile.write("Accuracy of "+category+" is "+str(ans)+"\n")
finalans=(allr/allt)*100
print("Overall Accuracy is "+str(finalans))
myfile.write("Overall Accuracy is "+str(finalans))