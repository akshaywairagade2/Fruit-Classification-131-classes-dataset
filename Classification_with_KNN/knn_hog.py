import os
import cv2

#Training the dataset with (1/10)th of total images per folder of the category
path="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Training"
categories=os.listdir(path)

#Storing the category name and it's histogram
histdict=dict()
for category in categories:
    cpath="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Training//"+category
    cimages=os.listdir(cpath)

    #used num to have different key names as they may overlap if they have same key
    num=0
    le=len(cimages)
    for i in range(0,le,10):
        image=cimages[i]
        impath="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Training//"+category+"//"+image
        img=cv2.imread(impath)

        #working on the hog feature
        hist=cv2.calcHist([img],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
        hist=cv2.normalize(hist,hist).flatten()
        if num<10:
            histdict[category+'0'+str(num)]=hist
        else:
            histdict[category+str(num)]=hist
        num+=1

#Testing
#Test done on total test dataset


#stored my data in this file
myfile=open("nhog.txt","a")
allt=0
allr=0
path="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Test"
categories=os.listdir(path)
for category in categories:
    cpath="D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Test//"+category
    cimages=os.listdir(cpath)
    c=0
    t=0
    for image in cimages:
        img=cv2.imread("D://Semester4//Data Analytics and Visualization//Assignment1b//fruits-360_dataset//fruits-360//Test//"+category+"//"+image)
        hist=cv2.calcHist([img],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
        hist=cv2.normalize(hist,hist).flatten()
        li=[]

        #calculated the distances between the test histogram and trained data histograms
        for fruit in histdict:
            histfr=histdict[fruit]
            d3=cv2.compareHist(hist,histfr,cv2.HISTCMP_BHATTACHARYYA)
            name=fruit

            #did fruit[:-2] because earlier we used two digit num so to remove that we used this
            li.append([d3,fruit[:-2]])
        
        #The lower the distance more it is similar
        li.sort()

        #di and li used for calculating the majority of fruits which are in top 10 nearest neighbours
        di=dict()
        #Here K is used as 10 for calculating the k-nearest neighbours
        for i in range(10):
            if li[i][1] in di:
                di[li[i][1]]+=1
            else:
                di[li[i][1]]=1
        nli=[]
        for i in di:
            nli.append([di[i],i])
        
        #The greater the neighbour points the more it has chance of category match
        nli.sort(reverse=True)
        if nli[0][1]==category:
            c+=1
            allr+=1
        t+=1
        allt+=1
    print(c,t)

    #Calculated category wise accuracy
    ans=(c/t)*100
    print(ans)
    myfile.write("Accuracy for "+category+" is "+str(ans)+"\n")

#calculated overall accuracy
fans=(allr/allt)*100
print(fans)
myfile.write("Total Accuracy obtained is "+str(fans))

# Total Accuracy obtained is 96.47390691114246