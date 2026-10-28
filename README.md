
# 🏦 NexusBank™ - Circular Queue Management Dashboard

A desktop graphical user interface (GUI) application built for a University Data Structures & Algorithms (DSA) lab project. This project demonstrates the practical implementation of a **Circular Queue** data structure using Python and Tkinter.

---

## 🚀 Features & Algorithm Logic

- **Circular Queue Architecture:** Fixed-size memory buffer (Capacity: 5 waiting lounge slots) implementing modular arithmetic `(rear + 1) % MAX` to optimize space utilization.
- **Dynamic Visualizer UI:** Color-coded chair status updates reflecting real-time backend state changes (`Front`, `Rear`, `Empty`, or `Occupied`).
- **Interactive Controls:**
  - **Issue One Token:** Enqueues a customer token into the next available circular slot.
  - **Call Next Customer:** Dequeues the customer at the `Front` pointer and sends them to the service counter.
  - **Bulk Fill Lounge:** Stress-tests the circular queue overflow handling by filling all slots simultaneously.
- **Diagnostic Status Bar:** Real-time pointer tracking displaying active memory indices (`front` and `rear`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **GUI Library:** Tkinter (Built-in standard Python GUI package)

---

## 🏃‍♂️ How to Run Locally

1. Make sure you have Python installed on your system.
2. Clone or download this repository.
3. Open your terminal or command prompt inside the project folder and run:
   ```bash
   python main.py
   ```
