'''
pyperclip来将剪切板上面文字每一行加一个星号以及空格
然后在复制到剪切板上面
'''
import pyperclip
text=pyperclip.paste()
print(text)
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)