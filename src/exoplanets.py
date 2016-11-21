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


########### FUNCTION TO RETRIEVE STELLAR PARAMTERS ##############
    def getPlanetParameters(object, catalogfile="") :
    
        if catalogfile :
            # getting the catalogue from a local path
            cata = oec.get_catalogue(catalogfile)
        else :
            # getting the catalogue from the default remote source
            cata = oec.get_catalogue()
    
    
        #-- Retrieve planet relevant information
        planetstr = ".//planet[name='" + object + " b']"
        planet = cata.find(planetstr)
    
        planetProps = 'mass radius period semimajoraxis eccentricity transittime temperature'.split()
        plPropsVal = {}
    
        for p in planetProps :
            plPropsVal[p] = []
            if '+/-' in str(findvalue(planet,p)) :
                for s in str(findvalue(planet,p)).split(' +/-') :
                    plPropsVal[p].append(float(s))
            elif '+' in str(findvalue(planet,p)) and '-' in str(findvalue(planet,p)):
                for s in str(findvalue(planet,p)).split(' ') :
                    plPropsVal[p].append(float(s))
            else :
                plPropsVal[p].append(str(findvalue(planet,p)))

#-- uncomment below to print all planet properties
#    for properties in cata.findall(planetstr+"/*"):
#        print "\t" + properties.tag + ":", properties.text

#-- Retrieve star relevant information
        starstr = ".//star[name='" + object + "']"
        star = cata.find(starstr)
    
        starProps = 'mass radius temperature magV magB magJ magH magK metallicity'.split()
        starPropsVal = {}
    
        for p in starProps :
            starPropsVal[p] = []
            if '+/-' in str(findvalue(star,p)) :
                for s in str(findvalue(star,p)).split(' +/-') :
                    starPropsVal[p].append(float(s))
            elif '+' in str(findvalue(star,p)) and '-' in str(findvalue(star,p)):
                for s in str(findvalue(star,p)).split(' ') :
                    starPropsVal[p].append(float(s))
            else :
                starPropsVal[p].append(str(findvalue(star,p)))


#-- uncomment below to print all planet properties
#    for properties in cata.findall(starstr+"/*"):
#        print "\t" + properties.tag + ":", properties.text
        return plPropsVal, starPropsVal
###########################################








