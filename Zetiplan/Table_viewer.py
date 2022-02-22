
import csv
def Get_DET(position):
    fulllist=[]
    for i in ['CSE_TT.csv','ECE_TT.csv','EEE_TT.csv','Civil_TT.csv','Mech_TT.csv']:
        fileobject=open(i,'r')
        data=csv.reader(fileobject)

        templist=[]
        for j in data:
            if j!=[]:
                templist.append(j)

        fulllist.append(templist)



    teachlist=[]

    fileobject=open('Teachers_list.csv','r')
    data=csv.reader(fileobject)
    print(data)

    

    for j in data:
        templist=[]
        if j!=[]:
            for i in j:
                print(i)
                templist.append(eval(i)[0])

            print()

            teachlist.append(templist)



    deptnames=['CSE Time Table','ECE Time Table','EEE Time Table','Civil Time Table','Mech Time Table']
    return [fulllist[position],teachlist[position],deptnames[position],position]


