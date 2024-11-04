'''
在一篇很长文章或者网页中找出所有电话号码和邮件地址
'''

'''
程序框架
#TODO:Create phone regex

#TODO:Create email regex

#TODO:Find matches in clipboard text.

#TODO:Copy result to the clipboard.
'''
import pyperclip
import re

# Create phone regex
phone_regex = re.compile(r'''
    (
        (\d{3}|\(\d{3}\))?                  # area code (optional)
        (\s|-|\.)?                          # separator
        (\d{3})                             # first 3 digits
        (\s|-|\.)?                          # separator
        (\d{4})                             # last 4 digits
        (\s*(ext|x|ext\.)\s*(\d{2,5}))?     # extension (optional)
    )
''', re.VERBOSE)

# Create email regex
email_regex = re.compile(r'''
    (
        #在字符类（[...]）内部时，.不会被解释为“匹配任意字符”
        [a-zA-Z0-9._%+-]+            # username
        @                            # @ symbol
        [a-z A-Z0-9.-]+              # domain name
        (\.[a-zA-Z]{2,})             # dot-something 
    )
''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[7] != '':
        phone_num += ' x' + groups[7]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy result to the clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email address found')
