from pathlib import Path
from zipfile import ZipFile

# Writing to a zip file
# try:
#     zip = ZipFile("files.zip", "w")
#     for p in Path("ecommerce").rglob("*.*"):
#         print(p)
#         zip.write(p)
# except Exception as e:
#     print(e)
# finally:
#     zip.close()

# try:
#     with ZipFile("files.zip", "w") as zip:
#         for file in Path('ecommerce').rglob('*.*'):
#             zip.write(file)
# except Exception as e:
#     print(e)

# Reading from a zip file
try:
    with ZipFile("files.zip") as zip:
        files = zip.namelist()
        print(files)
        for file in files:
            info = zip.getinfo(file)
            print(info, info.filename, info.file_size,
                  info.compress_size, info.compress_type)
        zip.extractall("extracted")
except Exception as e:
    print(e)
