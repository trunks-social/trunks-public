from os import listdir
from os.path import isfile, join
import json

onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
for file in onlyfiles:
    if file != "app_en.arb" and file != "untranslated.txt" and file != "README.md" and file != "cleanup.py":
       with open(file) as f:
           fileJson = json.load(f)
           copy = fileJson.copy()
           for key, value in fileJson.items():
              if key.startswith("@"):
                del copy[key]
           with open(file, 'w') as newfile:
               json.dump(copy, newfile, ensure_ascii=False, indent=4)
