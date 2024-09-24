## Running Powder Toy as a Server

Download the Powder Toy [here](https://powdertoy.co.uk/Download.html)

```
Xvfb :10 &
DISPLAY=:10 ./powder
```

This throws the whole GUI into a virtual frame buffer, getting rid of it. At this point, the only access to the game is through my LUA script.

There's a render option to render literally nothing. That's perfect for what I need. Render nothing, just grab particle data and throw it into Gunpowder Plot. Let the simulation handle everything.

## How to use Powder Toy

I should keep every copy of powder toy oriented in the same "north" direction in the game. This will make interpolation a billion times easier.

Beyond that, just run a powder toy of given max area around every player. When two players come near enough to each other for their powder toys to touch, they become one big powder toy with double with pixels. This will be represented in-game by the merging of the powder zones, creating an arena with the middle exactly between the two PCs

When the two PCs exit the arena, their individual powder toys reinitialize by taking a rectangular snapshot of the big powder toy around each PC and then applying that snapshot to their personal powder toy.

Actually, this isn't only for PCs. Every NPC that has magic will also have a gunpowder zone of their own. Most of the time, these will stay merged with their leader (you), but they can seperate as normal.

## LUA API

NOTE NOTE NOTE:
The stamp tool is going to be my BEST FUCKING FRIEND when creating and combining spells. I can use it to do a lot of different stuff, including probably the circular trimming. Just stamp down "nothing" in a circular frame.

Functions:

Read all particles

Save all particles to file

Load all particles to memory

Write all particles

Create new simulation window with given size

Trim particulate data to a circular region of radius R around the center of the screen (the player).
This should happen in Powder Toy. This makes sure that we don't have any weirdness coming from the missing corners.
However, I do want the circle in Powder Toy to be larger than what's actually displayed in Gunpowder Plot. This helps with scrolling and lends a sense of smokey, shifting magical winds.

Spawn elements in a specified configuration, velocity, and pressurization within Powder Toy. These are spells. Note that at many times, multiple players will be spawning elements into the same Powder Toy instance at the same time. I should make sure that's possible.

Clear Powder Toy

I need a really fast, clean implementation for particulate scrolling. If this is gonna be my whole game engine, I need it to work well. I think this has to be in LUA. It'll take the PC's vector of change of coordinates, then scroll the Powder Game appropriately. As my particulate circle in Powder Toy is larger than the one displayed in Gunpower Plot, I have some margin. This will make sure that elements don't dissapear suddenly.
    Brilliant idea!! The area between the larger Powder Toy circle and the Gunpowder Plot circle contains gradient with decreasing alpha values. This means that magic will look like it's dissapearing as it goes away, and also that gunpowder zones are actually slightly bigger than they appear. This will give the player a sense of leniency.

Whenever there's an obstacle in the godot engine, I'm just gonna use my script to write "rock" particulates or whatever where that obstacle should be. This is way easier than defining a whole world in Powder Toy. The rectangle that holds the player's viewport should be the same as the gunpowder zone: slightly smaller in Gunpowder Plot than in Powder Toy. This makes sure that the world extends beyond the player's screen, lending a sense of realism.

Player collisions and terrain destruction are both handled in Powder Toy. The worldmap generated procedurally by Gunpowder Plot is processed as a kind of "suggestion" to Powder Toy. When the player approaches a new area, Gunpowder Plot tells Powder Toy what particulates to render in that area. From there on, collisions and graphics are all up to the Powder Toy. A simple, elegant approach.

## Persona Spells

Persona spells are closely linked to the LUA Api. Each Persona has a special power over the currently running instance of Powder Toy.

### Architect - creation, structure

This will allow the DM to create things like complex and durable defensive structures, automated turrets, and of course, hyper-destructive nukes. These can be based on a seed from me or directly drawn from the DM's imagination.
Unlocks radioactive elements and particles. Nuke time.
Unlocks vibranium and diamond.

### Chronos - time

This will allow the DM to slow down or speed up the entire simulation rate. This will affect both you and your opponent because there isn't really the programmatic possibility of having two different timestreams in a single frame. If your opponents spella also affects time, then the two effects will multiply. For example:

0.5x times 2x: 1x

3x times 3x: 9x

0.25x times 0.25x: 0.0625x

### Death - destruction

This allows you to directly delete particles from the scene. The only particles you can't delete are playerium.
Unlocks antimatter and singularity spells.

### Fate - laws of nature, physical rules

This allows you to affect simulation settings like newtonian gravity, heat dissipation rate, and whatever else I can find. Conflicting effects work the same as time, multiplying together.

Unlocks gravitons, white and black holes,

### Hypnos - dreams and imagination

Go crazy. The DM gains unprecedented control over the LUA API. It will interpret even vague statements like "the essence of joy" as best it can. Creations will become cheaper to cast, but more vague and dream-like.

To implement this, I can make a "plausibility" setting for the DM. When Hypnos is unlocked, plausibility becomes adjustable.

Unlocks Clone, 

### Iris - perception

This creates illusions. These are materials that appear to be other materials. They can be cheap, easy-to-cast cardboard, but they'll look like titanium or lava or acid to opponents.

Examples:

"Acid disguised as water"

"Lava disguised as stone"

This is implemented by maintaining a seperate (but identical) list of rendering properties for particulates for all PCs. When an Iris spell is cast, the list of rendering properties is temporarily modified. This allows different players to see different things.

### Pandora - resonance

The DM will apply it's knowledge of the Powder Magic system to optimize all spells further. The DM will become more creative and engineering-minded, adding useful features or improving spells efficacy beyond the base text. The persona of DM creative genius and agency, showing off what the DM can do.

### Theia - life and light

Exactly what it sounds like. You unlock select elements from the Game of Life, and also all the forms of light and radiation in the game.

Unlocks Stickmen and other fighters from the Special tab.