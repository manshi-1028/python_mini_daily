import tkinter as tk
from tkinter import messagebox
import random
import time
from words import word_list

class TypingSpeedTest:

    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.start_time = None
        self.running = False

        self.sample_text = " ".join(random.sample(word_list, 25))

        title = tk.Label(
            root,
            text="Typing Speed Test",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=10)

        self.text_label = tk.Label(
            root,
            text=self.sample_text,
            wraplength=650,
            font=("Arial", 14),
            justify="left"
        )
        self.text_label.pack(pady=10)

        self.entry = tk.Text(root, height=5, width=70, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.entry.bind("<KeyPress>", self.start_test)

        self.timer_label = tk.Label(
            root,
            text="Time: 0s",
            font=("Arial", 12)
        )
        self.timer_label.pack()

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        check_btn = tk.Button(
            button_frame,
            text="Check Result",
            command=self.calculate_result
        )
        check_btn.grid(row=0, column=0, padx=10)

        reset_btn = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_test
        )
        reset_btn.grid(row=0, column=1, padx=10)

    def start_test(self, event):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_timer()

    def update_timer(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed}s")
            self.root.after(1000, self.update_timer)

    def calculate_result(self):
        if not self.running:
            return

        self.running = False

        typed_text = self.entry.get("1.0", tk.END).strip()

        elapsed_time = time.time() - self.start_time

        typed_words = typed_text.split()
        sample_words = self.sample_text.split()

        correct = 0

        for typed, actual in zip(typed_words, sample_words):
            if typed == actual:
                correct += 1

        minutes = elapsed_time / 60

        wpm = len(typed_words) / minutes if minutes > 0 else 0
        accuracy = (correct / len(sample_words)) * 100

        messagebox.showinfo(
            "Results",
            f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"
        )

    def reset_test(self):
        self.running = False

        self.sample_text = " ".join(random.sample(word_list, 25))

        self.text_label.config(text=self.sample_text)

        self.entry.delete("1.0", tk.END)

        self.timer_label.config(text="Time: 0s")


root = tk.Tk()
TypingSpeedTest(root)
root.mainloop()
