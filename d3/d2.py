import sys

def move_left(current_point, distance):
  points = []
  for i in range(current_point[0]-1, current_point[0]-distance-1, -1):
    points.append((i, current_point[1]))
  return points

def move_right(current_point, distance):
  points = []
  for i in range(current_point[0]+1, current_point[0]+distance+1):
    points.append((i, current_point[1]))
  return points

def move_down(current_point, distance):
  points = []
  for i in range(current_point[1]-1, current_point[1]-distance-1, -1):
    points.append((current_point[0], i))
  return points

def move_up(current_point, distance):
  points = []
  for i in range(current_point[1]+1, current_point[1]+distance+1):
    points.append((current_point[0], i))
  return points

def get_points(path):
  current_point = [0, 0]
  points = []
  for movement in path:
    direction = movement[:1]
    distance = int(movement[1:])

    if direction == 'L':
      for point in move_left(current_point, distance):
        points.append(point)
      current_point[0] -= distance
    
    elif direction == 'R':
      for point in move_right(current_point, distance):
        points.append(point)
      current_point[0] += distance
    
    elif direction == 'D':
      for point in move_down(current_point, distance):
        points.append(point)
      current_point[1] -= distance
    
    elif direction == 'U':
      for point in move_up(current_point, distance):
        points.append(point)
      current_point[1] += distance
    else:
      print("ERROR: Unknown direction " + direction)
  return points
    
def manhattan_distance(point):
  return abs(point[0]) + abs(point[1])

def wire_dist(intersections, firstPts, secPts):
    distPts = []
    for pt in intersections:
        d1 = 1
        for ptF in firstPts:
            if ptF == pt:
                break
            d1 = d1 + 1
        d2 = 1
        for ptS in secPts:
            if ptS == pt:
                break
            d2 = d2 + 1
        distPts.append(d1+d2)
    return distPts
            

f = open("input.txt", 'r')
first_wire_path = f.readline().replace("\n", "").split(",")
second_wire_path = f.readline().replace("\n", "").split(",")

#first_wire_path = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
#second_wire_path = ["U62","R66","U55","R34","D71","R55","D58","R83"]

#Set of points where the wires pass
first_wire_points = get_points(first_wire_path)
second_wire_points = get_points(second_wire_path)

print(first_wire_points)
print(second_wire_points)

intersections = set(first_wire_points).intersection(set(second_wire_points))
distances = wire_dist(intersections, first_wire_points, second_wire_points)
print(sorted(distances))
