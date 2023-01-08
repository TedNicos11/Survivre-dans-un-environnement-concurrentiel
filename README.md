# Project Description

It is the game of life in which two types of entities are considered: the mouse and the cat. The mouse and the cat feed, fight and negotiate their way through procedurally generated environments to outdo other mice and cats trying to do the same. In this game, the world is considered to have a beginning and an end that can be set at the start of the game. At its end, a dashboard presenting the entities and their remaining life. The objective is to simulate populations of agents in procedurally generated virtual worlds. It is inspired by classic massively multi-agent online role-playing games. We consider that:

- The game starts with a map composed of NxN tiles (set at the beginning of the game); 
- In each tile, only one agent can be present. In some cases, two agents of the same species can be present only if one is a man and the other a woman. In this case, in a number of instances, these agents give birth to babies and all agents move to adjacent tiles, leaving the female in the current tile. 
- Corn appears randomly on the tiles - Mice and cats must eat to survive 
- Cats eat mice and mice eat corn - If a cat and a mouse meet in a tile, the cat will kill the mouse and if the cat is not satiated, it will eat the mouse 
- If an entity has not eaten for a certain amount of time, it will die 
- Two entities of the same sex must not meet in the same tile - Each entity can do several actions: move, eat, breed. 
- Each entity can observe NxN tiles around it - If an entity leaves the map, it will die


# Objective:
The main objective of the overall exercise is to enable students to understand how to use OOP
techniques to develop software. On the other hand, they will learn how to implement software using object-oriented programming techniques.
object-oriented programming techniques. Thus, in a first step, the students will collect data on some of their daily activities. Later, they will use this data to design and develop an application.

# Installation & Launching 
Run the project using the command on (windows / linux): python3 main.py