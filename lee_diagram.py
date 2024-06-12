import miepython
import matplotlib.pyplot as plt
from wavelength_to_rgb import intensities_to_rgb
from solar import solar_spectrum
from progress_bar import progress_bar
from index_of_refraction import ior_water
import numpy as np
plt.style.use('dark_background')

# Microphysical properties
radii = np.logspace(1,3,100)*1e3 # Particle radius (nm)
theta = np.linspace(120., 150., 1000) # scattering angle (degrees)
s_wavelengths, s_irradiances = solar_spectrum()
wavelengths = s_wavelengths[(s_wavelengths > 390) & (s_wavelengths < 831)]
irradiances = s_irradiances[(s_wavelengths > 390) & (s_wavelengths < 831)]
ms = ior_water(wavelengths)

# Translate to size parameter & mu
xs = np.zeros((radii.shape[0],wavelengths.shape[0]))
for i, radius in enumerate(radii):
    for j, wavelength in enumerate(wavelengths):
        xs[i,j] = 2 * np.pi * radius / wavelength
mu = np.cos(theta / 180 * np.pi)

# Mie scattering calculation
scat = np.zeros((radii.shape[0], mu.shape[0], wavelengths.shape[0]))
for i in progress_bar(range(radii.shape[0]), "Scattering: ", 40):
    for j in range(wavelengths.shape[0]):
        scat[i,:,j] = miepython.i_unpolarized(ms[j], xs[i,j], mu, 'albedo')

# Multiply by solar irradiance
scat = scat * irradiances

# Find normalizing maximum
maximum = np.max(np.sum(scat, axis=1))

# Colorize
rgb = np.zeros((radii.shape[0], mu.shape[0], 3))
for i in progress_bar(range(radii.shape[0]), "Coloring: ", 40):
    for j in range(mu.shape[0]):
        rgb[i,j,:] = intensities_to_rgb(wavelengths, scat[i,j,:], norm=maximum)

# Normalize image
rgb /= np.max(rgb)

# Plot
fig = plt.figure(figsize=(10,7))
plt.imshow(rgb, aspect='auto', extent=[theta[0], theta[-1], 2, 0])
plt.gca().set_yticks((2,1,0))
plt.gca().set_yticklabels((1000,100,10))
plt.xlabel('Scattering angle ($degrees$)')
plt.ylabel('Radius ($\mu m$)')
plt.savefig('plots/lee_diagram.png')
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
