import numpy as np

def ior_water(wavelengths):
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
