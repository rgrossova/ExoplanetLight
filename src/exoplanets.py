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

    def setPhysical(self, Mp, Rp) :

        """ Set physical parameters of planet.
            
            Parameters
            ----------
            
            Mp    : The mass of the planet    [Mjup]
            
            Rp    : The radius of the planet  [Rjup]
            
            """
        
        self.mass = Mp
        self.radius = Rp

    def setOrbit(self, a, e, i, o, w, t0, P) :
        
        """ Set orbital parameters of planet.
            
            Parameters
            ----------
            
            a    : The semimajor axis of the orbit of the planet [AU]
            
            e    : The eccentricity                [-]

            i    : The orbital inclination         [deg]
            
            o    : The longitude of ascending node [deg]

            w    : The argument of periapse        [deg]
            
            t0   : The time of periapse passage    [BJD]
            
            P    : The orbital period              [days]
            
            """
        
        self.semimajoraxis = a
        self.eccentricity = e
        self.inclination = i
        self.longascnode = o
        self.argperiapse = w
        self.timeofperipass = t0
        self.orbitalperiod = P

    def setParentStar(self, Ms, Ls, SType) :
        
        """ Set parameters of parent star.
            
            Parameters
            ----------
            
            Ms    : The mass of the parent star           [Msun]
            
            Ls    : The luminosity of the parent star     [Lsun]
            
            SType : The spectral type of the parent star  [OBAFGKM]
            
            """
        
        self.starmass = Ms
        self.starluminosity = Ls
        self.spectraltype = SType

    def loadExoplanetDataFromCatalog(self):

        """ Retrieve system parameters from online catalogs
            """

    def loadSolarSystemPlanet(self, id) :
        """ Load information for a solar system planet.
            """
        SolarSystemPlanets = 'mercury venus earth mars jupiter saturn uranus neptune'.split()









