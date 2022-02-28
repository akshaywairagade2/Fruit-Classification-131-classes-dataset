import os
import cv2 as cv
file=open("list1.txt","r")
lis=file.readline()
lis=eval(lis)
print(len(lis))
path='D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Training'
fruits=os.listdir(path)
cons=0
tc=0
cc=0
y=0
finans=[]
for category in fruits:
    fruitt=0
    fruitc=0
    imagepath='D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Training//'+category
    infruits=os.listdir(imagepath)
    print(str(cons)+' '+category)
    catli=category.split()
    cate=category[:5]
    cate=cate.lower()
    # print(catli)
    for image in infruits:
        img=cv.imread("D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Training//"+category+"//"+image)
        c=0
        blue=0
        green=0
        red=0
        for i in range(100):
            for j in range(100):
                li=img[i][j]
                if (li[0]==255 and li[1]==255 and li[2]==255):
                    pass
                else:
                    blue+=li[0]
                    green+=li[1]
                    red+=li[2]
                    c+=1
        blue=round(blue/c)
        green=round(green/c)
        red=round(red/c)
        # print(blue,green,red)
        ansli=[]
        for i in range(len(lis)):
            li=lis[i]
            dist=((li[0]-blue)**2+(li[1]-green)**2+(li[0]-red)**2)**(0.5)
            ansli.append([dist,li[4]])
        ansli.sort()
        fr=ansli[0][1]
        fr=fr[0:5].lower()
        # print(fr,cate)
        if fr==cate:
            # print(ansli[0][1],category)
            cc+=1
            fruitc+=1
        if y==0:
            # print(ansli[i][1],category)
            y=1
        tc+=1
        fruitt+=1 
        acc=(fruitc/fruitt)*100
    print(category+" is "+str(acc))
    finans.append(category+" is "+str(acc))
    
print((cc/tc)*100)





