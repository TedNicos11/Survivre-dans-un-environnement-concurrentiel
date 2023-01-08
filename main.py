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
         ##  Méthode qui attributs les id
    def give_id(self):
        regex = string.ascii_letters+string.digits+string.punctuation
        return "".join([regex[random.randint(0,len(regex)-1)] for _ in range(10)])

    
    ### Méthode qui permet a un agent d'observer N x N tuile autour d'elle et renvoit la liste de ses voisins
    def get_voisin_tuile(self ,x ,y) -> List[Tuile]:
        voisins = []
        for i in range(-1,2):
            for j in range(-1,2):
                nx = x + i
                ny = y + j
                ## verifie que  les limites ne sont pas en dehors de la taille du tableau de tuile
                if(nx >= 0 and ny >= 0 and nx < Map.taille and ny < Map.taille):
                    voisins.append(Map.get_tuile( nx , ny ))
        return voisins
    
        
        
    ### ajouter une tuile dans une liste de déplacement valide fait par un agent
    def get_voisin_valid(self) -> List[Tuile]:
        x = self.tuile.x
        y = self.tuile.y
        voisins_valides = []
        # récupère les coordonnées d'une tuile
        voisins = self.get_voisin_tuile(x , y)
        for voisin in voisins:
            #
            if not voisin.isnot_empty():
                #if self.event(voisin):
                    
                    voisins_valides.append(voisin)
                #
        return voisins_valides
  
    ### Méthode qui renvoit la tuile dans laquelle l'agent va se déplacer(
    def next_move(self) -> Tuile:
        voisin_valide = self.get_voisin_valid()
        #voisin_valide = self.get_voisin_isFood()
        index = random.randint(0 ,len(voisin_valide)-1)
        voisin_valide[index]
        return voisin_valide[index]
    
    ###  Déplacer un agent vers une autre tuile
    def deplacer(self) -> None:
        """
        on récupere le prochain movement
        et on vide la tuile précédente en affectant à la nouvelle tuile suivante
        le prochain déplacement et on recupere les coordonnées de cette tuile
        de telle sorte que l'objet connaisse sur quelle tuile il est placer et vise versa
        """
        next_tile = self.next_move()
        #next_tile.envent()
        self.tuile.empty_tile()
        self.tuile = next_tile
        next_tile.set_value(self)


    
  
    
class Isinstance:
    def __init__(self):
        self.cat = Chat()
        self.mouse = Souris()
                    
#classe fille heritant de la super classe
class Chat(Agent):
    def __init__(self) -> None:
        super().__init__('😾')
        # self.valeur_affichage='\U0001F408'
    """
    
  def eat_mouse(self):
        x = self.tuile.x
        y = self.tuile.y
        voisins = self.get_voisin_tuile(x , y)
        for voisin in voisins:
            if voisin.is_cat():
                if voisin.is_mouse:
                    voisin.set_eat()
        return voisin"""
    """  
    def eat_mouse(self):
        Isins =Isinstance()
        for i in range(Map.taille):
            for j in range(Map.taille):
                self.tuile = Tuile(i,j)
                if Isins.mouse.tuile.i == Isins.cat.tuile.i and Isins.mouse.tuile.j == Isins.cat.tuile.j :
                    del mouse.valeur_affichage
        return Isins.cat"""
    

    def eat_mouse(self):
        Isins =Isinstance()
        x =random.randint(0 ,Map.taille -1)
        y =random.randint(0 ,Map.taille -1)
        voisins = self.get_voisin_tuile(x , y)
        for voisin in voisins:
            if voisin.is_mouse() and voisin.is_cat():
                if not voisin.isnot_empty():
                    if Isins.mouse.tuile.i == Isins.cat.tuile.i  and Isins.mouse.tuile.j == Isins.cat.tuile.j:
                        del mouse.valeur_affichage
                         
            
        

class Souris(Agent):
    def __init__(self) -> None:
        super().__init__(None)
        self.valeur_affichage='🐭'
        #self.valeur_affichage='S'
    
        
class Food(Affichable):
    def __init__(self) -> None:
        super().__init__('🃏')
        #self.valeur_affichage='\U0001F33D'
        
