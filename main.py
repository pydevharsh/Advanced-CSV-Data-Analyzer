# import Important Libraries :
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import logic



# === Window Create === 
window = tk.Tk()
window.state("zoomed")
window.resizable(False, False)
window.config(bg="#0f172a")
window.title("IBM DA : L1 - P1 - Data Viewer")



# === Window Column Configuration ===
window.grid_columnconfigure(0, weight=3)  # table zyada space lega
window.grid_columnconfigure(1, weight=1)  # insights fix rahega



# === Window Row Configuration ===
window.grid_rowconfigure(1,weight=1)



# === Header Section ===

# ```Header Frame```
header_frame = tk.Frame(
    window,
    bg="#1e293b",
    bd=5,
    relief="flat"
)
header_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=0)
header_frame.grid_columnconfigure(2, weight=0)
header_frame.grid_columnconfigure(3, weight=0)

# ```Header Title```
header_title_label = tk.Label(
    header_frame,
    bg="#1e293b",
    fg="#c7c7c8",
    text="CSV Data Viewer",
    font=("Courier", 15, "bold")
)
header_title_label.grid(row=0, column=0, ipady=10, padx=10,sticky="w")

# ```Header Open CSV Button```
header_open_csv_button = tk.Button(
    header_frame,
    bg="#344B73",
    fg="#f8fafc",
    text="Open CSV",
    font=("Courier", 14, "bold"),
    width=15,
    bd=1,
    relief="solid"

)
header_open_csv_button.grid(row=0, column=1, padx=10, sticky="e")
header_open_csv_button.config(
    command=lambda: logic.open_csv(tree, footer_status_label)
)

# ```Header Refresh DATA Button```
header_refresh_data_button = tk.Button(
    header_frame,
    bg="#295048",
    fg="#f8fafc",
    text="Refresh DATA",
    font=("Courier", 14, "bold"),
    width=15,
    bd=1,
    relief="solid"
)
header_refresh_data_button.grid(row=0, column=2, padx=10, sticky="e")
header_refresh_data_button.config(
    command=lambda: logic.refresh_data(tree)
)

# ```Header Exit Button```
header_Exit_button = tk.Button(
    header_frame,
    bg="#934343",
    fg="#f8fafc",
    text="Exit",
    font=("Courier", 14, "bold"),
    width=15,
    bd=1,
    relief="solid"
)
header_Exit_button.grid(row=0, column=3, padx=10, sticky="e")
header_Exit_button.config(
    command=lambda: logic.exit_app(window)
)



# === Data Table Section ===

# ```Data Table Frame```
data_Table_frame = tk.Frame(
    window,
    bg="#1e293b",
    bd=5,
    relief="flat",
    width=450,
)
data_Table_frame.grid(row=1, column=0,padx=5, pady=5, sticky="nsew")
data_Table_frame.grid_columnconfigure(0, weight=1)
# data_Table_frame.grid_propagate(False)

# --- CRITICAL STEP: Row 3 ko expand karne ke liye ---
data_Table_frame.grid_rowconfigure(3, weight=1)

# ```Data Table Title```
data_Table_title_label = tk.Label(
    data_Table_frame,
    bg="#1e293b",
    fg="#c7c7c8",
    text="DATA Table",
    font=("Courier", 15, "bold")
)
data_Table_title_label.grid(row=0, column=0, pady=10, padx=10,sticky="ew")

# ```Horizontal Line```
hr_line = tk.Frame(data_Table_frame, bg="gray", height=2, bd=0)
hr_line.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=12)

# ```Data Table Tree View Coming soon Frame```
data_tree_view_cs_frame = tk.Frame(
    data_Table_frame,
    bg="#0a2134",
    bd=1,
    relief="solid"
)
data_tree_view_cs_frame.grid(row=3, column=0, padx=5, pady=7, sticky="nsew")
data_tree_view_cs_frame.grid_columnconfigure(0, weight=1)
data_tree_view_cs_frame.grid_rowconfigure(0, weight=1)
data_tree_view_cs_frame.grid_propagate(False)

# ---Create tree View In Data Tabel Section ---

# ```Create Tree View```
tree = ttk.Treeview(data_tree_view_cs_frame)
tree.grid(row=0, column=0, sticky="nsew")

# ```Defining Columns```
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")

# ```Headings ON```
tree["show"] = "headings"

# ```Set Columns Name```
tree.heading("col1", text="Column 1")
tree.heading("col2", text="Column 2")
tree.heading("col3", text="Column 3")
tree.heading("col4", text="Column 4")
tree.heading("col5", text="Column 5")
tree.heading("col6", text="Column 6")

# ```Width Set```
tree.column("col1", width=130, stretch=False)
tree.column("col2", width=130, stretch=False)
tree.column("col3", width=130, stretch=False)
tree.column("col4", width=130, stretch=False)
tree.column("col5", width=130, stretch=False)
tree.column("col6", width=130, stretch=False)

# ```Horizontal Scroll```
scroll_x = ttk.Scrollbar(data_tree_view_cs_frame, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=scroll_x.set)
scroll_x.grid(row=1, column=0, sticky="ew")

