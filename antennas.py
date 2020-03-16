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
        self.init2DPlot(Plots)
        self.direc = self.getDirectivity(Plots)
        self.DtPat = self.initDirPlot()

    def init2DPlot(self, Plots):
        self.eRad2D = abs(((cos(Plots.len*pi*cos(Plots.theta2D)) - cos(Plots.len*pi))/sin(Plots.theta2D)))
        self.eRad2D = np.divide(self.eRad2D, np.amax(self.eRad2D))
        self.hRad2D = np.ones(Plots.theta2D.shape[0])

    def initDirPlot(self):
        return self.direc * self.eRad2D**2

    def update_2DPlot(self, Plots):
        if(Plots.simType == "Single Dipole"):
            self.eRad2D = abs(((cos(Plots.len*pi*cos(Plots.theta2D)) - cos(Plots.len*pi))/sin(Plots.theta2D)))
            self.hRad2D = np.ones(Plots.theta2D.shape[0])
        elif(Plots.simType == "Antenna Array"):
            if(Plots.arrType == "NoDip"):
                sigma = np.add (2 * pi * Plots.d * cos(Plots.theta2D), Plots.d_phi)
                N = Plots.numEle
                self.arrFact = (1 / N) * np.abs(np.divide(sin(N * sigma /2), sin(sigma / 2)))
                self.eRad2D = self.arrFact
            elif(Plots.arrType == "ColArray"):
                self.gamma = Plots.theta2D
                self.antPat = abs(((cos(Plots.len*pi*cos(Plots.theta2D)) - cos(Plots.len*pi))/sin(Plots.theta2D)))
                self.antPat = np.divide(self.antPat, np.amax(self.antPat))
                sigma = np.add (2 * pi * Plots.d * cos(self.gamma), Plots.d_phi)
                N = Plots.numEle
                self.arrFact = (1 / N) * np.abs(np.divide(sin(N * sigma /2), sin(sigma / 2)))
                self.eRad2D = np.multiply(self.antPat, self.arrFact)
                self.hRad2D = np.ones(Plots.theta2D.shape[0])
            elif(Plots.arrType == "PerpArray"):
                self.gamma = Plots.theta2D
                sigma = np.add (2 * pi * Plots.d * cos(self.gamma), Plots.d_phi)
                N = Plots.numEle
                self.arrFact = (1 / N) * np.abs(np.divide(sin(N * sigma /2), sin(sigma / 2)))
                self.antPat = abs(((cos(Plots.len*pi*cos(Plots.theta2D - pi / 2)) - cos(Plots.len*pi))/sin(Plots.theta2D - pi / 2)))
                self.antPat = np.divide(self.antPat, np.amax(self.antPat))
                self.eRad2D = np.multiply(self.antPat, self.arrFact)
                self.hRad2D = self.arrFact
        self.hRad2D = np.divide(self.hRad2D, np.max(self.hRad2D))
        self.eRad2D = np.divide(self.eRad2D, np.amax(self.eRad2D))
        self.direc = self.getDirectivity(Plots)
        self.DtPat = self.direc * self.eRad2D**2

    def getDirectivity(self, Plots):
        I = integrate.cumtrapz(self.eRad2D[5000:len(self.eRad2D)] ** 2 * sin(Plots.theta2D[5000:len(Plots.theta2D)]),Plots.theta2D[5000:len(Plots.theta2D)], initial=0)
        return round((2 / I[len(I)-1]), 2)

    def init_3DPlot(self, Plots):
        if(Plots.simType == "Single Dipole"):
            self.antPat3D = ((cos(Plots.len*pi*cos(Plots.THETA)) - cos(Plots.len*pi))/sin(Plots.THETA))
            self.antPat3D = np.divide(self.antPat3D, np.amax(self.antPat3D))
            self.rad3D = self.antPat3D
        elif(Plots.simType == "Antenna Array"):
            if(Plots.arrType == "NoDip"):
                sigma = np.add (2 * pi * Plots.d * cos(Plots.gamma3D), Plots.d_phi)
                N = Plots.numEle
                self.arrFact3D = (1 / N) * np.abs(np.divide(sin(N * sigma /2), sin(sigma / 2)))
                self.rad3D = np.divide(self.arrFact3D,np.max(self.arrFact3D))
            elif(Plots.arrType == "ColArray"):

                sigma = np.add (2 * pi * Plots.d * cos(Plots.gamma3D), Plots.d_phi)
                N = Plots.numEle
                self.arrFact3D = (1 / N) * np.abs(np.divide(sin(N * sigma /2), sin(sigma / 2)))

                self.antPat3D = ((cos(Plots.len*pi*cos(Plots.gamma3D)) - cos(Plots.len*pi))/sin(Plots.gamma3D))
                self.antPat3D = np.divide(self.antPat3D, np.amax(self.antPat3D))

                self.rad3D = np.multiply(self.antPat3D, self.arrFact3D)
            elif(Plots.arrType == "PerpArray"):

                sigma = np.add (2 * pi * Plots.d * cos(Plots.gamma3D), Plots.d_phi)
                N = Plots.numEle
                self.arrFact3D = (1 / N) * np.abs(np.divide(sin(N * sigma /2), sin(sigma / 2)))

                self.antPat3D = ((cos(Plots.len*pi*cos(Plots.gamma3D)) - cos(Plots.len*pi))/sin(Plots.gamma3D))
                self.antPat3D = np.divide(self.antPat3D, np.amax(self.antPat3D))

                self.rad3D = np.multiply(self.antPat3D, self.arrFact3D)
