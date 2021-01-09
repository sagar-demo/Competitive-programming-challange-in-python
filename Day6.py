f=int(input("Enter Fee disk size in bytes.."))
u=int(input("Enter Used disk size in bytes.."))
o=int(input("Enter old file size in bytes.."))
n=int(input("Enter new file size in bytes.."))

totalDiskSize=f+u
currentUseDeskSize=u-o
currentUseDeskSize=currentUseDeskSize+n
currentUseDeskSize=totalDiskSize-currentUseDeskSize
print("Free space Available ",currentUseDeskSize,"Bytes")
