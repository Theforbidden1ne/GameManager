import os
os.system('mkdir server/bin/client_linux')
os.system('mkdir server/bin/client_win')
os.system('cp dist/app.exe server/bin/client_win/client.exe')
os.system('cp dist/app server/bin/client_linux/client')