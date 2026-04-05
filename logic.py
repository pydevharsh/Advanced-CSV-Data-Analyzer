import pandas as pd
from tkinter import filedialog

# global data
df = None
selected_column = None



'''
---------------------------------
|         Alert Logic           |
---------------------------------
'''

def check_data_loaded():
    global df

    from tkinter import messagebox

    # 🔹 Step 1: Check if DataFrame exists
    if df is None:
        # 🔹 Step 2: Show Alert Popup
        messagebox.showerror(
            "Error",
            "⚠ Please load a CSV file first!"
        )
        return False

    # 🔹 Step 3: If data exists → continue
    return True



'''
---------------------------------
|         Open CSV              |
---------------------------------
'''

def open_csv(tree, status_label):
    global df

    # Step 1: file select
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )

    # --- IF File Are Not Selected So Function Are Stoped --- 
    if not file_path:
        return

    # Step 2: read csv
    df = pd.read_csv(file_path)

    # Step 3: clear old data
    tree.delete(*tree.get_children())

    # Step 4: set columns
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    # Step 5: insert rows
    for row in df.values:
        tree.insert("", "end", values=list(row))



'''
---------------------------------
|        Refresh DATA           |
---------------------------------
'''

def refresh_data(tree):
    global df

    # 🔹 Alert Check
    if not check_data_loaded():
        return

    # 🔹 Step 1: Check if DataFrame exists
    if df is None:
        print("❌ No data to refresh")
        return

    # 🔹 Step 2: Clear existing table data
    tree.delete(*tree.get_children())

    # 🔹 Step 3: Reset columns (optional but safe)
    tree["columns"] = list(df.columns)

    # 🔹 Step 4: Configure headings and column width
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=130)

    # 🔹 Step 5: Insert data again
    for row in df.values:
        tree.insert("", "end", values=list(row))

    # 🔹 Step 6: Success Message
    print("🔄 Data Refreshed Successfully")



'''
---------------------------------
|            Exit App           |
---------------------------------
'''

def exit_app(window):

    # 🔹 Step 1: Import messagebox
    from tkinter import messagebox

    # 🔹 Step 2: Ask confirmation from user
    confirm = messagebox.askyesno(
        "Exit Application",
        "Are you sure you want to exit?"
    )

    # 🔹 Step 3: If user clicks Yes → close app
    if confirm:
        window.destroy()

    # 🔹 Step 4: If No → do nothing
    else:
        return
    


'''
---------------------------------
|         Show Summary          |
---------------------------------
'''

def show_summary(
        total_rows_label,
        total_columns_label,
        duplicate_label,
        missing_label
    ):
    global df

    # 🔹 Alert Check
    if not check_data_loaded():
        return

    # --- IF Dataframe Are None So Function Are Stoped --- 
    if df is None:
        return
    
    # Step 1: calculations
    total_rows      = len(df)
    total_columns   = len(df.columns)
    duplicate_rows  = df.duplicated().sum()
    missing_rows    = df.isnull().sum().sum()

    # Step 2: update UI
    total_rows_label.config(text=f"Total Rows : {total_rows}")
    total_columns_label.config(text=f"Total Columns : {total_columns}")
    duplicate_label.config(text=f"Duplicate Rows : {duplicate_rows}")
    missing_label.config(text=f"Missing Values : {missing_rows}")

    

'''
---------------------------------
|            Add Row            |
---------------------------------
'''

def add_row(entry,tree):
    global df

    # 🔹 Alert Check
    if not check_data_loaded():
        return
    
    # --- IF Dataframe Are None So Function Are Stoped ---
    if df is None:
        return
    
    # Step 1: Get Row Data From Entry Box
    data_insights_add_row_column_entry_box = entry.get()

    # --- IF Entry Box Are Empty So Function Are Stoped --- 
    if not data_insights_add_row_column_entry_box:
        return
    
    # Step 2: Split Row Data
    row_data = [x.strip() for x in data_insights_add_row_column_entry_box.split(",")]

    # Step 3: Validation Row Data
    if len(row_data) != len(df.columns):
        return
    
    # Step 4: Add Row 
    df.loc[len(df)] = row_data

    # Step 5: Refresh Tabel
    tree.delete(*tree.get_children())

    # Step 6: Loop Through Row Data
    for row in df.values:
        tree.insert("","end",values=list(row))
    
    print("✅ Row Added")
    


'''
---------------------------------
|           Add Column          |
---------------------------------
'''

