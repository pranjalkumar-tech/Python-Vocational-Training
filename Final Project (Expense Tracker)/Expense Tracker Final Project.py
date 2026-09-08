import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Other"]

# --- Colors ---
BG = "#1e1f29"
CARD = "#282a3a"
ACCENT = "#7c83fd"
ACCENT_DARK = "#5a62e8"
TEXT = "#eaeaf2"
SUBTEXT = "#9a9cb8"
DANGER = "#ff6b6b"
ROW_ALT = "#2f3145"

# --- Database ---
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        date TEXT,
        note TEXT
    )
""")

conn.commit()

selected_id = None  # Stores the selected expense ID


def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM expenses ORDER BY date DESC, id DESC")

    for i, row in enumerate(cursor.fetchall()):
        tag = "odd" if i % 2 else "even"
        tree.insert("", tk.END, values=row, tags=(tag,))

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0

    total_label.config(text=f"Total spent:  ₹{total:,.2f}")


def clear_form():
    global selected_id

    amount_entry.delete(0, tk.END)
    category_var.set(CATEGORIES[0])

    date_entry.delete(0, tk.END)
    date_entry.insert(0, date.today().isoformat())

    note_entry.delete(0, tk.END)

    selected_id = None
    add_btn.config(text="Add Expense")


def add_expense():
    global selected_id

    amount = amount_entry.get().strip()
    category = category_var.get()
    expense_date = date_entry.get().strip()
    note = note_entry.get().strip()

    try:
        amount = float(amount)

        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0.")
            return

    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    try:
        date.fromisoformat(expense_date)
    except ValueError:
        messagebox.showerror("Error", "Date must look like 2026-08-12.")
        return

    if selected_id is not None:
        cursor.execute(
            """
            UPDATE expenses
            SET amount = ?, category = ?, date = ?, note = ?
            WHERE id = ?
            """,
            (amount, category, expense_date, note, selected_id)
        )

        conn.commit()
        messagebox.showinfo("Success", "Expense updated successfully.")

    else:
        cursor.execute(
            """
            INSERT INTO expenses (amount, category, date, note)
            VALUES (?, ?, ?, ?)
            """,
            (amount, category, expense_date, note)
        )

        conn.commit()
        messagebox.showinfo("Success", "Expense added successfully.")

    clear_form()
    refresh_table()


def delete_expense():
    if selected_id is None:
        messagebox.showwarning("Nothing selected", "Click a row first.")
        return

    answer = messagebox.askyesno(
        "Delete Expense",
        "Are you sure you want to delete this expense?"
    )

    if answer:
        cursor.execute(
            "DELETE FROM expenses WHERE id = ?",
            (selected_id,)
        )

        conn.commit()
        clear_form()
        refresh_table()


def on_row_click(event):
    global selected_id

    selected = tree.selection()

    if not selected:
        return

    values = tree.item(selected[0], "values")

    selected_id = int(values[0])

    amount_entry.delete(0, tk.END)
    amount_entry.insert(0, values[1])

    category_var.set(values[2])

    date_entry.delete(0, tk.END)
    date_entry.insert(0, values[3])

    note_entry.delete(0, tk.END)
    note_entry.insert(0, values[4])

    add_btn.config(text="Update Expense")


def close_app():
    conn.close()
    root.destroy()


# ---------------- window setup ----------------

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("680x520")
root.configure(bg=BG)
root.minsize(600, 460)
root.protocol("WM_DELETE_WINDOW", close_app)

style = ttk.Style(root)
style.theme_use("clam")

style.configure("TFrame", background=BG)
style.configure("Card.TFrame", background=CARD)

style.configure(
    "TLabel",
    background=BG,
    foreground=TEXT,
    font=("Segoe UI", 10)
)

style.configure(
    "Card.TLabel",
    background=CARD,
    foreground=SUBTEXT,
    font=("Segoe UI", 9, "bold")
)

style.configure(
    "Title.TLabel",
    background=BG,
    foreground=TEXT,
    font=("Segoe UI", 16, "bold")
)

style.configure(
    "Total.TLabel",
    background=BG,
    foreground=ACCENT,
    font=("Segoe UI", 13, "bold")
)

style.configure(
    "TEntry",
    fieldbackground="#3a3d54",
    foreground=TEXT,
    insertcolor=TEXT,
    borderwidth=0,
    padding=6
)

style.map(
    "TEntry",
    fieldbackground=[("focus", "#454869")]
)

style.configure(
    "TCombobox",
    fieldbackground="#3a3d54",
    background="#3a3d54",
    foreground=TEXT,
    arrowcolor=TEXT,
    borderwidth=0,
    padding=6
)

style.map(
    "TCombobox",
    fieldbackground=[("readonly", "#3a3d54")],
    foreground=[("readonly", TEXT)]
)

style.configure(
    "Accent.TButton",
    background=ACCENT,
    foreground="#ffffff",
    font=("Segoe UI", 10, "bold"),
    borderwidth=0,
    padding=8
)

style.map(
    "Accent.TButton",
    background=[("active", ACCENT_DARK)]
)

style.configure(
    "Danger.TButton",
    background=DANGER,
    foreground="#ffffff",
    font=("Segoe UI", 10, "bold"),
    borderwidth=0,
    padding=8
)

style.map(
    "Danger.TButton",
    background=[("active", "#e04b4b")]
)

style.configure(
    "Treeview",
    background=CARD,
    fieldbackground=CARD,
    foreground=TEXT,
    rowheight=28,
    borderwidth=0,
    font=("Segoe UI", 9)
)

style.configure(
    "Treeview.Heading",
    background="#3a3d54",
    foreground=TEXT,
    font=("Segoe UI", 9, "bold"),
    borderwidth=0
)

style.map(
    "Treeview",
    background=[("selected", ACCENT)],
    foreground=[("selected", "#ffffff")]
)

style.map(
    "Treeview.Heading",
    background=[("active", "#454869")]
)


# ---------------- header ----------------

header = ttk.Frame(root, style="TFrame")
header.pack(fill="x", padx=20, pady=(18, 6))

ttk.Label(
    header,
    text="💰 Expense Tracker",
    style="Title.TLabel"
).pack(side="left")


# ---------------- form card ----------------

form_card = ttk.Frame(root, style="Card.TFrame")
form_card.pack(fill="x", padx=20, pady=10)

form = ttk.Frame(form_card, style="Card.TFrame", padding=16)
form.pack(fill="x")

ttk.Label(
    form,
    text="AMOUNT",
    style="Card.TLabel"
).grid(row=0, column=0, sticky="w", padx=(0, 8))

amount_entry = ttk.Entry(form, width=12)
amount_entry.grid(
    row=1,
    column=0,
    padx=(0, 16),
    pady=(2, 10),
    sticky="w"
)

ttk.Label(
    form,
    text="CATEGORY",
    style="Card.TLabel"
).grid(row=0, column=1, sticky="w", padx=(0, 8))

category_var = tk.StringVar(value=CATEGORIES[0])

ttk.Combobox(
    form,
    textvariable=category_var,
    values=CATEGORIES,
    width=13,
    state="readonly"
).grid(
    row=1,
    column=1,
    padx=(0, 16),
    pady=(2, 10),
    sticky="w"
)

ttk.Label(
    form,
    text="DATE",
    style="Card.TLabel"
).grid(row=0, column=2, sticky="w", padx=(0, 8))

date_entry = ttk.Entry(form, width=13)
date_entry.insert(0, date.today().isoformat())

date_entry.grid(
    row=1,
    column=2,
    padx=(0, 16),
    pady=(2, 10),
    sticky="w"
)

ttk.Label(
    form,
    text="NOTE",
    style="Card.TLabel"
).grid(row=0, column=3, sticky="w", padx=(0, 8))

note_entry = ttk.Entry(form, width=20)
note_entry.grid(
    row=1,
    column=3,
    pady=(2, 10),
    sticky="w"
)

btn_row = ttk.Frame(form, style="Card.TFrame")
btn_row.grid(
    row=2,
    column=0,
    columnspan=4,
    pady=(6, 0),
    sticky="w"
)

add_btn = ttk.Button(
    btn_row,
    text="Add Expense",
    style="Accent.TButton",
    command=add_expense
)

add_btn.pack(side="left", padx=(0, 10))

ttk.Button(
    btn_row,
    text="Delete Selected",
    style="Danger.TButton",
    command=delete_expense
).pack(side="left", padx=(0, 10))

ttk.Button(
    btn_row,
    text="Clear Form",
    command=clear_form
).pack(side="left")


# ---------------- table ----------------

table_card = ttk.Frame(root, style="Card.TFrame")
table_card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(6, 10)
)

columns = ("id", "amount", "category", "date", "note")

tree = ttk.Treeview(
    table_card,
    columns=columns,
    show="headings",
    height=10
)

headings = {
    "id": "ID",
    "amount": "Amount",
    "category": "Category",
    "date": "Date",
    "note": "Note"
}

widths = {
    "id": 50,
    "amount": 90,
    "category": 110,
    "date": 100,
    "note": 180
}

for col in columns:
    tree.heading(col, text=headings[col])
    tree.column(
        col,
        width=widths[col],
        anchor="center" if col != "note" else "w"
    )

tree.tag_configure("odd", background=ROW_ALT)
tree.tag_configure("even", background=CARD)

vsb = ttk.Scrollbar(
    table_card,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=vsb.set)

tree.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(8, 0),
    pady=8
)

vsb.pack(
    side="right",
    fill="y",
    pady=8,
    padx=(0, 8)
)

tree.bind("<<TreeviewSelect>>", on_row_click)


# ---------------- footer ----------------

footer = ttk.Frame(root, style="TFrame")
footer.pack(
    fill="x",
    padx=20,
    pady=(0, 16)
)

total_label = ttk.Label(
    footer,
    text="Total spent:  ₹0.00",
    style="Total.TLabel"
)

total_label.pack(side="right")


refresh_table()
root.mainloop()
