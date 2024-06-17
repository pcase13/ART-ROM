class Scene:
    def __init__(self, x_limits, y_limits, z_limits):
        self.x_limits  = x_limits
        self.y_limits  = y_limits
        self.z_limits  = z_limits
        self.detectors     = []
        self.light_sources = []
        self.clouds        = []
    def add_detector(self, detector):
        self.detectors.append(detector)
    def add_lightsource(self, light_source):
        self.light_sources.append(light_source)
    def add_cloud(self, cloud):
        self.clouds.append(cloud)
