# simple-antenna-simulator
A simple GUI based antenna simulator built with python.

# Dependancies
When finished there should be three seperate executables in /Apps directory, one for windows, one for linux, and one for MAC. These are stand alone programs and do not require any additional software to execute.


To be able to run the source code the following must be installed:
- Python (Version 3.8.2 or newer are the only tested versions)
- Special Python Packages Include:
    - tkinter
    - numpy
    - scipy
    - matplotlib

# How to use
Double click on the application to run it, and use the graphical user interface to change antenna parameters. All parameters are based on a multiple of the design wavelength. So a conversion must be done to translate design parameters to physical units.

To view a 3-Dimensional plot, click on the `Show 3D Plot` button.

To simulate an antenna array, click on th drop down menu that displays `Single Dipole Antenna` on startup and select `Linear Antenna Array`. This view will show array patterns without dioples. If you wish to insert a dipole, click the `Insert Dipole` checkbox.

# Usage Disclaimer

This program was written by a group of junior engineers for an "Introduction to Antennas" class at Oregon State University and should only be used as an **education tool**. This program **should not** be used as a substitute for professional grade antenna simulation software. Neither Oregon State University, nor the authors of this program accept any responsibility for the function or misfunction of real world antennas designed from simulations in this software.