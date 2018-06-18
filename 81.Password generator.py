#Passwordd generator

import random
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\|,<>./?#~'@;:}][{=+-_)(*&^%$£!1234567890"
password_len = 8
p = "".join(random.sample(s,password_len))
print(p)