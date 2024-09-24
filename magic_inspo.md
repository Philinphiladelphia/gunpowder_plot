## Current State

The four kinds of player spells:
Continous sigil
Instant sigil
Indepenent sigil
Evolving sigil

Continous sigils are the simplest and lowest-cost. These sigils continously summon powder into the world based on their sigil lines. They continously drain mana during their operation. When the player stops casting the spell, it stops generating powder. This is good for things like flamethrowers and water jets.

Instant sigils are the discrete form of continous sigils. They cost a certain amount of mana, instantly summon something, and then go on cooldown for a given amount of time. Instant sigils can be charged up for enhanced effects. This is good for things like throwing boulders or summoning walls of ice.

Independent Sigils or Static Sigils are sigils which summon powder that dissapears instantly. The sigils themselves move independently across the screen, summoning a moving fireball or a black hole.
Independent sigils also enable defenses that move with the player, like "globe of water".
Independant sigils have the same control interface as NPCs, with maybe a few extras.
Independent sigils have a higher mana cost than instant sigils, as they are more focused.

Evolving sigils are independent sigils that grow more lines or summon their own sigils in their lifetime. They are the most advanced kind of sigil. They can summon phoenixes, labyriths, or endless hordes of zombies. They are, by neccessity, quite rare.
Evolving sigils take a chunk of your max mana when cast. They can be cast N times concurrently, where N varies from spell to spell.
An evolving sigil will use the mana you gave it to expand itself continously or to cast sigils of its own. Evolving sigils will run indefinitely until dismissed. Even when outside of a gunpowder zone, an evolving sigil will persist. When dismissed, the mana used on the evolving sigil will return to the player.

### Colors

Obviously, these sigils are color-coded Overwatch style.

Continous sigil: white
Instant sigil: blue
Indepenent sigil: purple
Evolving sigil: orange

https://www.youtube.com/watch?v=2xYaTGRvpv4

## Old Stuff

https://noita.fandom.com/wiki/Guide_To_Wand_Mechanics

https://powdertoy.co.uk/Download.html

The powder toy is so damn good as a magic system that I'm ditching the military weapons entirely. The game consists of perceptual sight lines, circular sound waves, and magical interactions through the Powder Toy engine.

Powder toy development notes:

https://powdertoy.co.uk/Wiki/W/Main_Page.html

Godot Ros Bridge:
https://github.com/flynneva/godot_ros

Next step: integrate turtlesim with powder toy.
I wanna manifest a flaming turtle.


Do I need a more minimal game engine? I feel like godot has too much clutter. I basically need to represent a big pixel buffer and a couple player attributes. Maybe there's something really low-level out there?

Looks like Godot is the low-level thing. It's 2D mode should allow me to work exclusively in pixels, which is exactly what I want. I can make my pixels in Godot correspond 1:1 with particles in Powder Toy.

The DM is going to design magic spells in vector graphics form. Then we will use the drawline function in Powder Toy to rasterize the vector spells. This keeps spells abstractable and able to be rotated. Also, spell results will be more consistent.
The DM can make vector spells for players, but I think a lot of players would enjoy a simple UI where they can craft a vector spell of their own. This will give them a better appreciation of the process.

Sigils, as saved spells, will have the intermediary form of JSON. A spell is a list of lines, the material of those lines, and the initial velocity of those lines. AI can also write this directly. Spells can also contain things like the heat or weight of their components.

I should get a ThoughtBot to crank out like 2000 different unique world building blocks for me so I don't have to do it myself.

When a spell is cast, the vector is imprinted onto the simulation as a flash of fire or a wall of water. More complex vector spells like shields and bombs are possible as well.

## Spell Ideas

All spells are chargable. Charge does different things for every spell. For some, it increases velocity. For some, heat. For some, number of particles. For some, dynamic sigil lines home in on your enemies or form a defensive wall. For some, a combination of all of this happens.

In action, spells work like this:
Take a presaved spell, cast it, then dynamic elements resolve and expand during the charging time (increasing mana cost), then both static and dynamic lines are sent to the Powder Magic engine. Think of it as spell extension. This allows incredibly adaptable and behaviorally complex spells, generated dynamically.

Players can use the normal Powder Toy brush tool to summon balls of elements directly into the world. They will pay the element's cost directly. As these summoned elements have no starting velocity, this ability is more useful for defense or utility than for offense.

Sigil magic charge-up time and dynamic sigil ground markers can act as telegraphing. When the Demon King is about to cast a big spell, you can see all of his Sigil lines on the ground before he casts it. Similarly, when he casts a Sigil Magic projectile he has to charge it up first. This makes the game feel more fair. Note that all PCs can charge while moving, with perhaps a slight speed penalty. It's always possible to roll out of a charging or casting spell to cancel it, but mana will not be refunded.

