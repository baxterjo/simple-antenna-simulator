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
        self.simType.set("Single Antenna")
        
        self.simTypeMenu = tk.OptionMenu(self.w_frame, 
                                         self.simType, 
                                         "Single Antenna", 
                                         "Antenna Array", 
                                         command=self.changeSim)
        self.simTypeMenu.grid(row=0,
                              columnspan=2)
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
                              from_=0.01, 
                              to=1.75, 
                              resolution=0.01,
                              length=300,
                              orient='horizontal',
                              tickinterval=0.25,
                              command=self.upL,
                              label="Length of Dipole [l / \u03bb]")
        self.l_sc.grid(row=2,
                       columnspan=2)
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
        
        ### GAMMA TO THETA RELATIONSHIP SLIDER ###
        self.gt_sc = tk.Scale(self.w_frame, 
                              from_=0, 
                              to=90, 
                              resolution=1,
                              length=300,
                              orient='horizontal',
                              tickinterval=0.25,
                              command=self.upL,
                              label="Gamma Theta Relationship [degs]")
        ### /GAMMA TO THETA RELATIONSHIP SLIDER ###
        
        ### INSERT DIPOLE CHECKBOX ###
        self.insDipVar = tk.BooleanVar()
        self.insDip_but = tk.Checkbutton(self.w_frame,
                                         text="Insert Dipole",
                                         command=self.insDip,
                                         var=self.insDipVar,
                                         onvalue=True,
                                         offvalue=False)
        ### /INSERT DIPOLE CHECKBOX ###
        
        ### Toggle 3D Button ###
        self.button3D = tk.Button(self.w_frame, 
                                  text="Show 3D Plot", fg="green",
                                  command=self.up3D)
        self.button3D.grid(row=1,
                           column=0)
        
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
        self.plots.toggle3D()
        self.canvas.draw()
        
    def insDip(self):
        if(self.insDipVar.get() == True):
            self.plots.dipole = True
            self.l_sc.grid(row=4,
                            columnspan=2)
        else:
            self.plots.dipole = False
            self.l_sc.grid_forget()
        self.canvas.draw()
        
    def changeSim(self, value):
        simType = self.simType.get()
        if(simType == "Single Antenna"):
            self.dp_sc.grid_forget()
            self.d_sc.grid_forget()
            self.gt_sc.grid_forget()
            self.insDip_but.deselect()
            self.insDip_but.invoke()
            self.insDip_but.grid_forget()
            self.l_sc.grid(row=2,
                           columnspan=2)
            self.plots.dipole = True
            self.plots.antArray = False
            self.plots.update_plots()
        elif(simType == "Antenna Array"):
            self.plots.dipole = False
            self.plots.antArray = True
            self.l_sc.grid_forget()
            self.insDip_but.grid(row=1,
                                 column=1)
            self.d_sc.grid(row=2,
                           columnspan=2)
            self.dp_sc.grid(row=3,
                            columnspan=2)
            self.plots.update_plots()
            
            
        

### Constuct Figures ###


root = tk.Tk()
app = Application(master=root)
app.mainloop()
