#During the last week of track training,
#Shoshanna achives the following time in sec-rounds:66,57,54,53,64,52, and 59 Found her best score use bubble sort
seconds=[66,57,54,53,64,52,59]
n=len(seconds)
for i in range(n):
    for j in range(0,n-i-1):
        if seconds[j]>seconds[j+1]:
            seconds[j],seconds[j+1]=seconds[j+1],seconds[j]
print("Her best time is",seconds[0],"seconds")
