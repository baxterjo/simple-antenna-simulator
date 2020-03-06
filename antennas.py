# -*- coding: utf-8 -*-
"""
Antenna Module for Antenna Simulator

Author: Jordan Baxter
"""

import numpy as np
from numpy import pi, cos, sin, tan
from scipy import integrate

class AntennaProfile():
    def __init__(self, Plots):
        self.eRad2D = self.init2DPlot(Plots.theta2D, Plots.len)
        self.direc = self.getDirectivity(Plots)
        self.DtPat = self.initDirPlot()
        
    def init2DPlot(self, theta2D, l):
        return abs(((cos(l*pi*cos(theta2D)) - cos(l*pi))/sin(theta2D))/(1-cos(l*pi)))

    def initDirPlot(self):
        return self.direc * self.eRad2D**2

    def update_2DPlot(self, Plots):
        if(Plots.simType == "Single Dipole"): 
            self.antPat = abs(((cos(Plots.len*pi*cos(Plots.theta2D)) - cos(Plots.len*pi))/sin(Plots.theta2D)))
            self.antPat = np.divide(self.antPat, np.amax(self.antPat))
<<<<<<< HEAD
        elif(Plots.simType == "Antenna Array"): 
            self.arrFact = np.ones(Plots.theta2D.shape()[0])
            if(Plots.arrType == "NoDip"):
                self.eRad2D = self.arrFact
            elif(Plots.dipole):
                self.eRad2D = self.antPat
            elif(Plots.antArray):
                self.eRad2D = self.arrFact
        self.direc = self.getDirectivity(Plots)
=======
        if(Plots.antArray): 
            #TODO: Antenna array functions.
            self.arrFact = 1
        if(Plots.antArray and Plots.dipole):
            self.eRad2D = np.multiply(self.antPat, self.arrFact)
        elif(Plots.dipole):
            self.eRad2D = self.antPat
        elif(Plots.antArray):
            self.eRad2D = self.arrFact
        self.direc = self.getDirectivity(Plots) #TODO: Array factor directivity.
>>>>>>> 9fd7cbb9890afb79850b38933058c1b3503d0fb9
        self.DtPat = self.direc * self.eRad2D**2

    def getDirectivity(self, Plots):
        FI = ((cos(Plots.len*pi*cos(Plots.d_theta)) - cos(Plots.len*pi))/sin(Plots.d_theta))/(1-cos(Plots.len*pi))
        #TODO: Use high resolution variables in eradpat
        I = integrate.cumtrapz(FI ** 2 * sin(Plots.d_theta), Plots.d_theta, initial=0)
        return 2 / I[9999]

    def init_3DPlot(self, Plots):
        if(Plots.dipole): 
            self.antPat3D = ((cos(Plots.len*pi*cos(Plots.THETA)) - cos(Plots.len*pi))/sin(Plots.THETA))
            self.antPat3D = np.divide(self.antPat3D, np.amax(self.antPat3D))
        if(Plots.antArray): self.arrFact3D = 1 #TODO: Array functionality for 3d plot.
        if(Plots.antArray and Plots.dipole):
            self.rad3D = np.multiply(self.antPat3D, self.arrFact3D)
        elif(Plots.dipole):
            self.rad3D = self.antPat3D
        elif(Plots.antArray):
            self.rad3D = self.arrFact3D
    
    
