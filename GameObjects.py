class GameObject:
    _image = None
    _width = None
    _height = None
    _xPos = None
    _yPos = None
    _isHovered = None
    _rect = None

    def __init__(self, image, width, height, x, y):
        self._image = image
        self._width = width
        self._height = height
        self._xPos = x
        self._yPos = y
        self._isHovered = False