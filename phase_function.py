import miepython
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')


# Microphysical properties
m = 1.33 # Real refractive index
radius = 3e-2 * 1e9 # particle radius (nm)
theta = np.linspace(-180, 180, 180) # scattering angle (degrees)

# Color-wavelength pairs option 1
wavelengths = np.linspace(400, 700, 6)  # light wavelength (nm)
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'red']
# Color-wavelength pairs option 2
wavelengths = np.asarray([415, 465, 495, 535, 580, 610, 700]) # light wavelength (nm)
colors = ['violet', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']

# Translate to size parameter & mu
xs = 2 * np.pi * radius /wavelengths
mu = np.cos(theta / 180 * np.pi)
scat = []

plt.figure(figsize=(12, 7))

for x, wavelength, color in zip(xs, wavelengths, colors):
    scat = miepython.i_unpolarized(m, x, mu, 'albedo')

    # Radial plot
    plt.subplot(121, projection='polar')
    plt.plot(np.radians(theta), scat, color=color)
    plt.gca().set_yticklabels([])  # omit radial labels

    # Cartesian plot
    plt.subplot(122)
    plt.plot(theta, scat, color=color)
    plt.xlabel('Exit Angle [degrees]')
    plt.ylabel('Scattered light intensity')
    
plt.tight_layout()
plt.savefig('plots/phase_function.png')
plt.show()
