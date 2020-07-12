#This file contains all needed data and methods corresponding to the orbital velocities of planets
# Computations are made relative to earth 

#Earth orbital velocity
Earth_orbital_velocity = 67000

#Relative to earth orbit radius

Mercury_Relative_Orbit_Radius = 0.387
Venus_Relative_Orbit_Radius = 0.723
Earth_Relative_Orbit_Radius = 1.0
Mars_Relative_Orbit_Radius = 1.524
Jupiter_Relative_Orbit_Radius = 5.203
Saturn_Relative_Orbit_Raduis = 9.539
Uranus_Relative_Orbit_Radius = 19.18
Neptune_Relative_Orbit_Radius = 30.06
Pluto_Relative_Orbit_Radius = 39.52


#Relative to earth year length

Mercury_Relative_Year_Length = 0.2409
Venus_Relative_Year_Length = 0.616
Earth_Relative_Year_Length = 1.0
Mars_Relative_Year_Length = 1.9
Jupiter_Relative_Year_Length = 12.0
Saturn_Relative_Year_Length = 29.5
Uranus_Relative_Year_Length = 84
Neptune_Relative_Year_Length = 165
Pluto_Relative_Year_Length = 248

#Relative to earth orbital velocity

Mercury_Relative_Orbit_Velocity = 1.607
Venus_Relative_Orbit_Velocity = 1.174
Earth_Relative_Orbit_Velocity = 1.000
Mars_Relative_Orbit_Velocity = 0.802
Jupiter_Relative_Orbit_Velocity = 0.434
Saturn_Relative_Orbit_Velocity = 0.323
Uranus_Relative_Orbit_Velocity = 0.228
Neptune_Relative_Orbit_Velocity = 0.182
Pluto_Relative_Orbit_Velocity = 0.159


def get_Mercury_Orbit_Velocity():
    return (Mercury_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Venus_Orbit_Velocity():
    return (Venus_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Earth_Orbit_Velocity():
    return (Earth_orbital_velocity)


def get_Mars_Orbit_Velocity():
    return (Mars_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Jupiter_Orbit_Velocity():
    return (Jupiter_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Saturn_Orbit_Velocity():
    return (Saturn_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Uranus_Orbit_Velocity():
    return (Uranus_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Neptune_Orbit_Velocity():
    return (Neptune_Relative_Orbit_Velocity * Earth_orbital_velocity)


def get_Pluto_Orbit_Velocity():
    return (Pluto_Relative_Orbit_Velocity * Earth_orbital_velocity)