import tkinter as tk
from tkinter import messagebox

class BankQueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NexusBank™ - Queue Management Dashboard")
        self.root.geometry("680x560") 
        self.root.configure(bg="#f3f4f6") 
        self.root.resizable(False, False)

        # Core Circular Queue Backend Variables
        self.MAX = 5
        self.queue = [None] * self.MAX
        self.front = -1
        self.rear = -1
        self.token_counter = 100

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        # 1. Header Frame Layout
        header_frame = tk.Frame(self.root, bg="#1e3a8a", height=70)
        header_frame.pack(fill="x")
        
        header_label = tk.Label(
            header_frame, 
            text="🏦 NexusBank Queue Controller", 
            font=("Arial", 18, "bold"), 
            fg="white", 
            bg="#1e3a8a", 
            pady=15
        )
        header_label.pack()

        # 2. Main Live Status Display Panel area
        self.display_frame = tk.LabelFrame(
            self.root, 
            text=" Real-Time Waiting Line Counter (Max 5 Lounge Chairs) ", 
            font=("Arial", 11, "bold"), 
            bg="white", 
            fg="#374151",
            padx=20, 
            pady=20
        )
        self.display_frame.pack(padx=20, pady=20, fill="x")

        # Dynamic Visual Chairs mapped on layout row
        self.chair_labels = []
        for i in range(self.MAX):
            lbl = tk.Label(
                self.display_frame, 
                text="🪑\nEmpty", 
                font=("Arial", 11), 
                bg="#e5e7eb", 
                fg="#6b7280", 
                width=10, 
                height=4, 
                bd=2, 
                relief="groove"
            )
            lbl.pack(side="left", padx=12)
            self.chair_labels.append(lbl)

        # 3. Action Control Grid System Panel
        control_frame = tk.Frame(self.root, bg="#f3f4f6")
        control_frame.pack(pady=10)

        self.btn_issue = tk.Button(
            control_frame, 
            text="🎟️ Issue One Token\n(1 Customer Arrives)", 
            font=("Arial", 10, "bold"), 
            bg="#10b981", 
            fg="white", 
            padx=10, 
            pady=10, 
            command=self.issue_token,
            bd=0, cursor="hand2"
        )
        self.btn_issue.grid(row=0, column=0, padx=10)

        self.btn_serve = tk.Button(
            control_frame, 
            text="💁‍♂️ Call Next Customer\n(Counter Free)", 
            font=("Arial", 10, "bold"), 
            bg="#3b82f6", 
            fg="white", 
            padx=10, 
            pady=10, 
            command=self.serve_customer,
            bd=0, cursor="hand2"
        )
        self.btn_serve.grid(row=0, column=1, padx=10)

        self.btn_fill_all = tk.Button(
            control_frame, 
            text="💥 Bulk Fill Lounge\n(Fill All At Once)", 
            font=("Arial", 10, "bold"), 
            bg="#7c3aed", 
            fg="white", 
            padx=10, 
            pady=10, 
            command=self.fill_all_slots,
            bd=0, cursor="hand2"
        )
        self.btn_fill_all.grid(row=0, column=2, padx=10)

        # 4. Diagnostics Metadata Status Bar at Bottom layout
        self.status_bar = tk.Label(
            self.root, 
            text="System Live • Front Pointer: -1 • Rear Pointer: -1", 
            font=("Arial", 10), bd=1, relief="sunken", anchor="w", 
            bg="#e5e7eb", fg="#4b5563", padx=10, pady=5
        )
        self.status_bar.pack(side="bottom", fill="x")

    def issue_token(self):
        if (self.rear + 1) % self.MAX == self.front:
            messagebox.showwarning("Lounge Full", "⚠️ Cannot issue ticket! All 5 waiting slots are completely full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.MAX
        self.token_counter += 1
        self.queue[self.rear] = self.token_counter
        self.update_display()

    def fill_all_slots(self):
        filled_any = False
        while (self.rear + 1) % self.MAX != self.front:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.MAX
            self.token_counter += 1
            self.queue[self.rear] = self.token_counter
            filled_any = True
            
        if filled_any:
            messagebox.showinfo("Bulk Fill", "⚡ Test Mode Active: All lounge seats filled with customers simultaneously!")
        else:
            messagebox.showwarning("Lounge Full", "⚠️ The lounge is already completely full!")
        self.update_display()

    def serve_customer(self):
        if self.front == -1:
            messagebox.showinfo("Line Empty", "📭 No customers are currently waiting in line.")
            return

        current_token = self.queue[self.front]
        messagebox.showinfo("Counter Announcement", f"🔔 NOW SERVING:\n\nToken #{current_token}\nPlease proceed to Counter 1.")
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX
        self.update_display()

    def update_display(self):
        for i in range(self.MAX):
            token = self.queue[i]
            label_text = "🪑\nEmpty"
            bg_color = "#e5e7eb"
            fg_color = "#6b7280"
            border_style = "groove"

            if token is not None:
                label_text = f"👤\nTOKEN\n#{token}"
                bg_color = "#fef3c7" 
                fg_color = "#b45309"
                border_style = "solid"

                if i == self.front and i == self.rear:
                    label_text += "\n(Front & Rear)"
                    bg_color = "#ddd6fe"
                    fg_color = "#6d28d9"
                elif i == self.front:
                    label_text += "\n(Next Up / Front)"
                    bg_color = "#d1fae5"
                    fg_color = "#065f46"
                elif i == self.rear:
                    label_text += "\n(Last In / Rear)"
                    bg_color = "#fee2e2"
                    fg_color = "#991b1b"

            self.chair_labels[i].config(text=label_text, bg=bg_color, fg=fg_color, relief=border_style)

        self.status_bar.config(
            text=f"System Active • Front Index: {self.front} | Rear Index: {self.rear} | Capacity: {self.MAX}"
        )

if __name__ == "__main__":
    window = tk.Tk()
    app = BankQueueGUI(window)
    window.mainloop()