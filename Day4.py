## jack bought 400 hot dogs for the school picnic.if they were contained in package of 8 hot dogs
#how many total package did he buy? create a python without using or % operator
totalHotDog=400
totalHotDogPerContainer=8
totalContainer=0
while (totalHotDog>=totalContainer):
    totalHotDog-=totalHotDogPerContainer
    totalContainer+=1
    print("jack buy total ",totalContainer,"container")