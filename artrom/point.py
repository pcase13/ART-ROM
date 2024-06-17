class Point:
    """General class for any point in space"""
    def __init__(self, location):
        self.location = location
        self.x        = location[0]
        self.y        = location[1]
        self.z        = location[2]
