
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small, big, goal):
  if goal > ((big * 5) + small):
    return False
  if  goal % 5 > small:
    return False
  return True

