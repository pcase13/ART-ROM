import miepython
import matplotlib.pyplot as plt
import numpy as np
from artrom.ior import ior_water

plt.style.use('dark_background')

# Microphysical properties
m = 1.33 # Real refractive index
radius = 1000. * 1e3 # Particle radius (nm)
theta = np.linspace(120.0, 150.0, 1000) # scattering angle (degrees)

# Color-wavelength pairs option 1
wavelengths = np.linspace(400, 700, 6)  # light wavelength (nm)
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'red']
# Color-wavelength pairs option 2
wavelengths = np.asarray([415, 465, 495, 535, 580, 610, 700]) # light wavelength (nm)
colors = ['violet', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']
ms = ior_water(wavelengths)

# Translate to size parameter & mu
xs = 2 * np.pi * radius / wavelengths
mu = np.cos(theta / 180 * np.pi)
scat = []

plt.figure(figsize=(12, 7))

for x, wavelength, color, m in zip(xs, wavelengths, colors, ms):
    scat = miepython.i_unpolarized(m, x, mu, 'albedo')

    # Cartesian plot
    plt.subplot(111)
    plt.plot(theta, scat, color=color)
    plt.xlabel('Exit Angle [degrees]')
    plt.ylabel('Scattered light intensity')

plt.tight_layout()
plt.savefig('plots/rainbow_band.png')
plt.show()
