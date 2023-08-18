import sys
import pyperclip
password = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}
                                                                                                    
if len(sys.argv)<2:
    print('format: password_locker[account]')
    sys.exit()


account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('password for'+account+'copied in clipboard')
else:
    print('there is no command named'+account)