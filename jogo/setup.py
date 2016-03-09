import cx_Freeze

executables = [cx_Freeze.Executable("main2.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["bg.png"]}},
    executables = executables

    )

