# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\ASUS\\AppData\\Local\\Temp\\COTP-runtime-probe-c755ef46d8704ebeaf349a832f4549d1\\probe.py'],
    pathex=['F:\\PC MEDIA\\developer_skills\\AI developer\\prompt and custom\\tool\\random\\COTP'],
    binaries=[],
    datas=[('F:\\PC MEDIA\\developer_skills\\AI developer\\prompt and custom\\tool\\random\\COTP\\data', 'data'), ('F:\\PC MEDIA\\developer_skills\\AI developer\\prompt and custom\\tool\\random\\COTP\\Script', 'Script')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cotp-info-probe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
