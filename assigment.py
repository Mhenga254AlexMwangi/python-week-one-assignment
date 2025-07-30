number1= int(input('Enter first number : '))
number2= int(input ('Enter second number : '))
operation= str(input('Enter operation : '))
if operation =="+":
 print('your answer is :',(number1+number2))
elif operation== "-":
 print('your answer is :',(number1-number2))
elif operation== "*":
 print('your answer is :',(number1*number2))
elif operation == "/":
 print ('your answer is :',(number1/number2))
else :
 print('Enter the correct operation')