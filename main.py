import tkinter as tk

root = tk.Tk()

root.title('Chemical Solution')
root.geometry('400x250')
root.resizable(width=False, height=False)

# Molar mass
l_molar_mass = tk.Label(root, text='Molar mass')
l_molar_mass.place(x=5, y=5)
e_molar_mass = tk.Entry(root, width=7)
e_molar_mass.place(x=5, y=30)
l_molar_mass_unit = tk.Label(root, text='g/mol')
l_molar_mass_unit.place(x=70, y=30)

# concentration
l_concentration = tk.Label(root, text='Concentration')
l_concentration.place(x=5, y=60)
e_concentration = tk.Entry(root, width=7)
e_concentration.place(x=5, y=85)
l_concentration_unit = tk.Label(root, text='mol/l')
l_concentration_unit.place(x=70, y=85)

# volume
l_volume = tk.Label(root, text='Final volume')
l_volume.place(x=200, y=5)
volume = tk.StringVar()
s_volume250 = tk.Radiobutton(root, text='250 ml', variable=volume, value=0.25)
s_volume250.place(x=200, y=30)
s_volume500 = tk.Radiobutton(root, text='500 ml', variable=volume, value=0.5)
s_volume500.place(x=200, y=55)
s_volume750 = tk.Radiobutton(root, text='750 ml', variable=volume, value=0.75)
s_volume750.place(x=200, y=80)
s_volume1000 = tk.Radiobutton(root, text='1000 ml', variable=volume, value=1)
s_volume1000.place(x=200, y=105)


def calculate():
    molar_mass = e_molar_mass.get()
    if ',' in molar_mass:
        molar_mass = molar_mass.replace(',', '.')
    concentration = e_concentration.get()
    if ',' in concentration:
        concentration = concentration.replace(',', '.')
    result_mass = float(molar_mass) * float(volume.get()) * float(concentration)
    label = tk.Label(root, text=round(result_mass, 3), width=10, height=1)
    label.place(x=240, y=162)


b_calc = tk.Button(root, text='Execute calculation', width=15, height=2, command=calculate)
b_calc.place(x=20, y=150)
l_calc_result = tk.Label(root, text='Weight:', width=7, height=1)
l_calc_result.place(x=170, y=162)
l_calc_unit = tk.Label(root, text='g', width=1, height=1)
l_calc_unit.place(x=340, y=162)

root.mainloop()
