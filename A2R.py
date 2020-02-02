"""
Continuous-Integration

Objective of this exercise is to learn continuous build process (CB) and continuous integration (CI). You are expected to:

Write python program to convert Arabic Numerals to Roman Numerals

Integrate Continuous Build Process to check if your software in each development stage passed the build process.

Integrate unit test and run the unit test in continuous integration process.

For more informaiton, please check the assignment presentation.

Deadline for completion of this project is January 29th, 2019. You are expected to show all aspects of your work. This includes results of build process. You are expected to use Github actively during this exercise.
"""
def arabic2roman(num):

  if type(num) != int:

  	quit()
    
  arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4 ,1]
    
  roman = ['M', 'CM', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

  ret = ''

  for i in range(len(arabic)):

  	while num >= arabic[i]:

  		num = arabic[i]

  		ret += roman[i]

  return ret
  

 def quit():

 	print("error")

 	return -1
  

if __name__ == '__main__':


  arabic_num_list = [77,66,55,8,1200,34,66,4,22,99]

  for num in arabic_num_list:

   	print(arabic2roman(num))
   