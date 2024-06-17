import Point
class Lightsource:
    """General class for objects to light the scene"""
    def __init__(self, centerpoint_location, spectrum='solar', intensity=1.0):
        self.centerpoint = Point(centerpoint_location)
        self.spectrum    = Spectrum(spectrum, intensity=intensity)
