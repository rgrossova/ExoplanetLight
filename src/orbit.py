# -*- coding: utf-8 -*-
"""
    Created on Nov 21 2016
    @author: Eder Martioli
    Laboratorio Nacional de Astrofisica, Brazil
    Last update on Nov 21, 2016
    """

import numpy as np
import math

def v_semiamp(G, i, ecc, M_b, M_s, P):
    """The velocity semi-amplitude.
        
        Parameters
        ----------
        
        : The semimajor axis of the orbit of the star [R_star]
        
        i    : The orbital inclination       [rad]
        
        ecc    : The eccentricity            [-]
        
        P    : The orbital period            [s]
        
        M_b  : The mass of companion         [kg]
        
        M_s  : The stellar mass              [kg]
        
        
        Returns
        -------
        
        K: The velocity semi-amplitude       [m/s]
        
        """
    return (((2*math.pi)/P)*((M_b*math.sin(i))/((M_b + M_s)**(2/3))*(math.sqrt(1-ecc**2)))*((2*math.pi*G)/(P**1/3)))



def E_eq(ecc,M):
    
    """The true anomaly iteration .
        
        Parameters
        ----------
        
        
        ecc  : The eccentricity                  [-]
        
        M    : M = (2*PI / P) * (t - T_0)        [-] -> from M to T_0, from T_0 to t,depending on line of sign
        
        P   : The orbital period                 [s]
        
        t   : The time interval                  [s]
        
        T_0   : The epoch of periastron passage  [s]


        Returns
        -------
        
        E: The eccentric anomaly                           [-]
        
        """
    n = 0
    E = M
    for n in range(101):
        E = M + ecc * math.sin(E)
        return E



def true_anom(ecc, M, E):
    
    """True anomaly .
        
        Parameters
        ----------
        
        ecc  : The eccentricity              [-]
        
        E  : The eccentric anomaly           [-]
        
        
        Returns
        -------
        
        f: The true anomaly                  [-]
        
        """
    return math.atan(math.sqrt((1+ecc)/(1-ecc))*(math.tan(E_eq(ecc,M)/2)))*2



def rv_model(gamma, G, i, ecc , M_b, M_s, P, E, M, w):
    
    """Radial velocity around barycenter of the system .
        
        
        Parameters
        ----------
        
        gamma  : The constant velocity       [m/s]
        
        G   : the gravitational constant     [N * m^2 / kg^2]
        
        i    : The orbital inclination       [rad]
        
        ecc    : The eccentricity            [-]
        
        M_b  : The mass of companion         [kg]
        
        M_s  : The stellar mass              [kg]
        
        P    : The orbital period            [s]
        
        E    : The eccentric anomaly         [-]
        
        M    : M = 2*PI / P * (t - T_0)      [-]
        
        P   : The orbital period                 [s]
        t   : The time interval                  [s]
        T_0   : The epoch of periastron passage  [s]
        
        w    : The argument of periastron [rad]
        
        
        Returns
        -------
        
        fr: Total flux ratio                [-]
        
        """
    
    return gamma + v_semiamp(G, i, ecc, M_b, M_s, P) * ( math.cos(true_anom(ecc, M, E) + w ) + ecc * math.cos(w) )

