import argparse #take user IMEI

parser = argparse.ArgumentParser(description='IMEI Luhn digit calculator.') #-h description
parser.add_argument("IMEI", help="Calculate luhn digit for this IMEI.", type=int) #madnatory argument IMEI
parser.add_argument("--raw", help="Print IMEI only", action="store_true") #good for scripts
parser.add_argument("--allrbi", help="Use all known Reported Body Identificators", action="store_true") #remove 35-86 lock
args = parser.parse_args() #obvious
IMEI=args.IMEI #I did this script on a phone srry
RBIList=[0,1,2,3,4,5,6,7,8,9,10,30,33,35,44,45,49,50,51,52,53,54,86,91,98,99] #List of all allowed RBIs, please do not edit to avoid invalid IMEIs
if not len(str(IMEI))==14: #make sure we arent doing dumb shit
	print("Invalid IMEI length!")
if args.allrbi==False:
	if IMEI//1000000000000==35 or IMEI//1000000000000==86: #please excuse my janky number calc, it works okay
		sum1=(IMEI//10000000000000)+(IMEI//100000000000%10)+(IMEI//1000000000%10)+(IMEI//10000000%10)+(IMEI//100000%10)+(IMEI//1000%10)+(IMEI//10%10)
		s2n1=(IMEI//1000000000000%10)*2
		if s2n1//10==1:
			s2n1=(s2n1//10)+(s2n1%10)
		s2n2=(IMEI//10000000000%10)*2
		if s2n2//10==1:
			s2n2=(s2n2//10)+(s2n2%10)
		s2n3=(IMEI//100000000%10)*2
		if s2n3//10==1:
			s2n3=(s2n3//10)+(s2n3%10)
		s2n4=(IMEI//1000000%10)*2
		if s2n4//10==1:
			s2n4=(s2n4//10)+(s2n4%10)
		s2n5=(IMEI//10000%10)*2
		if s2n5//10==1:
			s2n5=(s2n5//10)+(s2n5%10)
		s2n6=(IMEI//100%10)*2
		if s2n6//10==1:
			s2n6=(s2n6//10)+(s2n6%10)
		s2n7=(IMEI//1%10)*2
		if s2n7//10==1:
			s2n7=(s2n7//10)+(s2n7%10)
		sum2=s2n1+s2n2+s2n3+s2n4+s2n5+s2n6+s2n7
		luhn=10-((sum1+sum2)%10)
		if args.raw==True:
			print(IMEI,10-(sum1+sum2)%10,sep="")
		else:
			print("Output IMEI with Luhn digit: ",IMEI,luhn,sep="")
	else:
		print("RBI is invalid! Run with --allrbi to allow unusual RBIs.")
else:
	if IMEI//1000000000000==RBIList[0] or IMEI//1000000000000==RBIList[1] or IMEI//1000000000000==RBIList[2] or IMEI//1000000000000==RBIList[3] or IMEI//1000000000000==RBIList[4] or IMEI//1000000000000==RBIList[5] or IMEI//1000000000000==RBIList[6] or IMEI//1000000000000==RBIList[7] or IMEI//1000000000000==RBIList[8] or IMEI//1000000000000==RBIList[9] or IMEI//1000000000000==RBIList[10] or IMEI//1000000000000==RBIList[11] or IMEI//1000000000000==RBIList[12] or IMEI//1000000000000==RBIList[13] or IMEI//1000000000000==RBIList[14] or IMEI//1000000000000==RBIList[15] or IMEI//1000000000000==RBIList[16] or IMEI//1000000000000==RBIList[17] or IMEI//1000000000000==RBIList[18] or IMEI//1000000000000==RBIList[19] or IMEI//1000000000000==RBIList[20] or IMEI//1000000000000==RBIList[21] or IMEI//1000000000000==RBIList[22] or IMEI//1000000000000==RBIList[23] or IMEI//1000000000000==RBIList[24] or IMEI//1000000000000==RBIList[25]: #GUYS IM THE BEST CODER ALIVE
		sum1=(IMEI//10000000000000)+(IMEI//100000000000%10)+(IMEI//1000000000%10)+(IMEI//10000000%10)+(IMEI//100000%10)+(IMEI//1000%10)+(IMEI//10%10) #please excuse my janky number calc, it works okay
		s2n1=(IMEI//1000000000000%10)*2
		if s2n1//10==1:
			s2n1=(s2n1//10)+(s2n1%10)
		s2n2=(IMEI//10000000000%10)*2
		if s2n2//10==1:
			s2n2=(s2n2//10)+(s2n2%10)
		s2n3=(IMEI//100000000%10)*2
		if s2n3//10==1:
			s2n3=(s2n3//10)+(s2n3%10)
		s2n4=(IMEI//1000000%10)*2
		if s2n4//10==1:
			s2n4=(s2n4//10)+(s2n4%10)
		s2n5=(IMEI//10000%10)*2
		if s2n5//10==1:
			s2n5=(s2n5//10)+(s2n5%10)
		s2n6=(IMEI//100%10)*2
		if s2n6//10==1:
			s2n6=(s2n6//10)+(s2n6%10)
		s2n7=(IMEI//1%10)*2
		if s2n7//10==1:
			s2n7=(s2n7//10)+(s2n7%10)
		sum2=s2n1+s2n2+s2n3+s2n4+s2n5+s2n6+s2n7
		luhn=10-((sum1+sum2)%10)
		if args.raw==True:
			print(IMEI,10-(sum1+sum2)%10,sep="")
		else:
			print("Output IMEI with Luhn digit: ",IMEI,luhn,sep="")
	else:
		print("RBI is invalid!")