import os


subdirs =[
    'artifacts',
    'research',
    'models',
    'src',
    'src/components'
]

for subdir in subdirs:
    dirpath = os.path.join(os.getcwd(),subdir)
    os.makedirs(dirpath,exist_ok=True)