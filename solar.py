import numpy as np

def solar_spectrum(scale=1):
    data = np.genfromtxt('data/AM0AM1_5.csv', delimiter=',')
    wavelengths = data[:,0]
    irradiances = data[:,3]
    return wavelengths, irradiances

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.style.use('dark_background')

    # Fetch irradiances
    wavelengths, irradiances = solar_spectrum()

    # Integrate irradiances
    dw = np.zeros((wavelengths.shape))
    dw[1:] = wavelengths[1:] - wavelengths[:-1]
    dw[0] = dw[1]
    integ = round(np.nansum(irradiances * dw),2)

    # Plot up irradiance
    plt.plot(wavelengths, irradiances, color='yellow')
    plt.xlim((250,3000))
    plt.ylim((0.,1.8))
    plt.xlabel('wavelength ($nm$)')
    plt.ylabel('irradiance ($W\ m^{-2}\ nm^{-1}$)')
    plt.annotate('Integrated irradiance = ' + str(integ) + ' $W\ m^{-2}$', (1200, 1.5))
    plt.savefig('plots/solar.png')
    plt.show()