def add_column(entry, tree):
    global df

    # 🔹 Alert Check
    if not check_data_loaded():
        return

    # --- IF Dataframe Are None So Function Are Stoped ---
    if df is None:
        return
    
    # Step 1: Get Column Name From Entry Box
    col_name = entry.get().strip()

    # --- IF Entry Box Are Empty So Function Are Stoped --- 
    if not col_name:
        return
    
    # Step 2 : Validation : IF Name Are Alrady Asign So Function Are Stoped.
    if col_name in df.columns:
        print(f"❌ Column '{col_name}' already exists")
        return
    
    # Step 3: Add Column Name In DataFrame 
    df[col_name] = "" 
    
    # Step 4: Tabel Clear
    tree.delete(*tree.get_children())

    # Step 5: Update Tree View With New Columns
    tree["columns"] = list(df.columns)
    
    # Step 6: Tabel Styling
    for col in df.columns:

        # Set Column Name
        tree.heading(col, text=col)

        # Set Column Width
        tree.column(col, width=130, stretch=False)
    
    # Show Old DataFrame
    for row in df.values:

        # Show Old DataFrame In TreeView
        tree.insert("", "end", values=list(row))
    

    print(f"✅ Column '{col_name}' Added")



'''
---------------------------------
|           Delet Row           |
---------------------------------
'''

def delete_row(tree):
    global df

    # 🔹 Alert Check
    if not check_data_loaded():
        return
    
    # --- IF Dataframe Are None So Function Are Stoped ---
    if df is None:
        return

    # Step 1: Get Selected Item
    selected_item = tree.selection()

    # --- IF Not Selected Item So Function Are Stoped --- 
    if not selected_item:
        return

    # Step 2: Get Row Index
    index = tree.index(selected_item)

    # Step 3: Delete from DataFrame
    df = df.drop(df.index[index])

    # Step 4: Reset Index (IMPORTANT)
    df.reset_index(drop=True, inplace=True)

    # Step 5: Refresh Table
    tree.delete(*tree.get_children())

    # Step 6: Loop Through Row Data
    for row in df.values:
        tree.insert("", "end", values=list(row))

    print("✅ Row Deleted")



'''
---------------------------------
|         Select Column         |
---------------------------------
'''

def select_column(event, tree):
    global selected_column

    # 🔹 Alert Check
    if not check_data_loaded():
        return

    region = tree.identify_region(event.x, event.y)

    if region != "heading":
        return

    col = tree.identify_column(event.x)
    col_index = int(col.replace("#", "")) - 1

    if col_index < 0 or col_index >= len(tree["columns"]):
        return

    selected_column = tree["columns"][col_index]

    print(f"✅ Selected Column: {selected_column}")



'''
---------------------------------
|         Delet Column          |
---------------------------------
'''

def delete_column(tree):
    global df, selected_column

    # 🔹 Alert Check
    if not check_data_loaded():
        return

    # 🔹 Step 1: Check if DataFrame exists
    if df is None:
        return

    # 🔹 Step 2: Check if any column is selected
    if selected_column is None:
        print("❌ No column selected")
        return

    # 🔹 Step 3: Debug print
    print("Deleting:", selected_column)

    # 🔹 Step 4: Delete the selected column from DataFrame
    df.drop(columns=[selected_column], inplace=True)

    # 🔹 Step 5: Reset selected column
    selected_column = None

    # 🔹 Step 6: Clear existing table data
    tree.delete(*tree.get_children())

    # 🔹 Step 7: Update table columns
    tree["columns"] = list(df.columns)

    # 🔹 Step 8: Reconfigure table headings and column width
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    # 🔹 Step 9: Insert updated data back into table
    for row in df.values:
        tree.insert("", "end", values=list(row))

    # 🔹 Step 10: Success message
    print("✅ Column Deleted")



'''
---------------------------------
|          Save CSV Data        |
---------------------------------
'''

def save_csv(df):

    # 🔹 Alert Check
    if not check_data_loaded():
        return
    
    # 🔹 Step 1: Check if DataFrame exists
    if df is None:
        print("❌ No data to save")
        return

    # 🔹 Step 2: Import file dialog
    from tkinter import filedialog

    # 🔹 Step 3: Open Save Dialog Box
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Save CSV File"
    )

    # 🔹 Step 4: If user cancels dialog → stop function
    if not file_path:
        return

    # 🔹 Step 5: Save DataFrame to CSV
    df.to_csv(file_path, index=False)

    # 🔹 Step 6: Success Message
    print("✅ CSV File Saved Successfully")



'''
---------------------------------
|         Load New CSV          |
---------------------------------
'''

def load_new_csv(tree):
    global df, selected_column

    # 🔹 Step 1: Import required modules
    from tkinter import filedialog
    import pandas as pd

    # 🔹 Step 2: Open File Dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")],
        title="Select CSV File"
    )

    # 🔹 Step 3: If user cancels → stop function
    if not file_path:
        return

    # 🔹 Step 4: Load CSV into DataFrame
    df = pd.read_csv(file_path)

    # 🔹 Step 5: Reset selected column
    selected_column = None

    # 🔹 Step 6: Clear existing table data
    tree.delete(*tree.get_children())

    # 🔹 Step 7: Set new columns in table
    tree["columns"] = list(df.columns)

    # 🔹 Step 8: Configure table headings and column width
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=130)

    # 🔹 Step 9: Insert new CSV data into table
    for row in df.values:
        tree.insert("", "end", values=list(row))

    # 🔹 Step 10: Success Message
    print("📂 New CSV Loaded Successfully")