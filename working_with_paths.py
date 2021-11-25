from pathlib import Path

# Path(r"C:\Program Files\Microsoft")  # using raw string
# Path("/usr/local/bin")
# Path()  # current directory
# Path("ecommerce/__init__.py")  # relative path
# Path() / "ecommerce" / "__init__.py"  # combining with Path
# Path.home()  # home directory

path = Path("ecommerce/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# new path object with only filename and extension changed
# address remains the same
path = path.with_name("file.txt")
print(path)
print(path.absolute)

# only change the extension of the file
path = path.with_suffix(".py")
print(path)
