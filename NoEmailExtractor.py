#! python3

#This is a program for number and email extraction


import re,pyperclip

phone_number = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?)''',re.VERBOSE)
email = re.compile(r'([a-zA-Z0-9.%_+]+@[a-zA-Z0-9]+(\.[a-zA-Z]{2,4}))')

text = str(pyperclip.paste())
matches = []
for groups in phone_number.findall(text):
    phonenum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phonenum+= ' x' + groups[8]
    matches.append(phonenum)
for groups in email.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('no phone number or email address found')