#Count no of vowels

String = "Hello world! How are you? Its python world here!"
Vowels = "aeiou"
count = 0
# for Vowels in String:
for letters in String:
    if letters in Vowels:
      count += 1
print(count)
