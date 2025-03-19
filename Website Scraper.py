import tkinter as tk
from tkinter import scrolledtext
import urllib.request
import re

def scrapBlogs():

    url = url_entry.get()

    if not url:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a valid URL.\n")
        return

    try:

        pageToScrape = urllib.request.urlopen(url).read().decode('utf-8')

        titles = re.findall(r'<p class="bD0vt9 kN1aIK">(.*?)</p>', pageToScrape)

        views = re.findall(r'<span class="eYQJQu">(.*?)</span>', pageToScrape)

        output_text.delete(1.0, tk.END) 
        if titles and views:
            for view, title in zip(views, titles):
                output_text.insert(tk.END, f'{title} - Views: {view}\n')
        else:
            output_text.insert(tk.END, "No titles or views found.\n")

        output_text.insert(tk.END, "\nScraping Completed")

    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}\n")
#---

window = tk.Tk()

window_width=400
window_height=300

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x_position=(screen_width//2) - (window_width//2)
y_position=(screen_height//2) - (window_height//2)

window.title("Web Scraper GUI")

label = tk.Label(window, text="Enter the URL to scrape:", font=("Arial", 14))
label.pack(pady=10)

url_entry = tk.Entry(window, font=("Arial", 12), width=50)
url_entry.pack(pady=10)

scrape_button = tk.Button(window, text="Scrape Webpage", font=("Arial", 12), command=scrapBlogs)
scrape_button.pack(pady=10)

output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15, font=("Arial", 12))
output_text.pack(pady=10)

window.mainloop()
