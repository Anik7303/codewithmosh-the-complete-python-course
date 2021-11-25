import json
from pathlib import Path

# Writing json data to a file
# try:
#     products = [
#         {'name': 'one', 'no': 1, 'count': 67},
#         {'name': 'two', 'no': 2, 'count': 7}
#     ]
#     data = json.dumps(products)
#     Path('data.json').write_text(data)
# except Exception as e:
#     print(e)

# Reading json data from a file
try:
    data = Path('data.json').read_text()
    products = json.loads(data)
    print(products)

except Exception as e:
    print(e)
