#Display function to give context to user
def display():
	print("#"*30)
	print("WELCOME TO THE SEX RATIO FIXER")
	print("#"*30)
	print("Enter the number of boys and girls in your class and specify desired ratio. We shall help you out :>")
#Heart of the code. The ratio fixer
def RatioFixer(iB,iG,iN,iD):
	#Checking if ratio is already the same as no.of boys : girls
	if iB * iD == iG * iN:
		print("The class is already in required ratio !")
	#Else segregating boys : girls from total strength as per ratio
	else:
		totalStrength = iB + iG
		numDenSum = iN + iD
		iB = (iN * totalStrength)//numDenSum
		iG = totalStrength - iB
		print(f"The number of boys and girls should be approximately {iB} and {iG} respectively as per the given ratio of {iN}:{iD}")


def StrengthInput():
	try:
		#Taking input for required values
		iBoys = int(input("Enter number of boys in your class : "))
		iGirls = int(input("Enter number of girls in your class : "))
		#Ratio
		iNumerator = int(input("Enter the numerator for desired ratio of boys to girls : "))
		iDenominator = int(input("Enter the denominator for desired ratio of boys to girls : "))	
		#Just some loggers
	except Exception as e:		
		print("(-) Error was thrown :-> ",e)	
	else:		
		#Removing result as 0 or division by 0 using this simple logger
		if iBoys == 0 or iGirls == 0 or iNumerator == 0 or iDenominator == 0:			
			print("Uh huh invalid data! ")		
		else:			
			#Invoking method
			RatioFixer(iBoys,iGirls,iNumerator,iDenominator)
	finally:
		#Finishing code
		print("(-) Program has ended")


#Invoking main
def main():

	display()
	StrengthInput()
#Running code
if __name__ == '__main__':
	main()