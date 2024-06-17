import Point
class Cloud:
    """General class for objects to light the scene"""
    def __init__(self, centerpoint_location, radius, particle_size=1e-3, concentration=1.0):
        self.centerpoint   = Point(centerpoint_location)
        self.radius        = radius
        self.particle_size = particle_size
        self.concentration = concentration
