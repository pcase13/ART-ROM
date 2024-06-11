import miepython
import matplotlib.pyplot as plt
from wavelength_to_rgb import intensities_to_rgb
from solar import solar_spectrum
from progress_bar import progress_bar
from index_of_refraction import ior_water
import numpy as np
plt.style.use('dark_background')

# Microphysical properties
radius = 300. * 1e3 # Particle radius (nm)
theta = np.linspace(120.0, 150.0, 1000) # scattering angle (degrees)
s_wavelengths, s_irradiances = solar_spectrum()
wavelengths = s_wavelengths[(s_wavelengths > 390) & (s_wavelengths < 831)]
irradiances = s_irradiances[(s_wavelengths > 390) & (s_wavelengths < 831)]
ms = ior_water(wavelengths)

# Translate to size parameter & mu
xs = 2 * np.pi * radius / wavelengths
mu = np.cos(theta / 180 * np.pi)

# Mie scattering calculation
scat = []
for i in progress_bar(range(len(xs)), "Scattering: ", 40):
    scat.append(miepython.i_unpolarized(ms[i], xs[i], mu, 'albedo'))
scat = np.asarray(scat)

# Multiply by solar irradiance
scat = (scat.T * irradiances).T

# Find normalizing maximum
maximum = np.max(np.sum(scat, axis=1))*2

# Colorize
rgb = []
for i in progress_bar(range(theta.shape[0]), "Coloring: ", 40):
    rgb.append(intensities_to_rgb(wavelengths, scat[:,i], norm=maximum))
img = np.asarray(rgb).reshape(1,len(rgb),3)

# Normalize image
img /= np.max(img)

# Plot
plt.imshow(img, aspect='auto')
plt.show()

'''
plt.figure(figsize=(12, 7))


    # Cartesian plot
    plt.subplot(111)
    plt.plot(theta, scat, color=color)
    plt.xlabel('Exit Angle [degrees]')
    plt.ylabel('Scattered light intensity')

plt.tight_layout()
plt.savefig('plots/rainbow_band.png')
plt.show()
'''
