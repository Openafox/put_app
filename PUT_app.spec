# -*- mode: python -*-

block_cipher = None

# http://stackoverflow.com/questions/8870887/build-images-and-some-configuration-files-like-txt-and-xml-files-with-pyinstalle
# https://pythonhosted.org/PyInstaller/#the-tree-class

dict_tree = Tree('.\\img', prefix = 'img')
dict_tree += Tree('.\\data', prefix = 'data')
print 'dict_tree =', dict_tree


a = Analysis(['PUT_app.py', 'PUT_Gui.py', 'WinShorts.py', 'Pass.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=['.\\hooks'],
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
# a.datas += [('Pass.txt', 'Pass.txt', 'DATA')]
a.datas += dict_tree
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          # [('v', None, 'OPTION'),('W ignore', None, 'OPTION')], #Make Python Verbose
          exclude_binaries=True,
          name='PUT_app.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='oafox_programs')
