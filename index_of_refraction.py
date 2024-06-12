"""Index of refraction library

This module calculates the index of refraction of various materials.

Each material has a separate function. Running this module as a script
plots the index of refraction of water across the visible wavelengths.

This file can be imported to run:
    * ior_water - calculates the index of refraction of water at given
                  wavelengths.
"""

import numpy as np

def ior_water(wavelengths):
    """Calculates the index of refraction of water at a given wavelength.

    This function works for visible wavelengths and is based on:
    Daimon and Masumura 2007
    0.18–1.13 µm
    20.0 °C

    Parameters
    ----------
    wavelengths : array-like, required
        wavelengths at which to calculate the index of refraction

    Returns
    ------
    iors : array-like
        indices of refraction at given wavelengths
    """
    data = np.genfromtxt('data/Daimon-20.0C.csv', delimiter=',', skip_header=1)
    data[:,0] = 1e3 * data[:,0]
    iors = np.interp(wavelengths, data[:,0], data[:,1])
    return iors

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.style.use('dark_background')
    wavelengths = np.linspace(300,800)
    iors = ior_water(wavelengths)
    plt.plot(wavelengths, iors, color='blue')
    plt.xlabel('Wavelength ($nm$)')
    plt.ylabel('Real index of refraction')
    plt.savefig('plots/index_of_refraction.png')
    plt.show()
