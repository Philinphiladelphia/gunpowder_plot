# This script will take a json file representing a sigil graph and display it on a 2d plane with 
# lines, 
# circles for points, 
# colors for different particle elements, 
# arrows for line velocities, 
# line width
# Line border blacklists
# Line resonance cost (if I decide per-line cost is the way to go)

# Best way to display elements: use a gradient that takes (velocity*line size) (particulate momentum) for direction and size and element for color
# Lines with permeation blacklists are half-black, half color. Full black for a double-sided border.
# Higher resonance cost lines are wider and more prominent. Note that freshly designed sigils will not yet have resonance costs filled in by the DM.
# The DM creates spells, yet it also evaluates them. Conflict of interest, no? This is where Narcissus and Echo come in and debate.

# Recursively display all child sigils




# Magic updates at a different rate than framerate under my current scheme. Players are gonna deal with it because the simulation is so damn pretty.
# Maybe simulation framerate is 60, and magic framerate is 10? I think we can handle 10 FPS from both ROS and player experience perspectives.
# Anyway, magical casting rate needs to be decoupled from simulation rate. Otherwise spells will be laggy and unpredictable.
#
# Turtles travel in linked line segments. They will store all segments that they've traveled since the last magic frame.
# When the magic frame is cast, the turtles will all dump their line segments into ROS, which will translate them into the correct coordinates and pass them into
# An incredibly simple Powder Toy API. This API consists of:
# 
#  Use Powder Toy's DrawLine() to draw out all line segments found since last check from ROS. Draw each line segment in a for loop, applying velocity as you go.
# If velocity is a quadmap, maybe we'll have to average velocities. Careful with the implementation detail here.
#
# Current magical frame rate: 10 FPS



# Players (and I) need to be able to create their own sigil spells using lines and a character called the Spell Turtle.
# Players set down lines, then place down several instances of the Spell Turtle on those lines.
# The speed of these turtles can be set individually.
# When the spell activates, the Spell Turtles run through the spell, materializing it in Powder Toy.

# a MAJOR marketing avenue for this game might be as computer science education.
# The original Microworlds turtle graphics, along with the Logo language, were unbeliveably popular in the 80s.
# Computer science as a profession could use a revival. Maybe this is it.





# AMI AI instructions tied to the sigil (for living sigils)
# AMIs have the same looping instruction set as NPCs.
# Usually the AMI will serve as a patronus (think magic missles), an autoturret, or a regenerating meatshield. 
# Our system does offer the further possibilities that it's a combination of these... 
# or that it's a living self-buff, like adaptive mana shielding. Very efficient form of defense.

# https://en.wikipedia.org/wiki/Turtle_graphics
# Turtle graphics are an incredible AMI tool.
# Spells are simple and the rosetta patterns are crazy.
# I need to research this more.

# Turtle geometry works somewhat differently from (x,y) addressed Cartesian geometry, being primarily vector-based 
# (i.e. relative direction and distance from a starting point) in comparison to coordinate-addressed systems such as bitmaps or raster graphics. 
# As a practical matter, the use of turtle geometry instead of a more traditional model mimics the actual movement logic of the turtle robot. 

# https://docs.python.org/3/library/turtle.html
# Sigils are all gonna get rasterized by turtle graphics.
# Every sigil contains one or more root turtle nodes. When a spell is cast, turtles will spread along all lines connected to these nodes simultaneously.
# Turtles will multiply out at every intersection until they run into a node that a turtle has already visited. When this happens, they die.
# This process concludes in the full spell being manifested in powder by the turtles.

# Loops are posssible. Lines have a maximum activation number. When the number of turtles that have visited both endpoints of a line exceeds that number,
# the line is considered dead.
# This allows sigils with a lifespan, like static sigils


# Turtle graphics are a layer overtop of my ROS stuff and below the game controller.

# The turtles are gonna rasterize everything themselves. 
# Then, every N milliseconds, they'll send a complete list of particles and particle velocities to spawn into the ROS interface.
# This means we only need one ROS action for the powder toy interface.
# We'll need a second one for the AI interface.
# Just those two.

# Instant spells are formed by very high-speed turtles. Remember, turtles are not physics objects, so I don't need to worry about collision.
# In a graph setting, turtle graphics are computable iteratively. I can just decide how many ticks I want per second, then let the for loop play it out.
# Send the results to ROS, and I'm done.

# I need a conversion from sigil (turtle) coordinates to player coordinates to window coordinates. Particulates are spawned in window coordinates.
# I don't even care about the World Sigil coords.
# Each turtle will do this conversion on its current location to determine what coordinates to add to the particulate spawning pool.
# The velocity of a given particulate is at a right angle to the sigil line that spawned it and has the magnitude of the line's weight.



# Research done. Sigils now use the Turtle coordinate system, relative to the player. Makes a lot more sense than any absolute system.
# Turtle graphics are actually far easier to process and rasterize than cartesian ones.

# The World Sigil is the only sigil that operates in cartesian coordinates.


# resonance is the resource that the AI uses to estimate spell mana cost. 
# Different than mana, I repeat, resonance is not the same as mana

# Particles always come into existance with the same base velocity as their parent sigil. If this sigil is moving with the player, then it might be
# player velocity + sigil velocity. How irritatingly complicated.

# We're gonna be hiding two windows for this game to work:
# One from Powder Toy and one from TurtleSim lmaoooo

# powder toy method:
# https://unix.stackexchange.com/questions/512356/is-there-any-way-to-launch-gui-application-without-gui

# Turtlesim method:
# https://stackoverflow.com/questions/71941523/is-it-possible-to-use-turtle-without-the-graphics-window

# For testing, why not run all three? Looks cool

# Turns out "flaming turtle" was the right spell lol

