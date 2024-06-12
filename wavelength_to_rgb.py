"""Color-from-wavelength library

This module calculates RGB values for given wavelength or relative
intensities at various wavelengths.

It can also be run to plot a comparison of various ways of 
representing a rainbow.

This file can be imported to run:
    * wavelength_to_rgb - calculate RGB values for monochromatic
                  wavelength.
    * intensities_to_rgb - calculate RGB values for given relative
                  intensities at given wavelengths.
"""
import numpy as np

def wavelength_to_rgb(wavelength, intensity=0.5, option='bruton'):
    """Calculates the RGB values for a given wavelength

    Implemented techniques:
    - Bruton

    Parameters
    ----------
    wavelength : float, required
        wavelength at which to calculate color

    Returns
    ------
    R : float
        Red value between 0 and 1
    G : float
        Green value between 0 and 1
    B : float
        Blue value between 0 and 1
    """


    if option == 'bruton':
        '''
        Based on code by Dan Bruton
        http://www.physics.sfasu.edu/astro/color/spectra.html
        '''
        wavelength = float(wavelength)
        if wavelength >= 380 and wavelength <= 440:
            attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
            R = ((-(wavelength - 440) / (440 - 380)) * attenuation)
            G = 0.0
            B = (1.0 * attenuation)
        elif wavelength >= 440 and wavelength <= 490:
            R = 0.0
            G = ((wavelength - 440) / (490 - 440))
            B = 1.0
        elif wavelength >= 490 and wavelength <= 510:
            R = 0.0
            G = 1.0
            B = (-(wavelength - 510) / (510 - 490))
        elif wavelength >= 510 and wavelength <= 580:
            R = ((wavelength - 510) / (580 - 510))
            G = 1.0
            B = 0.0
        elif wavelength >= 580 and wavelength <= 645:
            R = 1.0
            G = (-(wavelength - 645) / (645 - 580))
            B = 0.0
        elif wavelength >= 645 and wavelength <= 750:
            attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
            R = (1.0 * attenuation)
            G = 0.0
            B = 0.0
        else:
            R = 0.0
            G = 0.0
            B = 0.0
        R = R ** intensity
        G = G ** intensity
        B = B ** intensity
        return R, G, B
    else:
        raise NameError

def intensities_to_rgb(wavelengths, intensities, norm=50, option='stockman_sharpe'):
    """Calculates the RGB values for a given set of intensities at specified wavelengths.

    Parameters
    ----------
    wavelengths : array-like, required
        wavelengths for given intensities 
    intesnities : array-like, required
        relative intensities at given wavelengths
    norm : float, optional
        normalization value
    option : string, optional
        which method

    Returns
    ------
    rgb : array-like
        array of (r, g, b) values from 0 to 1
    """
    if option == 'stockman_sharpe':
        data = np.genfromtxt('data/lin2012xyz2e_1_7sf.csv', delimiter=',')
        data[data == -99.] = np.nan
        data_x = np.interp(wavelengths, data[:,0], data[:,1])
        data_y = np.interp(wavelengths, data[:,0], data[:,2])
        data_z = np.interp(wavelengths, data[:,0], data[:,3])
        x = np.nansum(intensities * np.exp(data_x))
        y = np.nansum(intensities * np.exp(data_y))
        z = np.nansum(intensities * np.exp(data_z))
        matrix = np.array([
            [3.2406, -1.5372, -0.4986],
            [-0.9689, 1.8758, 0.0415],
            [0.0557, -0.2040, 1.0570]
        ])
        rgb = matrix @ np.asarray([x,y,z])
        rgb = rgb/np.sum(rgb)
        #rgb /= np.max(rgb)
        rgb = rgb * np.sum(intensities)/norm + np.zeros((3,)) * ((norm - np.sum(intensities))/norm)
        return rgb
    else:
        raise NameError

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.style.use('dark_background')

    # bruton
    wavelengths = np.arange(300,800,1)
    intensities = np.linspace(0.0,2.0,100)
    img = []
    for i, wavelength in enumerate(wavelengths):
        for j, intensity in enumerate(intensities):
            r_, g_, b_ = wavelength_to_rgb(wavelength, intensity=intensity)
            img.append([r_,g_,b_])
    img_bruton = np.asarray(img).reshape(len(wavelengths), len(intensities), 3)

    # stockman & sharpe
    intensities = np.ones(441) * .0
    rgb = []
    for i in range(intensities.shape[0]):
        intensities[:] = 0.
        mu = i
        sig = 30
        intensities[:] = [1.0 / (np.sqrt(2.0 * np.pi) * sig) * np.exp(-np.power((j - mu) / sig, 2.0) / 2) for j in range(intensities.shape[0])]
        intensities /= np.max(intensities)
        rgb.append(intensities_to_rgb(intensities, option='stockman_sharpe'))
    img_ss = np.asarray(rgb).reshape(1,intensities.shape[0],3)

    fig = plt.figure(figsize=(12,10))
    plt.subplot(121)
    plt.imshow(img_bruton, aspect='auto')
    plt.subplot(122)
    plt.imshow(img_ss, aspect='auto')
    plt.savefig('plots/wavelength_to_rgb.png')
    plt.show()
