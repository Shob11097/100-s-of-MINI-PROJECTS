#program to extract year, month and date from an url.

import re
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
extracting = re.findall(r'\d{4}/\d{2}/\d{1,2}',url)
print(extracting)