class Map:
    """definition de la grille de taille ['taille']"""
    taille = 0
    Grille = []
    def __init__(self,taille) -> None:
        Map.taille = taille
        for i in range(taille):
            Map.Grille.append([])
            for j in range(taille):
                tuile = Tuile(i,j)
                Map.Grille[i].append(tuile)
        # self.Grille = [[ Tuile() ]*(self.taille)  for i in range(self.taille)] ### une Map est une matrice de Tuile
        self.draw_walls()

    ### Méthode pour ajouter un affichable à une position aléatoire sur la map
    def add_affichable_on_map(self, agent) -> Affichable:
        while True:
            x=random.randint(0,self.taille-1)
            y=random.randint(0,self.taille-1)
            tuile = self.get_tuile(x,y)
            if tuile.is_empty():
                tuile.set_value(agent)
                agent.set_tuile(tuile)
                break
            elif not tuile.isnot_empty() and tuile.is_cat()== tuile.is_mouse():
                #tuile.set_value()
                agent.set_tuile(tuile)
                break
            elif not tuile.isnot_empty() and tuile.is_food()== tuile.is_mouse():
                self.add_food_on_map()
            
    

    def add_cat_on_map(self) -> Chat:
        chat = Chat()
        self.add_affichable_on_map(chat)
        chat.eat_mouse()
        return chat

    def add_mouse_on_map(self) -> Souris:
        souris = Souris()
        self.add_affichable_on_map(souris)
        return souris

    def add_food_on_map(self) -> Food:
        nourriture = Food()
        self.add_affichable_on_map(nourriture)
        return nourriture


    ### Méthode pour récupérer une tuile à une position x, y
    @classmethod
    def get_tuile(cls, x, y) -> Tuile:
        return cls.Grille[x][y]
    
    @classmethod
    def efface_ecran(cls):
         
        if sys.platform.startswith("win"):
           #if os is windows
           os.system("cls")
        else:
            #if os is linux
            os.system("clear")
             
            
    def draw_walls(self):
        #construction des cellule mur sur le map
        x, y = 0, self.taille // 2
        for _ in range(y, self.taille):
            tuile = self.get_tuile(x,_)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)
            
        x, y = (self.taille // 3) - 2, 1
        for _ in range(y, self.taille - 3):
            tuile = self.get_tuile(x,_)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x , y = (self.taille // 3) - 1, self.taille // 2
        for _ in range(x, y+2):
            tuile = self.get_tuile(_,y)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x , y = self.taille // 2, (self.taille // 3) - 1
        for _ in range(x, y+8):
            tuile = self.get_tuile(_,y)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x ,y = (self.taille-4) ,1
        for _ in range(y,self.taille-7):
            tuile = self.get_tuile(x,_)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x , y = (self.taille-1),0
        for _ in range(y,self.taille//2):
            tuile = self.get_tuile(x,_)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x , y= (self.taille//2)+3 ,self.taille -3
        for _ in range(x,y):
            tuile = self.get_tuile(_,y)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x , y = 0,0
        for _ in range(y,y+2):
            tuile = self.get_tuile(x,_)
            mur = CelluleMur(tuile)
            tuile.set_value(mur)

        x , y = 1,0
        for _ in range(self.taille):
            if _ == 0:
               tuile = self.get_tuile(x,_)
               mur = CelluleMur(tuile)
               tuile.set_value(mur)
            elif _ == 14:
                 tuile = self.get_tuile(x,_)
                 mur = CelluleMur(tuile)
                 tuile.set_value(mur)
        x , y = self.taille-1 , 0
        for _ in range(self.taille):
            if _ == 14 or _==13:
               tuile = self.get_tuile(x,_)
               mur = CelluleMur(tuile)
               tuile.set_value(mur)
        x , y = self.taille-2 ,0
        for _ in range(y,self.taille):
            if _ == 0 or _ == self.taille-1:
               tuile = self.get_tuile(x,_)
               mur = CelluleMur(tuile)
               tuile.set_value(mur)

    def console_display(self):
        for row in self.Grille:
            line = ""
            for tile in row:
                line = line + tile.get_icon()
            print(f"{line}")
        
        #print()


        
_map = Map(15)

mouse = _map.add_mouse_on_map()
cat = _map.add_cat_on_map()
mouse1 = _map.add_mouse_on_map()
cat1 = _map.add_cat_on_map()
mouse2 = _map.add_mouse_on_map()
cat2 = _map.add_cat_on_map()
mouse3 = _map.add_mouse_on_map()
mouse4 = _map.add_mouse_on_map()
mouse4 = _map.add_mouse_on_map()
food=_map.add_food_on_map()
food1=_map.add_food_on_map()
food2=_map.add_food_on_map()
food3=_map.add_food_on_map()
food4=_map.add_food_on_map()
food5=_map.add_food_on_map()
food6=_map.add_food_on_map()
food7=_map.add_food_on_map()
food8=_map.add_food_on_map()
food9=_map.add_food_on_map()
food10=_map.add_food_on_map()


while True :
    cat.deplacer()
    cat.eat_mouse()
    cat1.deplacer()
    cat1.eat_mouse()
    cat2.deplacer()
    cat2.eat_mouse()
    mouse.deplacer()
    mouse1.deplacer()
    mouse2.deplacer()
    mouse3.deplacer()
    mouse4.deplacer()
    cat.eat_mouse()
    _map.efface_ecran()
    _map.console_display()



    time.sleep(1)
 