# tree = ttk.Treeview(data_tree_view_cs_frame)
tree.grid(row=0, column=0, sticky="nsew")

tree.bind("<Button-1>", lambda event: logic.select_column(event, tree))



# === Data Insights Section ===

# ```Data Insights Frame```
data_insights_frame = tk.Frame(
    window,
    bg="#1e293b",
    bd=5,
    relief="flat"
)
data_insights_frame.grid(row=1, column=1,padx=5, pady=7, sticky="nsew")
data_insights_frame.grid_columnconfigure(0, weight=1)
data_insights_frame.grid_columnconfigure(1, weight=1)
data_insights_frame.config(width=500)
data_insights_frame.grid_propagate(False)


# ```Data Insinsights Title```
data_insights_title_label = tk.Label(
    data_insights_frame,
    bg="#1e293b",
    fg="#c7c7c8",
    text="DATA Insights",
    font=("Courier", 15, "bold")
)
data_insights_title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10,sticky="ew")


# ```Horizontal Line```
hr_line = tk.Frame(data_insights_frame, bg="gray", height=2, bd=0)
hr_line.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=12)


# --- Data Insights Card 1 Frame ---
data_insights_card_1_frame = tk.Frame(
    data_insights_frame,
    bg="#0a2134",
    bd=1,
    relief="solid"
)
data_insights_card_1_frame.grid(row=3, column=0,padx=5, pady=7, sticky="ew")
data_insights_card_1_frame.grid_columnconfigure(0, weight=1)

# ```Data Insinsights Card 1 Title Label```
data_insights_card_1_title_label = tk.Label(
    data_insights_card_1_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    text="File Overview",
    font=("Courier", 14, "bold")
)
data_insights_card_1_title_label.grid(row=1, column=0, pady=15, padx=20,sticky="w")


# ```Horizontal Line```
hr_line = tk.Frame(data_insights_card_1_frame, bg="gray", height=2, bd=0)
hr_line.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=12)


# ```Data Insights Card 1 Total Rows Label```
data_insights__total_rows_label = tk.Label(
    data_insights_card_1_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    font=("Courier",12,"bold"),
    text="Total Rows        :"
)
data_insights__total_rows_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=20, pady=12)

# ```Data Insights Card 1 Total Columns Label```
data_insights__total_columns_label = tk.Label(
    data_insights_card_1_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    font=("Courier",12,"bold"),
    text="Total Columns     :"
)
data_insights__total_columns_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=20, pady=12)


# --- Data Insights Card 2 Frame ---
data_insights_card_2_frame = tk.Frame(
    data_insights_frame,
    bg="#0a2134",
    bd=1,
    relief="solid"
)
data_insights_card_2_frame.grid(row=3, column=1,padx=5, pady=7, sticky="ew")
data_insights_card_2_frame.grid_columnconfigure(0, weight=1)


# ```Data Insinsights Card 2 Title Label```
data_insights_card_2_title_label = tk.Label(
    data_insights_card_2_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    text="Data Summary",
    font=("Courier", 14, "bold")
)
data_insights_card_2_title_label.grid(row=1, column=0, pady=15, padx=20,sticky="w")


# ```Horizontal Line```
hr_line = tk.Frame(data_insights_card_2_frame, bg="gray", height=2, bd=0)
hr_line.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=12)


# ```Data Insights Card 2 Duplicate Rows Label```
data_insights_duplicate_rows_label = tk.Label(
    data_insights_card_2_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    font=("Courier",12,"bold"),
    text="Duplicate Value Rows  :"
)
data_insights_duplicate_rows_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=20, pady=12)

# ```Data Insights Card 2 Missing Rows Label```
data_insights_missing_rows_label = tk.Label(
    data_insights_card_2_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    font=("Courier",12,"bold"),
    text="Missing Value Rows    :"
)
data_insights_missing_rows_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=20, pady=12)


# ```Data Insights Show Summary Button```
data_insights_show_summary_button = tk.Button(
    data_insights_frame,
    bg="#20457F",
    # activebackground="#2C4266",
    fg="#c7c7c8",
    bd=1,
    relief="groove",
    font=("Courier",16,"bold"),
    text="Show Summary"
)
data_insights_show_summary_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20, pady=12, ipadx=10, ipady=4)


data_insights_show_summary_button.config(
    command=lambda: logic.show_summary(
        data_insights__total_rows_label,
        data_insights__total_columns_label,
        data_insights_duplicate_rows_label,
        data_insights_missing_rows_label
    )
)


# --- Data Insights Card 3 Frame ---
data_insights_card_3_frame = tk.Frame(
    data_insights_frame,
    bg="#0a2134",
    bd=1,
    relief="solid"  
)
data_insights_card_3_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=7, sticky="ew")
data_insights_card_3_frame.grid_columnconfigure(0, weight=1)
data_insights_card_3_frame.grid_columnconfigure(1, weight=1)

