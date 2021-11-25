from pathlib import Path, WindowsPath

try:
    path = Path(r"ecommerce")
    # path = Path(r"ecommerce/working_with_directories")
    # print(f"{path.absolute()} exists: {path.exists()}")
    # path.mkdir()
    # print(f"{path.absolute()} exists: {path.exists()}")
    # path.rmdir()
    # print(f"{path.absolute()} exists: {path.exists()}")
    # path.rename("directory")
    # print(f"{path.absolute()} exists: {path.exists()}")

    # path.iterdir()
    # for p in path.iterdir():
    #     print(p)
    # PosixPath for unix systems and WindowsPath for windows systems
    # print([p for p in path.iterdir()])
    # print([p for p in path.iterdir() if p.is_file()])
    # print([p for p in path.iterdir() if p.is_dir()])
    # print([p for p in path.glob("*.*")])  # this takes a pattern to search
    # print([p for p in path.glob("*.py")])  # list all .py file in the current directory
    # searches recursively
    print([p for p in path.glob("**/*.py")])
    # or
    print([p for p in path.rglob("*.py")])
except Exception as e:
    print(e)
