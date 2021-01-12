# 5 th graders kara and rani both have lemonade stands.kara sells her lemonade at 5 cents a glass and Rani sells her at 7 cents a glass.Kara sold k number of glasses of lemonade today and Rani sold r number of glasses .who made the most money and by what amount? K and r are user entered value.
KaraGlassCount=int(input("Enter Kara's glass count"))
raniGlassCount=int(input("Enter Rani's glass count"))

KaraGlassRate=5
raniGlassRate=7

KaraTotalMoney=KaraGlassCount*KaraGlassRate
raniTotalMoney=raniGlassCount*raniGlassRate

if KaraTotalMoney>raniTotalMoney:
    print("Kara :",KaraTotalMoney,"Cents")
elif KaraTotalMoney<raniTotalMoney:
    print("Rani :",raniTotalMoney,"Cents")
elif KaraTotalMoney==raniTotalMoney:
    print("Kara and Rani's money is equal")