# --- Data Insights Card 3 Title Label ---
data_insights_card_3_title_label = tk.Label(
    data_insights_card_3_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    text="Add Row & Column : Separated By ( , )",
    font=("Courier", 14, "bold")
)
data_insights_card_3_title_label.grid(row=1, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

# ```Horizontal Line```
hr_line_3 = tk.Frame(data_insights_card_3_frame, bg="gray", height=2, bd=0)
hr_line_3.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=12)

# ```data insights add row colum Entry Box````
data_insights_add_row_column_entry_box = tk.Entry(
    data_insights_card_3_frame,
    bg="#646c72",
    fg="#01012b",
    font=("Courier", 12, "bold"),
    bd=1,
    relief="flat"
)
data_insights_add_row_column_entry_box.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=12)

# ```Add Row Button```
data_insights_add_row_button = tk.Button(
    data_insights_card_3_frame,
    bg="#1C473E",
    fg="#f8fafc",
    font=("Courier", 12, "bold"),
    text="Add Row",
    bd=1,
    relief="groove"
)
data_insights_add_row_button.grid(row=4, column=0, padx=(20, 5), sticky="ew", pady=12)
data_insights_add_row_button.config(
    command=lambda: logic.add_row(data_insights_add_row_column_entry_box, tree)
)

# ```Add Column Button```
data_insights_add_column_button = tk.Button(
    data_insights_card_3_frame,
    bg="#1a4357",
    fg="#c7c7c8",
    font=("Courier", 12, "bold"),
    text="Add Column",
    bd=1,
    relief="groove"
)
data_insights_add_column_button.grid(row=4, column=1, padx=(5, 20), sticky="ew", pady=12)
data_insights_add_column_button.config(
    command=lambda: logic.add_column(data_insights_add_row_column_entry_box, tree)
)

# ```Horizontal Line```
hr_line_3 = tk.Frame(data_insights_card_3_frame, bg="gray", height=2, bd=0)
hr_line_3.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=12)


# --- Data Insights Delete Section Title Label ---
data_insights_card_3_title_label = tk.Label(
    data_insights_card_3_frame,
    bg="#0a2134",
    fg="#c7c7c8",
    text="Deletee: Selected Row & Column",
    font=("Courier", 14, "bold")
)
data_insights_card_3_title_label.grid(row=6, column=0, columnspan=2, pady=5, padx=20, sticky="ew")


# ```Horizontal Line```
hr_line_3 = tk.Frame(data_insights_card_3_frame, bg="gray", height=2, bd=0)
hr_line_3.grid(row=7, column=0, columnspan=2, sticky="ew", padx=5, pady=12)

# ```Delete Row Button```
data_insights_Delete_row_button = tk.Button(
    data_insights_card_3_frame,
    bg="#872F2F",
    fg="#f8fafc",
    font=("Courier", 12, "bold"),
    text="Delete Row",
    bd=1,
    relief="groove"
)
data_insights_Delete_row_button.grid(row=8, column=0, padx=(20, 5), sticky="ew", pady=12)
data_insights_Delete_row_button.config(
    command=lambda: logic.delete_row(tree)
)

# ```Delete Column Button```
data_insights_Delete_column_button = tk.Button(
    data_insights_card_3_frame,
    bg="#874E2F",
    fg="#c7c7c8",
    font=("Courier", 12, "bold"),
    text="Delete Column",
    bd=1,
    relief="groove"
)
data_insights_Delete_column_button.grid(row=8, column=1, padx=(5, 20), sticky="ew", pady=12)
data_insights_Delete_column_button.config(
    command=lambda: logic.delete_column(tree)
)


# === Footer Section ===

# ```Footer Frame```
footer_frame = tk.Frame(
    window,
    bg="#1e293b",
    bd=5,
    relief="flat"
)
footer_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
footer_frame.grid_columnconfigure(0,weight=1)
footer_frame.grid_columnconfigure(1, weight=1)

# ```Footer Frame Status Label (Left Side)```
footer_status_label = tk.Label(
    footer_frame,
    bg="#1e293b",
    fg="#03AE53",
    font=("Courier", 15, "bold"),
    text="Status: Ready To View CSV Data",
)
footer_status_label.grid(row=3, column=0, padx=20, pady=10, sticky="w") 

# ```Footer Save CSV Button```
footer_save_csv_button = tk.Button(
    footer_frame,
    bg="#1A694F",
    fg="white",
    width=15,
    font=("Courier", 14, "bold"),
    bd=1,
    relief="solid",
    text=" SAVE CSV Data",
)
footer_save_csv_button.grid(row=3, column=1, padx=20, pady=10, sticky="e")
footer_save_csv_button.config(
    command=lambda: logic.save_csv(logic.df)
)

# ```Footer Exit Button```
footer_load_csv_button = tk.Button(
    footer_frame,
    bg="#21676C",
    fg="white",
    width=15,
    font=("Courier", 14, "bold"),
    bd=1,
    relief="solid",
    text=" Load New CSV "
)
footer_load_csv_button.grid(row=3, column=2, padx=10, pady=10, sticky="e")
footer_load_csv_button.config(
    command=lambda: logic.load_new_csv(tree)
)



# === Run Window ===
window.mainloop()
