"""
A class for working with Geany Color Schemes (and other) colours.

The Color class supports two (3 actually) notations. The first is either
condensed or normal HTML/CSS-like hex colors (#ffe, #121212, etc), and the
second is a normal six digit hex string except with a `0x` prefix (0x000000,
0XeFeFeF, etc).

To create a color:

  >>> color = Color(255, 255, 255)

Or parse a color string into a color object:

  >>> color = Color.from_string('#fff')

To convert to a normalized string:

  >>> color.to_string()
  '#fff'

To get a tuple of the RGB components scaled between 0 and 1:

  >>> float_tuple = color.as_floats
  >>> round(float_tuple[0],1), round(float_tuple[0],1), round(float_tuple[0],1)
  (1.0, 1.0, 1.0)

Note: the rounding is just so the test passes without precision problems.

The color can be converted to a string

  >>> 'color: ' + str(color)
  'color: #fff'

And has a tuple-like repr:

  >>> repr(color)
  '(255, 255, 255)'

To run the tests for the Color class, just run this script with or without
the `-v` option, ex:

    $ python color.py -v

"""

class Color(object):

  def __init__(self, r=0, g=0, b=0):
    """
    >>> c = Color(1, 2, 3)
    >>> c.r, c.g, c.b
    (1, 2, 3)
    >>> c = Color(0.5, 1.2, 42.0)
    >>> c.r, c.g, c.b
    (0, 1, 42)
    >>> c = Color('abc', 33, 42)
    Traceback (most recent call last):
      ...
    ValueError: invalid literal for int() with base 10: 'abc'
    """
    self.r, self.g, self.b = int(r), int(g), int(b)

  def __str__(self):
    """
    >>> c = Color(255, 0, 0)
    >>> str(c)
    '#f00'
    """
    return self.to_string()

  def __repr__(self):
    """
    >>> c = Color(255, 0, 0)
    >>> repr(c)
    '(255, 0, 0)'
    """
    return '(%s, %s, %s)' % (self.r, self.g, self.b)

  @property
  def as_floats(self):
    """
    >>> c = Color(127, 127, 0)
    >>> float_tuple = c.as_floats
    >>> round(float_tuple[0], 1), round(float_tuple[1], 1), \
      round(float_tuple[2], 1)
    (0.5, 0.5, 0.0)
    """

    def clamp(r,g,b):
      """
      >>> clamp_tup = clamp(-1.0, 4.0, 0.5)
      >>> round(clamp_tup[0],1), round(clamp_tup[1],1), round(clamp_tup[2],1)
      (0.0, 1.0, 0.5)
      """
      rgb = [r,g,b]
      for i, c in enumerate(rgb):
        if c < 0: c = 0
        if c > 1: c = 1
        rgb[i] = c
      return tuple(rgb)

    return clamp(self.r / 255.0, self.g / 255.0, self.b / 255.0)

  def to_string(self, prefix='#'):
    """
    >>> c = Color(255, 0, 0)
    >>> c.to_string()
    '#f00'
    >>> c = Color(255, 255, 255)
    >>> c.to_string('0x')
    '0xffffff'
    >>> c.to_string('#')
    '#fff'
    """
    c = '%02x' % self.r + '%02x' % self.g + '%02x' % self.b
    if prefix == '#' and c[0] == c[1] and c[2] == c[3] and c[4] == c[5]:
      c = c[0] + c[2] + c[4]
    return str(prefix) + c

  @staticmethod
  def from_string(color_str, prefixes=['#', '0x']):
    """
    >>> c = Color.from_string('0xFf0000')
    >>> c.to_string()
    '#f00'
    >>> c.r, c.g, c.b
    (255, 0, 0)
    """
    c = str(color_str)
    if not any(c.startswith(pfx) for pfx in prefixes):
      return None
    for pfx in prefixes:
      if c.startswith(pfx):
        c = c[len(pfx):]
        break
    if len(c) != 3 and len(c) != 6:
      return None
    elif len(c) == 3:
      c = c[0] + c[0] + c[1] + c[1] + c[2] + c[2]
    r, g, b = c[0:2], c[2:4], c[4:6]
    r, g, b = int(r, 16), int(g, 16), int(b, 16)
    return Color(r=r, g=g, b=b)

if __name__ == "__main__":
  import doctest
  doctest.testmod()
