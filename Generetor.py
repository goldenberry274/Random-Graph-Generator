import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx

def generate_graph():
    model = model_var.get()
    n = int(n_entry.get())
    p = float(p_entry.get())

    if model == "G(n, p) - Erdős–Rényi":
        G = nx.erdos_renyi_graph(n, p)
    elif model == "G(n, m) - Uniform":
        m = int(m_entry.get())
        G = nx.gnm_random_graph(n, m)
    else:
        return

    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray", node_size=500)
    plt.title(f"Random Graph: {model}")
    plt.show()

def update_fields(*args):
    if model_var.get() == "G(n, p) - Erdős–Rényi":
        m_label.grid_remove()
        m_entry.grid_remove()
    else:
        m_label.grid(row=4, column=0, sticky='w')
        m_entry.grid(row=4, column=1)

# GUI setup
root = tk.Tk()
root.title("Random Graph Generator")

model_var = tk.StringVar()
model_var.set("G(n, p) - Erdős–Rényi")
model_var.trace("w", update_fields)

ttk.Label(root, text="Graph Model:").grid(row=0, column=0, sticky='w')
model_menu = ttk.OptionMenu(root, model_var, "G(n, p) - Erdős–Rényi",
                            "G(n, p) - Erdős–Rényi", "G(n, m) - Uniform")
model_menu.grid(row=0, column=1)

ttk.Label(root, text="Number of vertices (n):").grid(row=1, column=0, sticky='w')
n_entry = ttk.Entry(root)
n_entry.insert(0, "10")
n_entry.grid(row=1, column=1)

ttk.Label(root, text="Probability (p):").grid(row=2, column=0, sticky='w')
p_entry = ttk.Entry(root)
p_entry.insert(0, "0.5")
p_entry.grid(row=2, column=1)

m_label = ttk.Label(root, text="Number of edges (m):")
m_entry = ttk.Entry(root)
m_entry.insert(0, "10")

ttk.Button(root, text="Generate Graph", command=generate_graph).grid(row=5, column=0, columnspan=2, pady=10)

update_fields()
root.mainloop()
