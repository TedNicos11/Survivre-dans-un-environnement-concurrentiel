import random
import string
from typing import List
import time ,os ,sys
#classe composante
class Tuile:
    def __init__(self,x_pos : int,y_pos : int) -> None:
        self.x = x_pos
        self.y = y_pos
        ### Une tuile contient un affichable. Par défaut, elle contient une CelluleVide
        self.valeur = CelluleVide(self)

    ### Méthode pour savoir si une tuile est vide ou non
    def is_empty(self) -> bool:
        return isinstance(self.valeur ,CelluleVide)
    ### 
    def isnot_empty(self) -> bool:
        return isinstance(self.valeur ,CelluleMur)

    ###
    def is_mouse(self) -> bool:
        return isinstance(self.valeur ,Souris)
    ###
    def is_cat(self) -> bool:
        return isinstance(self.valeur,Chat)

    
    ###
    def is_food(self) -> bool:
        return isinstance(self.valeur ,Food)

   

    ###
    """
    def conflit(self ,affichable):
        next_tile = self.next_move()
        affichable.next_tile = self.deplacer(affichable) 
        if affichable.next_tile == self.set_value(affichable):
            affichable.set_value(affichable)

        if agent.next_tile == self.set_value(agent):"""

    ### Méthode pour savoir qu'une tuile contien un agent ou non
    ##def is_affichable(self) -> bool:
        #return isinstance(self.valeur ,Agent)

    ### Méthode pour affecter un affichable à une tuile
    def set_value(self, affichable) -> None:
        self.valeur = affichable
        affichable.tuile = self
        
    ### Méthode qui renvoit la valeur affichable d'un affichable
    def get_icon(self) -> str:
        return self.valeur.get_icon()

    def empty_tile(self) -> None:
        self.set_value(CelluleVide(self))
        
class Affichable:
    """
    affiche un element de la cellule
    
    """

    def __init__(self, valeur_affichage) -> None:
        self.valeur_affichage = valeur_affichage
        self.tuile = None
    
    def set_tuile(self, tuile: Tuile) -> None:
        self.tuile = tuile

    def get_icon(self) -> str:
        return self.valeur_affichage

    def set_eat(self):
        self.valeur_affichage = None
        return self.valeur_affichage
    
class CelluleVide(Affichable):
    """
    creation de cellule vide dans la liste 2D
    
    """
    
    def __init__(self, tuile : Tuile) -> None:
        super().__init__('\u2B1C')
        self.tuile = tuile
        
class CelluleMur(Affichable):
    """
    creation de cellule non vide dans la liste 2D

    """
    
    def __init__(self, tuile: Tuile) -> None:
        super().__init__('\u2B1B')
        self.tuile = tuile

# super classe Agent       
class Agent(Affichable):
    sex = ["F","M"]
    dureVieMax = 10
    def __init__(self, valeur_affichage: str) -> None:
        super().__init__(valeur_affichage)
        id = Agent.give_id(self)
        self.sexe = Agent.sex[random.randint(0,1)]
        self.dureVie = Agent.dureVieMax
        i = random.randint(0,Map.taille - 1)
        j = random.randint(0,Map.taille - 1)
        self.tuile = Tuile(i,j)