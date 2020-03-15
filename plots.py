# -*- coding: utf-8 -*-
"""
Plots Module for Antenna Simulator
Created on Fri Feb 28 14:36:18 2020

Author: Jordan Baxter
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from matplotlib.figure import Figure
import antennas as ant
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

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
        self.subplots_adjust(left=0, right=1,top=0.9, bottom=0.05, wspace=0.05, hspace=0.3)
        ### FORMAT PLOTS ###
        self.ax.set_rmin(0)
        self.ax.set_theta_direction(-1)
        self.ax.set_theta_zero_location("N")
        self.ax.set_rlabel_position(180)
        self.ax.set_title("Normalized Radiation Pattern (Polar)", pad=10)
        

        self.bx.set_xlim(-pi,pi)
        self.bx.set_ylim(0,1.1)
        self.bx.set_title("Normalized Radiation Pattern (Linear)", pad=10)
        

        self.d_ticks = np.linspace(0, 10, 21)
        self.cx.set_theta_direction(-1)
        self.cx.set_theta_zero_location("N")
        self.cx.set_rmin(0)
        self.cx.set_rlabel_position(180)
        self.cx.set_rticks(self.d_ticks)
        self.cx.set_title("Antenna Directivity (Polar)", pad=10)

        self.dx.set_xlim(-pi,pi)
        self.dx.set_title("Antenna Directivity (Linear)", pad=10)

        ### SET INITIAL ANTENNA PARAMETERS ###
        self.theta2D = np.linspace(-pi, pi, 10000)
        self.theta3D = np.linspace(0.0000000000001, pi, 40)
        self.phi3D = np.linspace(-pi, pi, 40)
        self.THETA, self.PHI = np.meshgrid(self.theta3D, self.phi3D)
        self.numEle = 2
        self.simType = "Single Dipole"
        self.arrType = "NoDip"
        self.d_phi = float(0)
        self.d = float(0.0000001)
        self.len = float(0.0000001)
        self.plot3D = False
        self.antProf = ant.AntennaProfile(self)
        self.init_2Dplots()
        

    
    def init_2Dplots(self):
        self.ax.plot(self.theta2D, self.antProf.eRad2D,'b', label="E-Plane")
        self.bx.plot(self.theta2D, self.antProf.eRad2D,'b', label="E-Plane")
        self.ax.plot(self.theta2D, self.antProf.hRad2D,'g', label="H-Plane")
        self.bx.plot(self.theta2D, self.antProf.hRad2D,'g', label="H-Plane")
        self.cx.plot(self.theta2D, self.antProf.DtPat,'b')
        self.dx.plot(self.theta2D, self.antProf.DtPat,'b')
        self.ax.legend(loc='upper right')
        self.cx.set_rmax(int(self.antProf.direc) + 1)
        self.dx.set_ylim(0, int(self.antProf.direc) + 1)
        self.bx.legend(loc='upper right')
    
    def init_3Dplot(self):
        self.antProf.init_3DPlot(self)
        self.X = self.antProf.rad3D * np.sin(self.THETA) * np.cos(self.PHI)
        self.Y = self.antProf.rad3D * np.sin(self.THETA) * np.sin(self.PHI)
        self.Z = self.antProf.rad3D * np.cos(self.THETA)
        self.ex.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
        linewidth=0, antialiased=False, alpha=0.5)

    def update_plots(self):
        if(self.plot3D):
            self.antProf.init_3DPlot(self)
            del self.ex.lines[0:len(self.ex.lines)]
            self.X = self.antProf.rad3D * np.sin(self.THETA) * np.cos(self.PHI)
            self.Y = self.antProf.rad3D * np.sin(self.THETA) * np.sin(self.PHI)
            self.Z = self.antProf.rad3D * np.cos(self.THETA)
            self.ex.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
            linewidth=0, antialiased=False, alpha=0.5)
        else:
            self.antProf.update_2DPlot(self)
            del self.ax.lines[0:len(self.ax.lines)]
            del self.bx.lines[0:len(self.bx.lines)]
            del self.cx.lines[0:len(self.cx.lines)]
            del self.dx.lines[0:len(self.dx.lines)]
            self.ax.plot(self.theta2D, self.antProf.eRad2D,'b', label="E-Plane")
            self.bx.plot(self.theta2D, self.antProf.eRad2D,'b', label="E-Plane")
            self.ax.plot(self.theta2D, self.antProf.hRad2D,'g', label="H-Plane")
            self.bx.plot(self.theta2D, self.antProf.hRad2D,'g', label="H-Plane")
            self.cx.plot(self.theta2D, self.antProf.DtPat,'b')
            self.dx.plot(self.theta2D, self.antProf.DtPat,'b')
            self.ax.legend(loc='upper right')
            self.cx.set_rmax(int(self.antProf.direc) + 1)
            self.dx.set_ylim(0, int(self.antProf.direc) + 1)
            self.bx.legend(loc='upper right')
    
    def setDPhi(self, newDPhi):
        self.d_phi = float(newDPhi)
        self.update_plots()
    
    def setD(self, newD):
        self.d = float(newD)
        if(self.d == 0):
            self.d = 0.0001
        self.update_plots()
    
    def setL(self, newLen):
        self.len = float(newLen)
        self.update_plots()
    
    def setSimType(self, newtype):
        self.simType = newtype
        self.update_plots()
    
    def setArrType(self, newtype):
        self.arrType = newtype
        self.update_plots()
    
    def setNumEle(self, newNumEle):
        self.numEle = int(newNumEle)
        self.update_plots()
        
    def toggle3D(self):
        self.plot3D = not self.plot3D
        if(self.plot3D == True):
            self.ax.axis('off')
            self.bx.axis('off')
            self.cx.axis('off')
            self.dx.axis('off')
            self.ex = self.add_subplot(111, projection='3d')
            self.init_3Dplot()
        else:
            self.ax.axis('on')
            self.bx.axis('on')
            self.cx.axis('on')
            self.dx.axis('on')
            self.ex.remove()
        return self.plot3D 
        

    
