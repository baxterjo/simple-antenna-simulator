# -*- coding: utf-8 -*-
"""
Antenna Visualizer
Created on Thu Feb 27 18:05:13 2020

Description: A GUI based antenna simulator. Tweak sliders to adjust antenna parameters such as length, array patterns, and excitation phasing.

Authors:
    Jordan Baxter
    Chelsea Starr
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import plots

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("GUI Based Antenna Simulation")
        self.pack()
        self.create_frames()
        self.create_widgets()
        
        
    def create_frames(self):
        self.p_frame = tk.Frame(self.master)
        self.p_frame.pack(side = 'left')
        self.w_frame = tk.Frame(self.master)
        self.w_frame.pack(side = 'right')
        self.plots = plots.Plots(figsize=(11,9), dpi=75)
        self.canvas = FigureCanvasTkAgg(self.plots, master=self.p_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
       

    def create_widgets(self):
        
        ### DROPDOWN OPTIONS MENU ###
        self.simType = tk.StringVar()
        self.simType.set("Single Dipole")
        
        self.simTypeMenu = tk.OptionMenu(self.w_frame, 
                                         self.simType, 
                                         "Single Dipole", 
                                         "Antenna Array", 
                                         command=self.updateControls)
        self.simTypeMenu.grid(row=0,
                              column=1,
                              columnspan=2)
        tk.Label(self.w_frame, text="Simulation Type").grid(row=0, column=0)
        ### DROPDOWN OPTIONS MENU ###
        
        ### DELTA PHI SLIDER ###
        self.dp_sc = tk.Scale(self.w_frame, 
                              from_=0, 
                              to=2, 
                              resolution=0.01,
                              length=300,
                              orient='horizontal',
                              tickinterval=0.25,
                              command=self.upDPhi,
                              label="Excitation Phasing [\u0394\u03c6 / \u03bb]")
        ### /DELTA PHI SLIDER ###
        
        
        ### D SLIDER ###
        self.d_sc = tk.Scale(self.w_frame, 
                              from_=0, 
                              to=2, 
                              resolution=0.01,
                              length=300,
                              orient='horizontal',
                              tickinterval=0.25,
                              command=self.upD,
                              label="Distance Between Elements [d / \u03bb]")
        ### /D SLIDER ###
        
        ### L SLIDER ###
        self.l_sc = tk.Scale(self.w_frame, 
                              from_=0, 
                              to=1.75, 
                              resolution=0.01,
                              length=300,
                              orient='horizontal',
                              tickinterval=0.25,
                              command=self.upL,
                              label="Length of Dipole [l / \u03bb]")
        self.l_sc.grid(row=2,
                       columnspan=3)
        ### /L SLIDER ###

        ### NUMBER OF ELEMENTS SLIDER ###
        self.dp_sc = tk.Scale(self.w_frame, 
                              from_=1, 
                              to=20, 
                              resolution=1,
                              length=300,
                              orient='horizontal',
                              tickinterval=5,
                              command=self.upNumEle,
                              label="Number of Elements")
        ### /NUMBER OF ELEMENTS SLIDER ###
        
        ### INSERT DIPOLE CHECKBOX ###
        self.insDipVar = tk.IntVar()
        self.insDipVar.set(1)

        self.noDip = tk.Radiobutton(self.w_frame,text="No Dipole", variable=self.insDipVar, value=1, command=self.insDip)
        self.coLin = tk.Radiobutton(self.w_frame, text="Colinear Array", variable=self.insDipVar, value=2, command=self.insDip)
        self.perp = tk.Radiobutton(self.w_frame, text="Perpendicular Array", variable=self.insDipVar, value=3, command=self.insDip)
        ### /INSERT DIPOLE CHECKBOX ###
        
        ### Toggle 3D Button ###
        self.button3D = tk.Button(self.w_frame, 
                                  text="Show 3D Plot", fg="green",
                                  command=self.up3D)
        self.button3D.grid(row=1,
                            column=1,
                            columnspan=2)
        
        ### QUIT BUTTON ###
        self.quit = tk.Button(self.master, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def upNumEle(self, slidevalue):
        self.plots.setNumEle(slidevalue)
        self.canvas.draw()

    def upDPhi(self, slidevalue):
        self.plots.setDPhi(slidevalue)
        self.canvas.draw()
        
    def upD(self, slidevalue):
        self.plots.setD(slidevalue)
        self.canvas.draw()
    
    def upL(self, slidevalue):
        self.plots.setL(slidevalue)
        self.canvas.draw()
        
    def up3D(self):
        if (self.plots.toggle3D() == True):
            self.toggleWidgets("off")
        else:
            self.toggleWidgets("on")
        self.canvas.draw()
        
    def insDip(self):
        arrType = self.insDipVar.get()
        if(arrType == 1):
            self.l_sc.grid_forget()
            self.plots.setArrType("NoDip")
        elif(arrType == 2):
            self.l_sc.grid(row=4,
                            columnspan=3)
            self.plots.setArrType("ColArray")
        elif(arrType == 3):
            self.l_sc.grid(row=4,
                            columnspan=3)
            self.plots.setArrType("PerpArray")
        self.canvas.draw()
        
    def updateControls(self, value):
        simType = self.simType.get()
        if(simType == "Single Antenna"):
            self.dp_sc.grid_forget()
            self.d_sc.grid_forget()
            self.noDip.grid_forget()
            self.coLin.grid_forget()
            self.perp.grid_forget()
            self.insDipVar.set(1)
            self.l_sc.grid(row=2,
                           columnspan=3)
        elif(simType == "Antenna Array"):
            self.l_sc.grid_forget()
            self.d_sc.grid(row=2,
                           columnspan=3)
            self.dp_sc.grid(row=3,
                            columnspan=3)
            self.noDip.grid(row=4,
                            column=0)
            self.coLin.grid(row=4,
                            column=1)
            self.perp.grid(row=4,
                            column=2)   
        self.plots.setSimType(simType)
        self.canvas.draw()
        

    def toggleWidgets(self,onOff='on'):
        if(onOff == "off"):
            self.dp_sc.configure(state='disabled')
            self.d_sc.configure(state='disabled')
            self.noDip.configure(state='disabled')
            self.l_sc.configure(state='disabled')
            self.simTypeMenu.configure(state='disabled')
        else:
            self.dp_sc.configure(state='normal')
            self.d_sc.configure(state='normal')
            self.noDip.configure(state='normal')
            self.l_sc.configure(state='normal')
            self.simTypeMenu.configure(state='normal')
            
            
        

### Constuct Figures ###


root = tk.Tk()
app = Application(master=root)
app.mainloop()
