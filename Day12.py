# the number of red blood corpuscles in one the cubic millimetre is about 5,000,000 and the number of while blood corpuscles in one cubic
# the millimeter is about 8,000 .what is the ratio blood corpuscles to red blood corpuscles?
#Aspect Ratio should be as an int value
def greatestCommonFactor(whiteC,redC):
    return whiteC if(redC==0) else greatestCommonFactor(redC,whiteC%redC)
redCorpuscles=5000000
whiteCorpuscles=8000
factor=greatestCommonFactor(whiteCorpuscles,redCorpuscles)
whiteRatio=int(whiteCorpuscles/factor)
redRatio=int(redCorpuscles/factor)
print("Aspect Ratio ",whiteRatio,":",redRatio)