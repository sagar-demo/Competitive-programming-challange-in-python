sweaterPrice=68
sweaterCount=3
computerGamePrice=75
computerGameCount=1
braceletPrice=43
braceletCount=2

#discount And Rebate
returnedBraceletCount=1
rebateOnComputerGame=10


# calculation part
totalGiftPrice=(sweaterPrice*sweaterCount)+(computerGamePrice*computerGameCount)+(braceletPrice*braceletCount)

discountAndRebate=(braceletPrice*returnedBraceletCount)+rebateOnComputerGame

finalGiftPrice=totalGiftPrice-discountAndRebate
print("Final gift is ",finalGiftPrice)

