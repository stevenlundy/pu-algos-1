from math import atan, pi

def get_polar_angle(origin, point):
  dx = point[0] - origin[0]
  dy = point[1] - origin[1]
  if dy == 0:
    if dx >= 0:
      return 0
    else:
      return pi
  elif dx == 0:
    return pi/2
  elif dx < 0:
    return pi + atan(dy/dx)
  else:
    return atan(dy/dx)

def convex_hull(points):
  points.sort(key=lambda point: point[1])
  origin = points[0]
  points.sort(key=lambda point: get_polar_angle(origin, point))
  print points


convex_hull([
  (0, 1),
  (1, 6),
  (1, 3),
  (3, 0),
  (4, 5),
  (4, 3),
  (5, 4),
  (5, 2)
])
