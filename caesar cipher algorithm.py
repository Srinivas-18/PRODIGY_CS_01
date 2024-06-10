import tkinter as tk
from tkinter import messagebox

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        result = ""
        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result

    def decrypt(self, message):
        result = ""
        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Caesar Cipher")

        self.message_label = tk.Label(master, text="Enter a message:")
        self.message_label.pack()

        self.message_entry = tk.Text(master, height=10, width=40)
        self.message_entry.pack()

        self.shift_label = tk.Label(master, text="Enter a shift value:")
        self.shift_label.pack()

        self.shift_entry = tk.Entry(master, width=10)
        self.shift_entry.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.pack()

    def encrypt(self):
        message = self.message_entry.get("1.0", "end-1c")
        shift = int(self.shift_entry.get())
        cipher = CaesarCipher(shift)
        encrypted = cipher.encrypt(message)
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", encrypted)

    def decrypt(self):
        message = self.message_entry.get("1.0", "end-1c")
        shift = int(self.shift_entry.get())
        cipher = CaesarCipher(shift)
        decrypted = cipher.decrypt(message)
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", decrypted)

root = tk.Tk()
gui = GUI(root)
root.mainloop()