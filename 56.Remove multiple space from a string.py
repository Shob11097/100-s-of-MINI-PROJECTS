#To remove multiple space from a string!

import re
text = "Python      exercises  are good   to   practise "
space = re.sub(" +"," ",text)
print(space)