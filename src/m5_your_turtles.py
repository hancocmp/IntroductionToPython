"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mason Hancock.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg
window = rg.TurtleWindow()

blue_turt = rg.SimpleTurtle('turtle')
blue_turt.pen = rg.Pen('blue', 3)
blue_turt.speed = 50  # Fast

red_turt = rg.SimpleTurtle('turtle')
red_turt.pen = rg.Pen('red', 3)
red_turt.speed = 50  # Fast
red_turt.pen_up()
red_turt.right(90)
red_turt.forward(100)
red_turt.right(90)
red_turt.forward(50)
red_turt.pen_down()
sizeB=200
size=200
for k in range(10):

    blue_turt.draw_circle(sizeB)
    sizeB=sizeB-10

for k in range(10):
    red_turt.draw_square(size)
    size=size-20