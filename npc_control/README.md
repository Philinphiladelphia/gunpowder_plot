Non-Player Character control is the name of the control scheme for all NPC characters.

NPC characters are varied in their physical attributes, so we have a set of basic actions that all of them share and specialized abilities for each.

Each NPC has this basic set of actions:

Face direction
Move in direction
Static overwatch
Dynamic overwatch on waypoint route
Basic Attack in target direction
Heavy Attack in target direction
Read leader vector, direction, heading, target, and leader weapon heading from leader for reference
Choose between two actions based on data point (if/else)
Die

These commands will be strung together in an infinite loop. Each will be associated with a duration. If the command is completed early, the NPC will skip to the next command.

Each NPC has at least three activatable abilities, one in each of the following three categories:

Movement
Defense
Attack

Some NPCs have special skills or unusual atributes. These NPCs will contain instructions on how to use them.

Magical abilities can be granted to NPCs. When granted, instructions on how to use them are written to the NPC's behavior list along with the ability. When this happens, the NPC gains mana and all its benefits except for the brainwashing ones.


you can change your own feelings whenever the fuck you want. You can also do whatever the fuck you want! That's the beauty of life!