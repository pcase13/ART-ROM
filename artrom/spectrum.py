import numpy as np
from config import solar_irradiance_data

class Spectrum:
    """General class defining various spectra"""
    def __init__(self, spectrum_name='solar', intensity=1.0):
        self.spectrum_name = spectrum_name
        self.intensity = intensity

    def get_spectrum(self):
        if self.spectrum_name == 'solar':
            print(self.intensity)
            return self._solar_spectrum(scale=self.intensity)
        else:
            raise NotImplementedError

    def _solar_spectrum(self, scale=1.):
        """Calculate solar irradiance after passing through the atmosphere.

        This function works for visible wavelengths and is based on:
        https://www.pveducation.org/pvcdrom/appendices/standard-solar-spectra

        Parameters
        ----------
        scale : float, optional
            amount to scale solar irradiance by

        Returns
        ------
        wavelengths : array-like
            wavelengths at which irradiances are given (nm)
        irradiances : array-like
            irradiance at given wavelengths (W m-2 nm-1)
        """
        data = np.genfromtxt(solar_irradiance_data, delimiter=',')
        wavelengths = data[:,0]
        irradiances = data[:,3]
        return wavelengths, irradiances

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.style.use('dark_background')

    # Fetch irradiances
    spectrum = Spectrum(spectrum_name='solar', intensity=1.0)
    wavelengths, irradiances = spectrum.get_spectrum()

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
    plt.savefig('../plots/solar.png')
    plt.show()
