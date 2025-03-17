# build.spec
block_cipher = None

a = Analysis(
    ['NotAVirus.py'],  # Replace with your script name
    pathex=[],
    binaries=[],
    datas=[('NotAVideo.mp4', '.'), ('ffplay.exe', '.')],  # Bundle video + ffplay
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GTA VI',  # Name your .exe
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to `False` to hide the console
    icon='favicon.ico',  # Optional: add an icon
)