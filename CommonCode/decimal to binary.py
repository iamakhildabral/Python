####### Decimal to binary coversion ##########

decimal_no = int(input("Enter the decimal numebr to convert it into binary:"))

binary = ''

if decimal_no > 1:
       while decimal_no > 1:
              binary = binary + str(decimal_no%2)
              decimal_no = decimal_no // 2
       binary = binary + str(decimal_no)
       binary = binary[::-1]
       print("the binary form of your decimal number is :"+binary)
else:
       print("The binary equivalent is :"+str(decimal_no))
