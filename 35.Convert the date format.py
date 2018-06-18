#Convert the date format

import re

date = "2012-04-01"

date_format = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1',date)
print(date_format)