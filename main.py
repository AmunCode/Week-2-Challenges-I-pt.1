print('Hi everyone, please enter your grade number to find out what letter grade you received. \n')

mar=int(input('Enter your grade here:'))
if mar>=90:
  print('You have received a A')
elif mar>=80 and mar<90:
  print('You have received a B')
elif mar>=70 and mar<80:
  print('You have received a C')
elif mar>=70 and mar<60:
  print('You have received a D')
elif mar<=60:
  print('You have received a F')
  
# check code for what happends if I score a 65.
