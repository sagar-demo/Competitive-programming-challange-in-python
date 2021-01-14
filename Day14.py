# How many ways can your student Ram Anju Deepak and Ravi line up  in  a line.if the order matters?
# Print all possible combination
def PrintAllCombination(sArray):
    if len(sArray)==0:
        return []
    if len(sArray)==1:
        return [sArray]
    l=[]
    for i in  range(len(sArray)):
        m=sArray[i]
        remLst=sArray[:i]+sArray[i+1:]
        for p in PrintAllCombination(remLst):
            l.append([m]+p)
    return l


studentArray=["Ram","Anju","Deepak","Ravi"]
for combination in PrintAllCombination(studentArray):
    print(combination)