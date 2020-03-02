# -*- coding: utf-8 -*-
"""
Plots Module for Antenna Simulator
Created on Fri Feb 28 14:36:18 2020

Author: Jordan Baxter
"""
import matplotlib as mlp
import numpy as np
from numpy import pi
from matplotlib.figure import Figure
import antennas as ant

### Create Plot Class ###
class Plots(Figure):
    def __init__(self, figsize=None, dpi=None):
        super().__init__(figsize,dpi)
        self.figsize = figsize
        ### CREATE PLOTS ###
        self.ax = self.add_subplot(221, polar=True)
        self.bx = self.add_subplot(222)
        self.cx = self.add_subplot(223, polar=True)
        self.dx = self.add_subplot(224)
        self.ex = self.add_subplot(111)
        self.ex.axis('off')
        self.subplots_adjust(left=0, right=1,top=0.9, bottom=0.05, wspace=0.05, hspace=0.3)
        ### FORMAT PLOTS ###
        self.ax.set_rmin(0)
        self.ax.set_rmax(1)
        self.ax.set_title("Normalized Radiation Pattern (Polar)", pad=10)
        self.ax.legend()

        self.bx.set_xlim(-pi,pi)
        self.bx.set_ylim(0,1)
        self.bx.set_title("Normalized Radiation Pattern (Linear)", pad=10)
        self.bx.legend()

        self.cx.set_rmin(0)
        self.cx.set_title("Antenna Directivity (Polar)", pad=10)

        self.dx.set_xlim(-pi,pi)
        self.dx.set_title("Antenna Directivity (Linear)", pad=10)

        ### SET INITIAL ANTENNA PARAMETERS ###
        self.theta2D = np.linspace(-pi, pi, 1000)
        self.theta3D = np.linspace(0.0000000000001, pi, 200)
        self.phi3D = np.linspace(-pi, pi, 200)
        self.d_theta = np.linspace(0.00000000001,pi,10000)
        self.numEle = 1
        self.gammTheRel = 0
        self.dipole = True
        self.antArray = False
        self.d_phi = float(0)
        self.d = float(0)
        self.len = float(0.0000001)
        self.plot3D = False
        self.antProf = ant.AntennaProfile(self)
        self.init_2Dplots()

    
    def init_2Dplots(self):
        self.ax.plot(self.theta2D, self.antProf.eRad2D,'b')
        self.bx.plot(self.theta2D, self.antProf.eRad2D,'b')
        self.cx.plot(self.theta2D, self.antProf.DtPat,'b')
        self.dx.plot(self.theta2D, self.antProf.DtPat,'b')
        dmax = np.amax(self.antProf.DtPat)
        self.cx.set_rmax(int(dmax) + 1)
        self.dx.set_ylim(0, int(dmax) + 1)
    
    def init_3Dplots(self):
        #TODO
        return 1
        
    def update_plots(self):
        if(self.plot3D):
            self.antProf.update_3DPlot()
        else:
            self.antProf.update_2DPlot(self)
            del self.ax.lines[0:len(self.ax.lines)]
            del self.bx.lines[0:len(self.bx.lines)]
            del self.cx.lines[0:len(self.cx.lines)]
            del self.dx.lines[0:len(self.dx.lines)]
            self.ax.plot(self.theta2D, self.antProf.eRad2D,'b')
            self.bx.plot(self.theta2D, self.antProf.eRad2D,'b')
            self.cx.plot(self.theta2D, self.antProf.DtPat,'b')
            self.dx.plot(self.theta2D, self.antProf.DtPat,'b')
            dmax = np.amax(self.antProf.DtPat)
            self.cx.set_rmax(int(dmax) + 1)
            self.dx.set_ylim(0, int(dmax) + 1)
    
    def setDPhi(self, newDPhi):
        self.d_phi = float(newDPhi)
        self.update_plots()
    
    def setD(self, newD):
        self.d = float(newD)
        self.update_plots()
    
    def setL(self, newLen):
        self.len = float(newLen)
        self.update_plots()
    
    def toggleDip(self):
        self.dipole = not self.dipole
        self.update_plots()
    
    def setNumEle(self, newNumEle):
        self.numEle = newNumEle
        self.update_plots()
        
    def toggle3D(self):
        self.plot3D = not self.plot3D
        if(self.plot3D == True):
            self.ax.axis('off')
            self.bx.axis('off')
            self.cx.axis('off')
            self.dx.axis('off')
            self.ex.axis('on')
        else:
            self.ax.axis('on')
            self.bx.axis('on')
            self.cx.axis('on')
            self.dx.axis('on')
            self.ex.axis('off') 
        

    
