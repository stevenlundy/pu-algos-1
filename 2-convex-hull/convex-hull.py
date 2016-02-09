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

def is_ccw(a, b, c):
  area = (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])
  return area > 0

def convex_hull(points):
  points.sort(key=lambda point: point[1])
  origin = points[0]
  points.sort(key=lambda point: get_polar_angle(origin, point))
  hull_points = []
  hull_points.append(points[0])
  hull_points.append(points[1])
  for i in range(2, len(points)):
    hull_points.append(points[i])
    while not is_ccw(*hull_points[-3:]):
      del hull_points[-2]
  return hull_points

print convex_hull([
  (0, 1),
  (1, 6),
  (1, 3),
  (3, 0),
  (4, 5),
  (4, 3),
  (5, 4),
  (5, 2)
])
