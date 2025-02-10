# OTzav
OT_Game_2024 - Game Design Document
The repository contains a prototype implementation of a game in Pygame, developed as part of the Object Technologies course. The project demonstrates essential game mechanics and serves as an example for students developing their final project.

Author: Martin Lyžičiar
Chosen Theme: 4 Elements



1. Introduction
This game was created for the Object Technologies course to demonstrate turn-based combat mechanics with elemental interactions. The game features a player-versus-enemy battle system where the player selects elemental attacks and plays strategically to defeat multiple waves of enemies.

1.1 Inspiration
The game draws inspiration from titles such as:

Slay the Spire
A strategic deck-building game where players choose cards to attack enemies while managing resources.

Genshin Impact (Elemental Reactions)
A game that uses elemental interactions where different elements react together to create stronger attacks and effects.

1.2 Player Experience
The player fights waves of enemies using elemental attacks. By choosing the right elements and matching cards, the player can increase attack power and trigger elemental reactions for bonus damage. The goal is to defeat the final boss and earn skill points to upgrade abilities.

1.3 Development Software
Pygame-CE → Game development framework
PyCharm 2024.1 → IDE used for programming
Me → Source for graphical assets



2. Concept

2.1 Gameplay Overview
The player selects an element at the start of each turn.
The player chooses two cards that match the chosen element to increase attack power.
The player attacks the enemy, triggering damage or elemental reactions.
The enemy fights back after the player's turn.
When an enemy is defeated, the next enemy spawns.
If all enemies are defeated, the boss battle begins.
After defeating the boss player gains skill points to enhance his abilities such as the power of his element, the chances for the element to appear and the maximum elemental cards picked per turn.

2.2 Theme Interpretation (4 elements)
The game revolves around elemental strategy:

The four elements are Fire (F), Water (W), Earth (E), and Lightning (L).
Matching elements boosts attack, while combining elements triggers reactions.
After every wave of enemies, the boss battle takes place.

2.3 Primary Mechanics
Element Selection: The player chooses one of four elements at the start of their turn.
Elemental cards managment: Managing the elemental cards player can choose from.
Card Matching: The player selects two cards to boost their attack power based on the selected element.
Elemental Reactions: Combining elements triggers special effects.
Skill Points System: After defeating the boss, the player earns skill points to upgrade elemental power and card selection chances.

2.4 Class Design
Main: Handles the main game logic (UI, combat loop).
Player: Manages the player character, health, upgrades, and skill points.
Enemy: Handles enemy behavior, waves, turns, and attacks.
Element: Stores elemental properties, damage calculation, and reactions.
Card: Represents elemental cards used for attacks.
CardManager: Functions to manage elemental cards
Upgrade Menu: Allows skill point spending for upgrades.
Figure: Placeholder for character design and player damage taken or healed display, enemy applied element and status effect.
HealthBar: HealthBars for Characters.



3. Art

3.1 Visual Style
The game uses a minimalistic 2D art style focusing on:

Elemental colors for visual clarity
Simple UI components like buttons and menus
Effects to highlight attacks and reactions

3.2 UI Design
The player and enemy figures display status effects and damage taken.
Health bars dynamically update based on damage taken.
A floating damage text effect appears after player takes damage for 1 second before disappearing.
Same for player healing
The Upgrade Menu allows players to enhance abilities after defeating the boss.



4. Game Experience

4.1 UI Elements
Element selection buttons (for Fire, Water, Earth, Lightning)
Card selection system for attack strategy
Enemy waves & health bars for progress tracking
Floating damage numbers & status effects
UpgradeMenu
    Two Buttons for each element. First for element level, second for element probability followod by current values respectively.
    Button for increasing elemental cards used per turn.
    Current skill points display. Button for closing the UpgradeMenu.
    Upgrades prices are: element level+ for 1 Skill point
                         element probabilityx for 2 skill points
                         elemental cards used per turn for 3 skill points


5.2 Controls
Mouse:
Left Click: Selects elements, cards, reset cards and upgrade menu options
Keyboard:
U: Opens the upgrade menu
