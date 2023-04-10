from tkinter import * 
import sympy as sp

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

window = Tk()
window.title = 'SIR Model Simulator'

inputsFrame = Frame(padx=20, pady=30)
eqFrame = Frame(padx=20, pady=30)

lbl_inputs = Label(inputsFrame, text = "INPUTS")
lbl_S0 = Label(inputsFrame, text = "S(0): ")
lbl_I0 = Label(inputsFrame, text = "I(0): ")
lbl_constantA = Label(inputsFrame, text = "constant a: ")
lbl_constantC = Label(inputsFrame, text = "constant c: ")
lbl_constantSigma = Label(inputsFrame, text = "constant σ: ")
lbl_varTime = Label(inputsFrame, text = "Simulate at t=")

lbl_inputs.grid(row=0, column=0, sticky="W")
lbl_S0.grid(row=1, column=0, sticky="E")
lbl_I0.grid(row=2, column=0, sticky="E")
lbl_constantA.grid(row=3, column=0, sticky="E")
lbl_constantC.grid(row=4, column=0, sticky="E")
lbl_constantSigma.grid(row=5, column=0, sticky="E")
lbl_varTime.grid(row=6, column=0, sticky="E", pady=10)

ent_S0 = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_I0 = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_constantA = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_constantC = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_constantSigma = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_varTime = Entry(inputsFrame, width=10, bg="white", fg="black")

ent_S0.grid(row=1, column=1, sticky="W")
ent_I0.grid(row=2, column=1, sticky="W")
ent_constantA.grid(row=3, column=1, sticky="W")
ent_constantC.grid(row=4, column=1, sticky="W")
ent_constantSigma.grid(row=5, column=1, sticky="W")
ent_varTime.grid(row=6, column=1, sticky="E", pady=10)

s0 = 0
i0 = 0
constantA = 0
constantC = 0
constantSigma = 0
varTime = 0

already_simulated = False

def simulate_on_click():

    global already_simulated
    if already_simulated == True: 
        for widget in eqFrame.winfo_children():
            widget.destroy()
    
    s0 = int(ent_S0.get())
    i0 = int(ent_I0.get())
    constantA = int(ent_constantA.get())
    constantC = int(ent_constantC.get())
    constantSigma = int(ent_constantSigma.get())
    varTime = int(ent_varTime.get())

    S = sp.Symbol('S')
    I = sp.Symbol('I')
    R = sp.Symbol('R')
    a = sp.Symbol('a')
    c = sp.Symbol('c')
    σ = sp.Symbol('σ')

    rateOfSus = sp.Eq(S, -constantA*constantC*S*I)
    rateOfInf = sp.Eq(I, constantA*constantC*S*I-constantSigma*I)
    rateOfRec = sp.Eq(R, constantSigma*I)

    lbl_susRate = Label(eqFrame, text = "S(0)=" + str(rateOfSus))
    lbl_infRate = Label(eqFrame, text = "I(0)=" + str(rateOfInf))
    lbl_recRate = Label(eqFrame, text = "R(0)=" + str(rateOfRec))

    lbl_susRate.pack()
    lbl_infRate.pack()
    lbl_recRate.pack()

    already_simulated = True

btn_compute = Button(inputsFrame, text = "Simulate SIR Model", command = simulate_on_click)
btn_compute.grid(row=7, column=0, columnspan=2)

inputsFrame.pack(side=LEFT)
eqFrame.pack(side=TOP)

window.mainloop()