import tkinter as tk
import tt_entails as tt

window = tk.Tk()

window.title("Truth Table App")
window.geometry("400x600")

def sat_walk():
    if not knowledge_base.get():
        pass
    else:
        result = tt.walk_sat(str(knowledge_base.get()) + ";")
        result_display = tk.Text(master=window, height=5, width=30, bg="azure")
        result_display.grid(column=0, row=4)
        result_display.insert(tk.END, result)


label = tk.Label(text="- : negation \n^ : and \nv : or \n=> : if ... then \n<=> : if and only if", justify="left")
label.grid(column=0, row=0)

label1 = tk.Label(text="Please enter knowledge base\n(clauses need to be seperated by commas)")
label1.grid(column=0, row=1)

knowledge_base = tk.Entry(bg="azure")
knowledge_base.grid(column=0, row=2)

result_sat = tk.Button(text="A model that satisfies given clauses are: ", command=sat_walk)
result_sat.grid(column=0, row=3)

window.mainloop()