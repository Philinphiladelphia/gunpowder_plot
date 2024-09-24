// Powder Magic interface

// Manifest playerium in the Powder Toy so it can take damage
GetPlayerLocation();
ManifestPlayerParticles();

// move all previously existing particles relative to the player, load in new particles from the World Sigil to fill in the edges
GetWorldSigil();

// I shouldn't give Powder Toy the whole world sigil at once. 
// I'll give it my viewport coordinates and it can give me all the World Sigil lines inside of
// those coordinates or intersecting with the rectangle. Those are the only lines I need to render, anyway.
// This check is pretty easy. Are both points in the line outside of the box? Ditch it.

// I guess the world sigil and all other sigils are gonna live in ROS. It doesn't make sense to process anything in godot.


UpdateTerrain(world_sigil);

// Manifest sigil magic. This includes player sigils, enemies, generals, etc.
GetBufferedSigils();
ManifestSigils();

// to control this, I need ROS topics for player location, world sigil, and activated sigils.
