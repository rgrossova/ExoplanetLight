# -*- coding: utf-8 -*-
"""
    Created on Nov 21 2016
    @author: Eder Martioli
    Laboratorio Nacional de Astrofisica, Brazil
    Last update on Nov 21, 2016
    
    exoplanets.py is a library of classes and functions to 
    handle exoplanet data.
    
    """

class planet :
    'Common base class for a planet'
    def __init__(self, Id):
        self.id=Id

    def testId(self) :
        try :
            print self.id
        except :
            print "Error: cannot retrieve exoplanet: ",self.id
            exit()

    def setPhysical(self, Mass, Radius) :
        self.mass = Mass
        self.radius = Radius

    def setOrbit(self, a, e, i, o, w, t0, P) :
        self.semimajoraxis = a  # AU
        self.eccentricity = e   # 0 - 1
        self.inclination = i    # degrees
        self.longascnode = o    # degrees
        self.argperiapse = w    # degrees
        self.timeofperipass = t0 # BJD
        self.orbitalperiod = P  # days

    def setParentStar(self, mass, spctype) :
        self.starmass = mass
        self.spectraltype = spctype

    def loadExoplanetDataFromCatalog(self):

    def loadSolarSystemPlanet(self) :
        SolarSystemPlanets = 'mercury venus earth mars jupiter saturn uranus neptune'.split()









