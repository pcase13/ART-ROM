import Ray
import Point
class Pixel:
    """General class for end point pixel"""
    def __init__(self, location, angle=0.0, rgb=np.zeros(3)):
        self.location = Point(location)
        self.angle    = angle
        self.rgb      = rgb
    def set_rgb(self, rgb):
        self.rgb = rgb
    def cast_ray(self, wavelengths):
        ray = Ray(wavelengths)
        self.rgb = ray.cast(self.location, self.angle)
