import re
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

def load_text(file_path):
    """Load text from a given file path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")
        return None

def find_words(text, words):
    """Find occurrences of given words in the text, supporting multiple Indian languages."""
    word_counts = Counter()
    words_set = set(words)
    word_list = re.findall(r'[\u0900-\u097F\u0980-\u09FF\u0A00-\u0A7F\u0B00-\u0B7F\u0B80-\u0BFF\u0C00-\u0C7F\u0D00-\u0D7F\w]+', text.lower())
    word_context = {}

    for i, word in enumerate(word_list):
        if word in words_set:
            word_counts[word] += 1
            context_before = ' '.join(word_list[max(0, i-10):i])
            context_after = ' '.join(word_list[i+1:min(len(word_list), i+11)])
            word_context[word] = word_context.get(word, []) + [(context_before, word, context_after)]

    return word_counts, word_context

def analyze_text():
    file_path = file_path_var.get()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a file.")
        return

    additional_words = words_entry.get().strip()
    words_to_search = predefined_words[:]
    if additional_words:
        words_to_search.extend([word.strip() for word in additional_words.split(',')])

    text = load_text(file_path)
    if text:
        word_counts, word_context = find_words(text, words_to_search)

        report_text.delete(1.0, tk.END)
        if not word_counts:
            report_text.insert(tk.END, "No explicit words found. Text looks clean.")
        else:
            report_text.insert(tk.END, "Text Analyzer Report\n==============================\n")
            for word, count in word_counts.items():
                report_text.insert(tk.END, f"'{word}' found {count} times.\n")
            report_text.insert(tk.END, "\n==============================\n")

            report_text.insert(tk.END, "\nWord Context:\n")
            for word, contexts in word_context.items():
                report_text.insert(tk.END, f"\nOccurrences of '{word}':\n")
                for before, match, after in contexts:
                    report_text.insert(tk.END, f"...{before} >> {match} << {after}...\n")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    file_path_var.set(file_path)

# ✅ Initialize Tkinter GUI
root = tk.Tk()
root.title("Text Analyzer")
root.geometry("600x500")

tk.Label(root, text="Select File:").pack()
file_path_var = tk.StringVar()
file_entry = tk.Entry(root, textvariable=file_path_var, width=50)
file_entry.pack()
tk.Button(root, text="Browse", command=browse_file).pack()

tk.Label(root, text="Enter additional words (comma-separated):").pack()
words_entry = tk.Entry(root, width=50)
words_entry.pack()

tk.Button(root, text="Analyze", command=analyze_text).pack()

report_text = tk.Text(root, height=15, width=70)
report_text.pack()

predefined_words = [
    "hi", "hello", "nikhil", "patil", "नमस्ते", "परीक्षण", "पटिल",  # Hindi/Marathi
    "বাংলা", "প্রযুক্তি", "সুপ্রভাত",  # Bengali
    "నమస్తే", "తెలుగు", "పరీక్ష",  # Telugu
    "வணக்கம்", "தமிழ்", "சோதனை",  # Tamil
    "മലയാളം", "പരീക്ഷണം", "നമസ്കാരം"  # Malayalam
]

root.mainloop()