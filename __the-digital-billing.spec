# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['__the-digital-billing.py'],
             pathex=['C:\\Users\\Sanchit Baweja\\Desktop\\THE DIGITAL BILLING\\manage products\\_v2_THE DIGITAL BILLING\\TDB\\TDB-IP PROJECT-GROUP NO 3-2020-21'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='__the-digital-billing',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
