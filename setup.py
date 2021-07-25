import cx_Freeze

executables = [cx_Freeze.Executable('dinogame.py')]

cx_Freeze.setup(
    name="Dino Game",
    options={'build_exe': {'packages': ['pygame'],
                            'include_files':['imagens', 'sons']}},

    executables = executables

)