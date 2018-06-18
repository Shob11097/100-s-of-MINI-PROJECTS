#Python program to replace whitespaces with an underscore and vice versa

text = 'Python Exercises Paragraphs are commonly numbered using the decimal system, where (in books) the ' \
       'integral part of the decimal represents the number of the chapter and the fractional parts are arranged ' \
       'in each chapter in order of magnitude. Thus in Whittaker and Watson'

underscore = text.replace(' ', '_')
print(underscore)