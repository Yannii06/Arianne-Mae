import tkinter as tk

from tkinter import Tk, Label, Entry, Button, Frame, Listbox, Scrollbar, messagebox

class ContactListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact List App")
        self.master.configure(bg="slategray3")  # Setting background color
        self.master.geometry("400x400")

        self.contacts = [
            "Joy: 09213467890",
            "Nico: 09507032210",
            "Arwyn: 09319744755",
            "Kyla: 09703599960",
            "Myrna 09227446543",
            "Karl: 09749502190",
            "Lance: 09457122033",
            "Trixi: 09303497686",
            "Jamaica: 09631475689",
            "Christian: 09564438292"
        ]

        self.title_label = Label(master, text="Contact List App", bg="slategray3", fg="white", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = Label(master, text="Name:", bg="slategray3", fg="white")
        self.name_label.grid(row=1, column=0)

        self.name_entry = Entry(master)
        self.name_entry.grid(row=1, column=1)

        self.phone_label = Label(master, text="Phone:", bg="slategray3", fg="white")
        self.phone_label.grid(row=2, column=0)

        self.phone_entry = Entry(master)
        self.phone_entry.grid(row=2, column=1)

        self.add_button = Button(master, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        self.contact_frame = Frame(master, bg="slategray3")
        self.contact_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.contact_scrollbar = Scrollbar(self.contact_frame, orient="vertical")
        self.contact_scrollbar.pack(side="right", fill="y")

        self.contact_listbox = Listbox(self.contact_frame, yscrollcommand=self.contact_scrollbar.set)
        self.contact_listbox.pack(side="left", fill="both", expand=1)
        self.contact_scrollbar.config(command=self.contact_listbox.yview)

        self.delete_button = Button(master, text="Delete Contact", command=self.delete_contact, bg="#f44336", fg="white")
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        self.view_button = Button(master, text="View Contact", command=self.view_contact, bg="#2196F3", fg="white")
        self.view_button.grid(row=6, column=0, pady=5, padx=5, sticky="we")

        self.reset_button = Button(master, text="Reset Fields", command=self.reset_fields, bg="#FFC107", fg="white")
        self.reset_button.grid(row=6, column=1, pady=5, padx=5, sticky="we")

        self.edit_button = Button(master, text="Edit Contact", command=self.edit_contact, bg="#FF5722", fg="white")
        self.edit_button.grid(row=7, column=0, columnspan=2, pady=5, padx=5, sticky="we")

        
        for contact in self.contacts:
            self.contact_listbox.insert("end", contact)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact_info = f"{name}: {phone}"
            self.contacts.append(contact_info)
            self.contact_listbox.insert("end", contact_info)
            self.name_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contact_listbox.delete(selected_index)
            del self.contacts[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def view_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact_info = self.contact_listbox.get(selected_index)
            messagebox.showinfo("Contact Info", contact_info)
        else:
            messagebox.showwarning("Warning", "Please select a contact to view.")

    def reset_fields(self):
        self.name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact_info = self.contact_listbox.get(selected_index)
            name, phone = contact_info.split(':')
            self.name_entry.insert("end", name.strip())
            self.phone_entry.insert("end", phone.strip())
            self.delete_contact()
        else:
            messagebox.showwarning("Warning", "Please select a contact to edit.")

def main():
    root = Tk()
    app = ContactListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
