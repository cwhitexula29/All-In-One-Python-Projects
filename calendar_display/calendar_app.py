import tkinter as tk
from tkinter import messagebox
import calendar

def main():
    root = tk.Tk()
    root.title("Calendar App")
    root.geometry("300x150")
    
    tk.Label(root, text="Enter Year:").pack(pady=5)
    year_entry = tk.Entry(root)
    year_entry.pack(pady=5)
    
    def show_calendar():
        # Placeholder function for showing calendar
        print("Show calendar function placeholder")
    
    tk.Button(root, text="Show Calendar", command=show_calendar).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()