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
        self.eRad3D = self.init3DPlot(Plots.theta3D, Plots.phi3D, Plots.len)
        self.direc = self.getDirectivity(Plots)
        self.DtPat = self.initDirPlot()
        
    def init2DPlot(self, theta2D, l):
        return abs(((cos(l*pi*cos(theta2D)) - cos(l*pi))/sin(theta2D))/(1-cos(l*pi)))

    def initDirPlot(self):
        return self.direc * self.eRad2D**2
    
    def init3DPlot(self, theta3D, phi3D, len):
        #TODO
        return 1

    def update_2DPlot(self, Plots):
        if(Plots.dipole): 
            self.antPat = abs(((cos(Plots.len*pi*cos(Plots.theta2D)) - cos(Plots.len*pi))/sin(Plots.theta2D)))
            self.antPat = np.divide(self.antPat, np.amax(self.antPat))
        if(Plots.antArray): self.arrFact = 1
        if(Plots.antArray and Plots.dipole):
            self.eRad2D = np.multiply(self.antPat, self.arrFact)
        elif(Plots.dipole):
            self.eRad2D = self.antPat
        elif(Plots.antArray):
            self.eRad2D = self.arrFact
        self.direc = self.getDirectivity(Plots)
        self.DtPat = self.direc * self.eRad2D**2

    def getDirectivity(self, Plots):
        FI = ((cos(Plots.len*pi*cos(Plots.d_theta)) - cos(Plots.len*pi))/sin(Plots.d_theta))/(1-cos(Plots.len*pi))
        I = integrate.cumtrapz(FI ** 2 * sin(Plots.d_theta), Plots.d_theta, initial=0)
        return 2 / I[9999]

    def update_3DPlot(self):
        #TODO
        return 1
    
    
