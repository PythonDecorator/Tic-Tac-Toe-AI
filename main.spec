# -*- mode: python -*-
a = Analysis(['main.py'],
         pathex=['C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe'],
         datas=[('C:\\Users\\XPS\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\customtkinter', 'customtkinter/'), ('C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe\\venv\\Lib\\site-packages\\pygame', 'pygame/')],
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('files\\images\\logo.ico', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe\\files\\images\\logo.ico', 'DATA'), ('files\\sound\\bg_music.mp3', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe\\files\\sound\\bg_music.mp3', 'DATA'), ('files\\images\\o.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe\\files\\images\\o.png', 'DATA'), ('files\\images\\x.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe\\files\\images\\x.png', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='Tic-Tac-Toe.exe',
      debug=False,
      strip=None,
      upx=True,
      console=False,
      icon='C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Tic Tac Toe\\files\\images\\logo.ico')
