import tkinter as tk
import tksheet



from storage_grid import StorageGrid

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile     = 'rijkszaak'
bucket      = 'sbx4-bas-deletion-test-bucket'

sg = StorageGrid(s3_endpoint, profile)
sg.set_max_items(100)

# sg.list_buckets()
objects = [' '] #sg.list_objects(bucket)

def single_select(event):
    # print(event)
    # print(event['selected'].row)
    # print(event['selected'].column)
    cell_value = sheet.get_cell_data(event['selected'].row, event['selected'].column)
    print(cell_value)

def button_clicked():
    sg.set_max_items(int(num_items_input.get("1.0", 'end-1c')))
    objects = sg.list_objects(bucket)
    num_items.configure(text="Number of objects: " + str(len(objects)))
    sheet.set_sheet_data(objects)
    sheet.set_all_column_widths(600)
    #sheet.column_width(column=0, width=400, redraw=True)
    # sheet.column_width(column=0, width=600)
    # sheet.height_and_width(900)
    # sheet.pack(fill=tk.BOTH, expand=True)
    #print("Button clicked!")

top = tk.Tk()

btn_frame= tk.Frame(top)

num_items_input = tk.Text(btn_frame,
                    height=1,
                    width=20)
num_items_input.grid(row=0, column=0, padx=10, pady=10)

btn_frame.grid(row=0, column=0 ,sticky=tk.EW)
button = tk.Button(btn_frame, 
                   text="Get objects from bucket", 
                   command=button_clicked,
                  )
button.grid(row=0, column=1, padx=10, pady=10)

num_items = tk.Label(btn_frame, text="Number of objects found: " + str(len(objects)))
num_items.grid(row=0, column=2)


sheet_frame = tk.LabelFrame(top, text="items in bucket", padx=5, pady=5)
sheet_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.NSEW)
sheet_frame.rowconfigure(0, weight=1)
sheet_frame.columnconfigure(0, weight=1)
sheet = tksheet.Sheet(sheet_frame)
sheet.grid(row=1, column=0, columnspan=3, padx = 10, pady = 10, sticky=tk.NSEW)
sheet.pack(fill=tk.BOTH, expand=True)
# print([[f"{ri+cj}" for cj in range(4)] for ri in range(2)])
sheet.set_sheet_data(objects)
# table enable choices listed below:
sheet.enable_bindings(("single_select",
                       "row_select",
                       "column_width_resize",
                       "arrowkeys",
                       "right_click_popup_menu",
                       "rc_select",
                       "rc_insert_row",
                       "rc_delete_row",
                       "copy",
                       "cut",
                       "paste",
                       "delete",
                       "undo",
                       "edit_cell"))
sheet.column_width(column=0, width=600)
sheet.height_and_width(900)

sheet.extra_bindings("cell_select", single_select)

top.title("StorageGrid objects")

top.columnconfigure(0, weight=1)
top.rowconfigure(1, weight=1)

top.geometry('800x800')
top.mainloop()