from tkinter import *
from storage_grid import StorageGrid

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile     = 'rijkszaak'
bucket      = 'prod4-demo-acc01-db-archive'

sg = StorageGrid(s3_endpoint, profile)
sg.set_max_items(20)

# sg.list_buckets()
objects = sg.list_objects(bucket)

rows = []
# i = rows
# j = cols
i = 0
for obj in objects:
    i+=1
    col0 = Entry(relief=GROOVE)
    col0.grid(row=i, column=0, sticky=NSEW)
    col0.insert(END, obj)
    rows.append([col0])
mainloop()