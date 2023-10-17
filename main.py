import random
import tkinter as tk
import math

iter = 3
def submit():
    global iter
    iter = int(entry.get())
    result_label.config(text=f"Число итераций: {iter}")
def update_value(val):
    label.config(text=f"Значение r: {val:.2f}")
def build_mountains():
    global r
    canvas.delete("all")
    listik = list()
    h1 = random.randint(100, 400)
    h2 = random.randint(100, 400)
    print(h1, h2)
    xh1 = 6
    xh2 = 994
    canvas.create_oval(xh2 - 3, h2 - 3, xh2 + 3, h2 + 3, fill="red", outline='black', tags="point")
    listik.append([xh1, h1])
    listik.append([xh2, h2])
    for i in range(iter):
        for j in range(len(listik) - 1):
            l = math.sqrt((listik[j][0] - listik[j + 1][0]) ** 2 + (listik[j][1] - listik[j + 1][1]) ** 2)
            h = (listik[j][1] + listik[j + 1][1]) / 2 + random.randint(int(-r.get() * l), int(r.get() * l))
            if h > 600:
                h = 594
            if h < 0:
                h = 6
            x1 = (listik[j][0] + listik[j + 1][0]) / 2
            listik.append([x1, h])
            # canvas.create_line(listik[j] - 3, (h1 + h2) / 2 - 3, abs(xh1 + xh2) / 2 + 3, abs(h1 + h2) / 2 + 3)
        listik = sorted(listik, key=lambda x: (x[0], x[1]))
        # print(listik)
    for i in range(len(listik) - 1):
        canvas.create_line(listik[i][0], listik[i][1], listik[i + 1][0], listik[i + 1][1])
        canvas.create_oval(listik[i][0] - 3, listik[i][1] - 3, listik[i][0] + 3, listik[i][1] + 3, fill="green", outline='black', tags="point")
    canvas.create_oval(xh1 - 3, h1 - 3, xh1 + 3, h1 + 3, fill="red", outline='black', tags="point")
        # canvas.create_oval(x1 - 3, h - 3, x1 + 3, h + 3)
        # canvas.create_line(xh1, h1, (xh1 + xh2) / 2, h)
        # canvas.create_line(xh2, h2, (xh1 + xh2) / 2, h)
        # print(r.get())

            # l = math.sqrt((xh2 - xh1)**2 + (h2 - h1)**2)
            # h = (h1 + h2) / 2 + random.randint(int(-r.get() * l), int(r.get() * l))
            # x1 = (xh1 + xh2) / 2
            # # canvas.create_oval(abs(xh1 + xh2) / 2 - 3, (h1 + h2) / 2 - 3, abs(xh1 + xh2) / 2 + 3, abs(h1 + h2) / 2 + 3)
            # canvas.create_oval(x1 - 3, h - 3, x1 + 3, h + 3)
            # listik.append([x1, h])
            # canvas.create_line(xh1, h1, (xh1 + xh2) / 2, h)
            # canvas.create_line(xh2, h2, (xh1 + xh2) / 2, h)
            # print(r.get())

root = tk.Tk()
root.title("Лабораторная 5. Задание 2")

canvas = tk.Canvas(root, width=1000, height=600)
canvas.pack()

btn1 = tk.Button(root, text="Построить горы", command=build_mountains)
btn1.pack(side="right")

r = tk.DoubleVar()
r.set(0.4)

label = tk.Label(root, text="Значение r: 0.01")
label.pack(side="left")

scale = tk.Scale(root, from_=0, to=1.0, resolution=0.01, orient="horizontal", variable=r, command=lambda val: update_value(r.get()))
scale.pack(side="left")


entry = tk.Entry(root)
entry.pack(side="top")


submit_button = tk.Button(root, text="Подтвердить", command=submit)
submit_button.pack(side="top")

result_label = tk.Label(root, text=f"Число итераций: {iter}")
result_label.pack(side="top")

root.mainloop()
