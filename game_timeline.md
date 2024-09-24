I have 45 days until I'm flat broke. This was 100% my own choice: I paid 25,000$ for pescolito's school and in general invested heavily in having a wife. Now, I need to grow up and have some balls. If BDG can do it, so can I.

Publishing on steam takes a two week runup period. This means I have roughly 30 days to create a publishable game. If I can do it in less, then I won't be as fucking stressed out.

I have a magic system, NPC AI, and a game structure and mechanics. I have all my tech planned out, all we're doing now is building.

## Core Elements:

Powder Magic API

Gunpowder Plot game engine (combat and destructible terrain)

a touch of LLM integration. Use the tech that you already have tested for this, don't go crazy.

ros to tie everything together


## Supplements

Generative level engine. Themes for all 5 worlds, seed art for each of them, varied level structures, perhaps a special challenge on each level. This challenge should come in the form of Powder Toy obstacles or interactables within the physics engine. Shit is more fun to build in Powder Toy anyway. I want Powder Toy to be my principle design tool and game engine. Godot is mostly for utility.

Demon King design and testing. Now he only needs to be an isolated boss battle, so I can basically just make him a smart dude with spells customized to counter you and a shitton of mana and health. He has a shit ton of LLM processing time (anytime you're not using it), and I should abuse that to generate and iterate on the nastiest spells possible. He can use the General boss fights as data, testing spells in those battles and taking the most effective one from each General. He will also have 3 spells of his own, totally unexpected.

Demon King steam servers. Allll we need to store is spells (and maybe the core beliefs that go with them).

Leaderboards? For best Demon King slain?

Menu system
 - Settings
   - Accessibility

Save system



The DM's world can and should absolutely have many dynamic powder elements like flowing water, fire, electricty, vines, etc. It makes thr world dynamic and exciting and gives the DM more design options to play with.




## Plot Adjustments

In Gunpowder Plot, you always start out as an unnamed NPC. It's more in keeping thematically and it gives the "Link" effect.

The unamed NPC leaves their home and goes out into the world to defeat the Demon King. If they die, a different NPC takes up the mantle.

To make this work, enemies need to be common and recruitable NPCs need to be rare. Mana can be gained by defeating Generals or completing challenges. Recruitable NPCs already have some magic of their own. You can choose whether to enhance that magic by granting them useful spells. Or, you can kill them, and you will gain their mana.

NPCs are extraordinarily valuable because they act as extra lives. NPCs cannot take damage, but you can. Whenever you lose all your playerium, an NPC will sacrifice itself for you, replenishing your life at the cost of its own. When an NPC sacrifices itself for your life, it becomes a spirit creature and run away. When an NPC sacrifices itself for your mana, it becomes a soulless zombie and tries to attack you. You'll have to put it down.

Generals have 3 or 4 NPCs each. When you kill the General, you'll gain their NPCs. There are a few other ways to get them, but this is the main one.



## Demon King Phases:

In the first phase, NPCs that sacrifice themselves for your life during the Demon King fight will not escape, but will instead increase the Demon King's mana. In his first phase, the Demon King has his own cadre of NPCs that he uses as meat shields. He doesn't do much fighting himself, letting his goons wear you down until you can hit him as he dodges.

In his second phase, the Demon King kills all his NPCs and takes their life and mana. He now attacks you directly with powderful sigils.

In the third phase, he kills all of your NPCs one by one, taking their life and mana as he does. His sigils grow more powerful as he gains more mana. You'd do well to kill your companions yourself to deny him the power.

Once the Demon King absorbs all your NPCs, he enters the forth phase, saying "In this world of just you and me... what is reality, really?"
The Demon King gains limited power over the World Sigil. He starts destroying powder everywhere with destructive spells. Instead of being replaced, acid, fire, and lava flow out from every damaged area of the world. Even the background layer becomes untraversable in places. The battle of sigils continues, but now over uncertain and dangerous terrain.

In the fifth stage, the Demon King traps you in a Nightmare Sigil. This sigil is the opposite of a World Sigil. It takes all the damage data from the completed World Sigil and creates a world composed of your deadliest enemies and most hated traps. Generals appear in this world, taunting you about when you took damage to them and recasting the spells that hurt you most. The very walls close in behind you, summoning lava and acid that leaves only one path forwards, forever closing. There is no fighting back, only a desperate struggle for your life.

The fifth stage is the final stage, looping until the player defeats the Demon King. The Nightmare Sigil will be cast every time the Demon King reaches full mana. Every time the Nightmare Sigil is cast, it will be improved with data of how the player was damaged on the last round. Each Nightmare Sigil will run for 30 seconds, then the player will have an opportuinity to damage the Demon King for a brief period. Once the player depletes all the Demon King's HP, they win Gunpowder Plot. They will unlock a powerful new ability for the next run (probably permanent persona upgrades, allowing them persona spells from the start of the game).



## NPC Fights

Players can take NPCs through the game with them as blood bags or pop them for mana at any point. A balance between offense and defense. When an NPC is sacrificed to save you, their potential mana is lost, so there is an element of risk and reward.

Almost all enemies fight you with your own gunpowder zone. Some special enemies, the Generals, and the Demon King have their own zones. All other enemies manifest elemental attacks or summon ephemeral bodies of acid or fire to harm you. Obviously, these attacks are only effective within your gunpowder zone. You always have a zone active once you gain mana, so enemies are always a threat to you. NPC casters take advantage of your gunpowder zone to supplement your spells, but are immune to damage, as they have no zones of their own.

All enemy's bodies are composed of sigils. These sigils manifest powder that represents the enemy. Enemies are defeated when the playerium core inside of them has its HP depleted.


## AI Systems

Upgrade mechanism for spells:
When I get to a special altar, just ask the DM to upgrade the spell somewhat lmao. It's just that easy. The player can specify the upgrade as a verb: reduce cost, increase firepower, add poison, etc etc etc. It's a good and simple system.

Multiplayer system:
All players have mana, but their zones are permanently active and merged. Players cannot move outside of the shared zone, which will be pretty hilariously small at first, like a clown car. The zone will grow as the players gain mana.

For this design, the only Powder Toy we need running is the host's. 