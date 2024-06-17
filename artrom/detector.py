import Pixel
import Point
class Detector:
    """General class for arrays of pixels to receive"""
    def __init__(self, resolution, dx, dy, centerpoint_location, viewpoint_location):
        self.centerpoint = Point(centerpoint_location)
        self.viewpoint   = Point(viewpoint_location)
        self.dx          = dx
        self.dy          = dy
        self.pixels      = np.empty(resolution, dtype=object)

        vPixel = np.verctorize(Pixel)

        locations_x = np.arange(-1*dx*resolution[0]/2, dx*resolution[0]/2, dx) + location[0]
        locations_y = np.arange(-1*dy*resolution[1]/2, dy*resolution[1]/2, dy) + location[1]
        locations_z = np.zeros((resolution)) + location[2]
        locations   = np.array((locations_x, locations_y, locations_z))

        angles_phi   = np.tan((self.viewpoint.x - locations_x)/(self.viewpoint.y - locations_y))
        angles_theta = np.tan(np.sqrt((self.viewpoint.x - locations_x)**2 + (self.viewpoint.y - locations_y)**2)/(self.viewpoitn.z - locations_z))
        angles       = np.zarray((angles_phi, angles_theta))

        self.pixels[:,:] = vPixel(locations, angle=angles),

