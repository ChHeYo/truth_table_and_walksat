from tkinter import *
import tt_entails as tt


def sat_walk():
    if not knowledge_base.get():
        pass
    else:
        result = tt.walk_sat(str(knowledge_base.get()) + ";")
        if result:
            result_display.delete(0, 'end')
            result_display.insert(0, result)
        else:
            result_display.delete(0, 'end')
            result_display.insert(0, "No model found") 


window = Tk()

window.title("Truth Table App")
window.geometry("400x400")
window.resizable(width=False, height=False)

frame = Frame(window)

strVal = StringVar()
result = StringVar()

# label = tk.Label(frame, text="- : negation \n^ : and \nv : or \n=> : if ... then \n<=> : if and only if", justify="left")
# label.grid(row=0)

label1 = Label(frame, text="Please enter knowledge base\n(clauses need to be seperated by commas)")
label1.grid(row=0, pady=(30, 10))

knowledge_base = Entry(frame, bg="azure", textvariable=strVal)
knowledge_base.grid(row=1, pady=(10, 10))

result_sat = Button(frame, text="Show", command=sat_walk)
result_sat.grid(row=2, pady=(10, 40))

result_display = Entry(frame, bg="azure", textvariable=result)
result_display.grid(row=3)

frame.pack()

window.mainloop()