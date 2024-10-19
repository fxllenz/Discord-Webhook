import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.title("Webhook Sender - Made by fallen")
root.geometry("600x490")
root.config(bg="#2c2f33")
root.iconbitmap(resource_path("icon.ico"))

embeds = []


def test_webhook():
    webhook_url = url_entry.get()
    if not webhook_url:
        messagebox.showerror("Error", "Webhook URL is required")
        return

    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            test_button.config(bg="#43b581")  
        else:
            test_button.config(bg="#f04747")  
            messagebox.showerror("Error", "Webhook URL is invalid. Status code: " + str(response.status_code))
    except Exception as e:
        test_button.config(bg="#f04747") 
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def send_webhook():
    webhook_url = url_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    username = username_entry.get()
    avatar_url = avatar_url_entry.get()

    embed = {}
    
    title = embed_title_entry.get()
    description = embed_description_text.get("1.0", tk.END).strip()
    color = color_entry.get()

    if title:
        embed["title"] = title
    if description:
        embed["description"] = description
    if color:
        try:
            embed["color"] = int(color, 16) 
        except ValueError:
            messagebox.showerror("Error", "Invalid color code (use hexadecimal).")
            return
    
    if author_name_entry.get():
        embed["author"] = {"name": author_name_entry.get()}

    if footer_text_entry.get():
        embed["footer"] = {"text": footer_text_entry.get()}

    if image_url_entry.get():
        embed["image"] = {"url": image_url_entry.get()}

    if thumbnail_url_entry.get():
        embed["thumbnail"] = {"url": thumbnail_url_entry.get()}

    embeds = [embed]  
    
    payload = {
        "content": content,
        "username": username if username else None,
        "avatar_url": avatar_url if avatar_url else None,
        "embeds": embeds if  embeds else None

    }

    if not webhook_url:
        messagebox.showerror("Error", "Webhook URL is required")
        return

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            messagebox.showinfo("Success", "Webhook sent successfully!")
        else:
            messagebox.showerror("Error", f"Failed to send webhook. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def style_entry(widget):
    widget.config(highlightbackground="#23272a", highlightthickness=1, borderwidth=0)
    widget.config(bg="#23272a", fg="white", insertbackground="white", relief="flat")


header_frame = tk.Frame(root, bg="#2c2f33")
header_frame.pack(pady=10)
tk.Label(header_frame, text="Webhook URL:", bg="#2c2f33", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=5)
url_entry = tk.Entry(header_frame, width=40)
style_entry(url_entry)
url_entry.grid(row=0, column=1, padx=5)
test_button = tk.Button(header_frame, text="Test Webhook", command=test_webhook, bg="#7289da", fg="white", width=15)
test_button.grid(row=0, column=2, padx=5)
send_button = tk.Button(root, text="Send Webhook", command=send_webhook, bg="#43b581", fg="white", width=50)
send_button.pack(pady=10)
input_frame = tk.Frame(root, bg="#2c2f33")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Username (Optional):", bg="#2c2f33", fg="white").grid(row=0, column=0, padx=5)
username_entry = tk.Entry(input_frame, width=50)
style_entry(username_entry)
username_entry.grid(row=0, column=1, padx=5)
tk.Label(input_frame, text="Avatar URL (Optional):", bg="#2c2f33", fg="white").grid(row=1, column=0, padx=5)
avatar_url_entry = tk.Entry(input_frame, width=50)
style_entry(avatar_url_entry)
avatar_url_entry.grid(row=1, column=1, padx=5)
tk.Label(input_frame, text="Content:", bg="#2c2f33", fg="white").grid(row=2, column=0, padx=5)
content_text = scrolledtext.ScrolledText(input_frame, width=50, height=4, bg="#23272a", fg="white", insertbackground="white", relief="flat")
content_text.grid(row=2, column=1, padx=5)
embed_frame = tk.Frame(root, bg="#2c2f33")
embed_frame.pack(pady=10)
tk.Label(embed_frame, text="Embed Title:", bg="#2c2f33", fg="white").grid(row=0, column=0, padx=5)
embed_title_entry = tk.Entry(embed_frame, width=50)
style_entry(embed_title_entry)
embed_title_entry.grid(row=0, column=1, padx=5)
tk.Label(embed_frame, text="Embed Description:", bg="#2c2f33", fg="white").grid(row=1, column=0, padx=5)
embed_description_text = scrolledtext.ScrolledText(embed_frame, width=50, height=4, bg="#23272a", fg="white", insertbackground="white", relief="flat")
embed_description_text.grid(row=1, column=1, padx=5)
tk.Label(embed_frame, text="Embed Color (Hex):", bg="#2c2f33", fg="white").grid(row=2, column=0, padx=5)
color_entry = tk.Entry(embed_frame, width=50)
style_entry(color_entry)
color_entry.grid(row=2, column=1, padx=5)
tk.Label(embed_frame, text="Author Name (Optional):", bg="#2c2f33", fg="white").grid(row=3, column=0, padx=5)
author_name_entry = tk.Entry(embed_frame, width=50)
style_entry(author_name_entry)
author_name_entry.grid(row=3, column=1, padx=5)
tk.Label(embed_frame, text="Footer Text (Optional):", bg="#2c2f33", fg="white").grid(row=4, column=0, padx=5)
footer_text_entry = tk.Entry(embed_frame, width=50)
style_entry(footer_text_entry)
footer_text_entry.grid(row=4, column=1, padx=5)
tk.Label(embed_frame, text="Image URL (Optional):", bg="#2c2f33", fg="white").grid(row=5, column=0, padx=5)
image_url_entry = tk.Entry(embed_frame, width=50)
style_entry(image_url_entry)
image_url_entry.grid(row=5, column=1, padx=5)
tk.Label(embed_frame, text="Thumbnail URL (Optional):", bg="#2c2f33", fg="white").grid(row=6, column=0, padx=5)
thumbnail_url_entry = tk.Entry(embed_frame, width=50)
style_entry(thumbnail_url_entry)
thumbnail_url_entry.grid(row=6, column=1, padx=5)
root.mainloop()