Players shouldn't be able to craft spells just anytime. They should find an altar that allows them to input a phrase. When input, the altar will lock and enemies will come out to attack. Once the DM is done generating the spell (or after like a minute maybe), the altar pops open. Activate it, and you'll be granted three options for spells all based on the prompt you provided.

There can be some "broken spell altars" that contain some fixed words in the prompt, or only allow you to enter a specific amount of letters. This is a way that we can force the players to be creative with their spells.
Spell Altars can have some spell attributes visible ahead of time. That way, the player can input a phrase which might synergize with the buffs to the spell provided by the altar.

Spells can be upgraded at shops. These upgrades will reduce spell cost, increase velocity, add strange elements, merge spells, etc. Money for shops is dropped by slain enemies.

Generals drop an upgraded version of the Altar called a Persona Altar. This allows you to directly commune with a DM persona to write a spell. This spell has a fixed word like "time" or "space" or "black hole", etc. This is a word related to the power of the persona, and is different every time. The player will finish the spell and it will generate. The spell will have power over the given persona's systems and elements.

The Demon King is totally unbeatable in the early game because he has access to every single DM persona right from the start. This makes his basic spells way better than yours. He'll also probably have way more mana and HP than you from the start. He is a Demon King, after all!

The Demon King grants some of his generals Persona powers. This is his biggest mistake- once you kill those generals, you will gain those same powers for yourself. Only then can you battle the Demon King. Persona powers can be seen a little like metroidvania upgrades.

I don't feel like the Demon King should be a persistent entity throughout the game. The Demon King exists in a palace alllllll the way at the end of the game, like Bowser. Getting there is the journey of the game and the goal of the rouguelike. Also, make the game design wayyyy easier.

I think I'll design a free spell that almost everyone has access to called "gun". Make it with gunpowder and lead lmao.


If people want points instead of lines, they're gonna have to learn that a line with both points in the same place is just a point.

In Gunpowder Plot, if you wanna shoot something, you summon a gun, it fires, then it dissapears. Just like Reaper.

Can dynamic sigils be generated by querying the DM in real-time? It'll stream out the new dynamic lines.


If I really want spell inspo, just look at the Dungeons and Dragons spell list.



Level structure can be shorter, more broken up, like Spelunky, Peglin, Enter the Gungeon, Slay the Spire, or Hades. A big, expansive level is harder to generate and harder to render.

Hades
^^ This is my primary level generation inspo
Remember to go hard on the level design. You have everything you could want, from landmines to GOL monstrosities. Be creative, bob. Remember, in rougelikes, it's ok to kill players unfairly a few times. In fact, it's kinda expected.

Basic game structure:
5 worlds, one general at the end of each world. You gain a persona spell from each general and gain a great deal of mana along the way.

If you make it through 5 worlds, you can challenge the Demon King. If you haven't gained a lot of mana, chosen your spells wisely, and learned how to synergize, you'll never have a chance. Even then, you'll need plenty of HP and good dodging skills to make it through the fight.

When you beat the Demon King, you'll unlock a new element or power for all future runs. Rinse and repeat forever. Enemies will start getting harder slowly as you start getting better. The Demon King will unlock new powers and strategies as you beat him, granting you more and more rewards as you beat him more times.

I should start the players off reaaaaal basic: just fire and velocity manipulation. They'll unlock every single element of the whole system one at a time. Not only will this be a great learning tool, it's highly motivational to keep playing and it stretches the runtime of the game greatly. Every single piece of progress unlocks something new. All the mana that they collect in a given run is converted to experience at the end, unlocking all kinds of new things. This will keep players playing even when they lose.

Also helps if players can have some agency in which powers they unlock. Maybe let's do it Vampire Surviors style? Players can put experience points whereever they want, building up a character with personlized strengths and weaknesses over time.



Magic should have a feeling like meditation. Like the world around you goes still for a moment. Like everyone else is still dancing, but you are standing still. Somehow, everything dances around you without striking you.

When you're casting a spell, both you and your opponent go into temporary slow-mo. This is accomplished by turning down the powder toy simulation rate. 

This turns Gunpowder Plot from a game of twitch reflexes like WOL into a game of wizardly creativity and strategy, like Dresden.

Movement slows down, but sigil spellcasting remains at the same speed. During the slowdown period, both you and the enemy caster will prepare sigil spells. Then, as time speeds up again after both of you are done casting, everything will resolve. Explosively. This is the right time to dodge. This creates a fun two-sided dominant strategy of attacking then dodging.

With this, the game becomes spell rock paper scissors, except you have 8 spells on hand and can invent any spell you can imagine. You'll have to create attacks, defenses, and movement spells, only for all of them to resolve in one big burst. The goal is to require the player to outthink their opponent instead of outplaying them.