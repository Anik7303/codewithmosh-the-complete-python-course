from pathlib import Path
from time import ctime
import shutil

path = Path(r"ecommerce/__init__.py")
# path = Path(r"__init__.txt")
# print(path.exists())
# path.rename("__init__.txt")
# path.unlink()

# fstat = path.stat()
# print(fstat)
# print(f"Last Accessed At: {ctime(fstat.st_atime)}")
# print(f"Created At: {ctime(fstat.st_ctime)}")
# print(f"Modified At: {ctime(fstat.st_mtime)}")

# print(path.read_bytes())
# print(path.read_text())
# path.write_bytes()
# path.write_text("...")

# copy file using Path
source = Path(r"ecommerce/__init__.py")
target = Path(r"ecommerce/__init__.txt")
# target.write_bytes(source.read_bytes())

# copy file using shutil
# shutil.copy(source, target)
