'''
sys读取输入参数
如果sys.arg为1则只有一个参数即python string_project.py，则返回这个脚本的用法
如果为2即 python string email，即运行脚本带上要复制的账户
再进入判断，如果账户存在就调用pyperclip把密码复制到剪切板，
账户不存在便打印不存在信息
'''
PASSWORDS={
    'email':'fjisdfjiffjoadsoj',
    'blog':'ffjjfjsaiee455',
    'luggage':'7887458',
}

import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: py string_project.py [account] - copy account password')
    sys.exit()
account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+'copied to clipboard.')
else:
    print('There is no account named '+account)