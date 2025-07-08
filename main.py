import pygame
import sys
import json
import os
from Files import config 
from Files import textures_manager
from Files import Lecteur_map as lecteur
pygame.init()


print()
#horloge Interne
horloge = pygame.time.Clock()
FPS = config.FPS


# Fenêtre
largeur_fenetre, hauteur_fenetre = config.get_dimensions()

pygame.display.set_caption("Menu de jeux")
flags = pygame.RESIZABLE
# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), flags)
# Définit le titre de la fenêtre
pygame.display.set_caption(config.Titre) 

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
DARK_BLUE = (0, 51, 102)
BLACK = (0, 0, 0)

#taille bouton
BT_width = config.taille_BT_w
BT_height = config.taille_BT_h

# Dimensions de la grille
taille_cellule = config.taille_cellule


# récupérer grille avec les valeur en int
largeur_grille, hauteur_grille, grille = lecteur.chargerfichier()

# Calculer les coordonnées mondiales du centre de la grille
# C'est la position *idéale* du joueur dans le monde
centre_grille_x_monde = (largeur_grille // 2) * taille_cellule
centre_grille_y_monde = (hauteur_grille // 2) * taille_cellule

# Couleurs
couleur_grille = (100, 100, 100)
couleur_cellule = (200, 200, 200)


# Position initiale de la caméra
camera_x = 0
camera_y = 0


# --- Ajout du joueur ---
# Dimensions et couleur du joueur
taille_joueur = config.taille_joueur
couleur_joueur = (255, 255, 0) # Bleu

# Position initiale du joueur au centre de l'écran (ne bouge pas par rapport à la fenêtre)
joueur_x_fixe = (largeur_fenetre - taille_joueur) // 2
joueur_y_fixe = (hauteur_fenetre - taille_joueur) // 2
# --- Fin Ajout du joueur ---

# déclaraton de l'emplacement "imaginaire" du joueur avec pour référentiel la grille
position_player = pygame.Rect(joueur_x_fixe, joueur_y_fixe, taille_joueur, taille_joueur)
# ajustabilité des positions pour la "hitbox" (jsp comment cela s'écrit mdr)
position_player.x = centre_grille_x_monde + 0
position_player.y = centre_grille_y_monde + 0

#récupère la grille avec les emplacements de texture
grille, collision_map = textures_manager.placer_texture(taille_cellule, largeur_grille, hauteur_grille, grille)


# Police
font = pygame.font.SysFont(None, 50)



# Bouton classique
def draw_button(text, x, y, w, h, color, hover_color, action_name):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(fenetre, hover_color, (x, y, w, h))
        if click[0] == 1:
            return action_name
    else:
        pygame.draw.rect(fenetre, color, (x, y, w, h))

    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
    fenetre.blit(text_surf, text_rect)
    return None

# Menu principal
# La fonction menu_scene doit aussi prendre les événements en paramètre
def menu_scene(events, largeur_fenetre, hauteur_fenetre): # <-- Ajout de 'events'
    fenetre.fill(BLACK)
    
    #nombre de bouton
    nb_BT = 4
    compteur_BT = 0
    
    #result = draw_button(text, x, y, w, h, color, hover_color, action_name)
    result = draw_button("Game", (largeur_fenetre - BT_width) // 2 ,(hauteur_fenetre  - BT_height ) // 2 -100 -25 *nb_BT + compteur_BT * 100,  BT_width ,  BT_height, BLUE, DARK_BLUE, "jeu")
    compteur_BT += 1
    if result:
        return result
    result = draw_button("Charger", (largeur_fenetre - BT_width) // 2 ,(hauteur_fenetre  - BT_height ) // 2 -100 -25 *nb_BT + compteur_BT * 100,  BT_width ,  BT_height, BLUE, DARK_BLUE, "quit")
    
    compteur_BT += 1
    if result:
        return result
    result = draw_button("Save", (largeur_fenetre - BT_width) // 2 ,(hauteur_fenetre  - BT_height ) // 2 -100 -25 *nb_BT + compteur_BT * 100,  BT_width ,  BT_height, BLUE, DARK_BLUE, "quit")
    
    compteur_BT += 1
    if result:
        return result
    result = draw_button("Quit", (largeur_fenetre - BT_width) // 2 ,(hauteur_fenetre  - BT_height ) // 2 -100 -25*nb_BT + compteur_BT * 100,  BT_width ,  BT_height, BLUE, DARK_BLUE, "quit")
    
    
    # Gérer les événements spécifiques au menu ici si nécessaire (ex: touches clavier)
    for event in events: # <-- Utilisation des événements passés en paramètre
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Exemple : quitter le menu avec ESC
                print("ESC pressée dans le menu")
                return "quit"

    return "menu"


# Boucle principale avec gestion de scène
def run(largeur_fenetre, hauteur_fenetre):
    current_scene = "menu"
    while True:
        # COLLECTE UNIQUE de TOUS les événements pour cette frame
        events = pygame.event.get() 
        keys_pressed = pygame.key.get_pressed()
        # Traitement des événements globaux (comme quitter le jeu depuis n'importe quelle scène)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 2. Détecter l'événement de redimensionnement de la fenêtre
            elif event.type == pygame.VIDEORESIZE:
                # Récupérer les nouvelles dimensions
                largeur_fenetre = event.w
                hauteur_fenetre = event.h
                
                
                
                # Mettre à jour la taille de la surface d'affichage de Pygame
                # C'est important pour que Pygame puisse redimensionner le "canvas" interne.
                fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), pygame.RESIZABLE)
                
        # Appel de la scène actuelle, en lui passant TOUS les événements collectés
        if current_scene == "menu":
            current_scene = menu_scene(events, largeur_fenetre, hauteur_fenetre) # <-- Passe les événements
        elif current_scene == "jeu":
            current_scene = jeu_scene(events, camera_x, camera_y) # <-- Passe les événements
        
        # Gestion des changements de scène (quit est déjà traité au-dessus, mais c'est bien de l'avoir ici aussi)
        if current_scene == "quit":
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        horloge.tick(FPS)

















# Jeu
def jeu_scene(events, camera_x, camera_y): # <-- Ajout de 'events' (pour la gestion des évènements)
    #Gère la logique et le rendu de la scène de jeu principale

    #Args:
        #events (list): Liste des événements Pygame collectés depuis la boucle principale.
        #camera_x (int): Position X  actuelle de la caméra.
        #camera_y (int): Position Y actuelle de la caméra.

    #Returns:
        #str: Le nom de la scène suivante ("jeu" pour rester, "menu" pour retourner au menu)
    
    
    #variables à réinitialiser à chaque boucle:
    #deplacement vitesse
    vitesse = config.vitesse
    
    # Stocke la position du joueur et de la caméra AVANT tout calcul de mouvement
    # Utile pour la détection de collision afin de pouvoir "revenir en arrière" (en focntion des axes)
    ancienne_position_x = position_player.x
    ancienne_position_y = position_player.y
    ancienne_camera_x = camera_x
    ancienne_camera_y = camera_y
    
    
    # --- Gestion des événements spécifiques à la scène de jeu ---
    # Parcourt les événements collectés une seule fois par la boucle principale du jeu.
    for event in events: # <-- Utilisation des événements passés en paramètre, PLUS DE pygame.event.get() ici
        # Détecte n'importe quelle touche pressée
        if event.type == pygame.KEYDOWN:
            # Ajout d'une détection pour ESC pour revenir au menu, comme indiqué dans le texte d'aide
            if event.key == pygame.K_ESCAPE:
                # Si vous voulez quitter le jeu et revenir au menu avec 'A'
                return "menu" # <-- Changement ici pour revenir au menu
    
    # --- Gestion du déplacement du joueur par les touches ---
    # Obtient l'état actuel de toutes les touches du clavier (quelles touches sont pressées).
    keys_pressed = pygame.key.get_pressed()
    # Modifie la vitesse du joueur si la touche 'Maj Gauche' (LSHIFT) est pressée.
    vitesse += vitesse * keys_pressed[pygame.K_LSHIFT]
    deplacement_x = (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) - (keys_pressed[pygame.K_q] or keys_pressed[pygame.K_LEFT])
    deplacement_x *= vitesse
    
    deplacement_y = (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) - (keys_pressed[pygame.K_z] or keys_pressed[pygame.K_UP])
    deplacement_y *= vitesse
    
    # Appliquez le mouvement désiré au joueur sur X
    position_player.x += deplacement_x
    
    
    # --- Détection de collision sur l'axe X (Optimisé par grille) ---
    # Optimisation de la détection de collision : Seules les cellules à proximité du joueur sont vérifiées
    # Calcule la plage des indices de grille (min_gx à max_gx) que le joueur pourrait toucher
    # après son déplacement sur l'axe X. Une marge de +/- 1 cellule est ajoutée (-1 pour min, +1 pour max)
    # pour s'assurer de ne rater aucune collision, même avec des mouvements rapides ou aux bords des cellules.
    min_gx = int(position_player.left // taille_cellule) -1
    max_gx = int(position_player.right // taille_cellule) +1
    min_gy = int(position_player.top // taille_cellule) -1 # Inclure Y pour avoir la zone de vérification
    max_gy = int(position_player.bottom // taille_cellule) +1
    
    
    # Limiter les indices aux bords de la grille
    # S'assure que les indices calculés restent dans les limites valides de la grille
    min_gx = max(0, min_gx)
    max_gx = min(largeur_grille - 1, max_gx)
    min_gy = max(0, min_gy)
    max_gy = min(hauteur_grille - 1, max_gy)
    
    
    # Parcourt uniquement les cellules de la grille potentiellement en collision avec le joueur.
    for y_grid in range(min_gy, max_gy + 1):
        for x_grid in range(min_gx, max_gx + 1):
            # Vérifie si la cellule actuelle (x_grid, y_grid) est un bloc de collision.
            if (x_grid, y_grid) in collision_map:
                # Récupère l'objet Rect représentant le bloc de collision.
                bloc_rect = collision_map[(x_grid, y_grid)] 

                if position_player.colliderect(bloc_rect):
                    # Si le joueur se déplaçait vers la droite
                    if deplacement_x > 0:
                        position_player.right = bloc_rect.left
                    # Si le joueur se déplaçait vers la gauche
                    elif deplacement_x < 0:
                        position_player.left = bloc_rect.right

    
    
    
    # --- Application du mouvement et détection de collision (axe Y) ---
    # Applique le déplacement calculé à la position Y du joueur.
    position_player.y += deplacement_y
    
    # Optimisation de la détection de collision : Seules les cellules à proximité du joueur sont vérifiées
    # Calcule la plage des indices de grille (min_gx à max_gx) que le joueur pourrait toucher
    # après son déplacement sur l'axe X. Une marge de +/- 1 cellule est ajoutée (-1 pour min, +1 pour max)
    # pour s'assurer de ne rater aucune collision, même avec des mouvements rapides ou aux bords des cellules
    min_gx = int(position_player.left // taille_cellule) -1
    max_gx = int(position_player.right // taille_cellule) +1
    min_gy = int(position_player.top // taille_cellule) -1
    max_gy = int(position_player.bottom // taille_cellule) +1
    
    # S'assure que les indices calculés restent dans les limites valides de la grille.
    min_gx = max(0, min_gx)
    max_gx = min(largeur_grille - 1, max_gx)
    min_gy = max(0, min_gy)
    max_gy = min(hauteur_grille - 1, max_gy)
    
    # Parcourt les cellules potentiellement en collision pour l'axe Y.
    for y_grid in range(min_gy, max_gy + 1):
        for x_grid in range(min_gx, max_gx + 1):
            if (x_grid, y_grid) in collision_map:
                bloc_rect = collision_map[(x_grid, y_grid)]
                

                if position_player.colliderect(bloc_rect):
                    # Si le joueur se déplaçait vers le bas
                    if deplacement_y > 0:
                        position_player.bottom = bloc_rect.top
                    # Si le joueur se déplaçait vers le haut
                    elif deplacement_y < 0:
                        position_player.top = bloc_rect.bottom
    

    # --- Mise à jour de la caméra ---
    # La caméra est ajustée de manière à ce que le joueur reste "fixe" au centre de l'écran
    camera_x = joueur_x_fixe - position_player.x # joueur_x_fixe est le centre X de l'écran pour le joueur
    camera_y = joueur_y_fixe - position_player.y # joueur_y_fixe est le centre Y de l'écran pour le joueur
    
    
    
    
    
    # --- Rendu graphique de la scène ---
    
    # Dessiner la grille
    # Efface l'écran en le remplissant de noir. Cela supprime tous les dessins de la frame précédente.
    fenetre.fill((0, 0, 0))

    # --- Calculer la zone visible de la grille ---

    # Coordonnées monde du coin supérieur gauche de l'écran
    world_x_start_screen = -camera_x
    world_y_start_screen = -camera_y

    # Coordonnées monde du coin inférieur droit de l'écran
    world_x_end_screen = world_x_start_screen + largeur_fenetre
    world_y_end_screen = world_y_start_screen + hauteur_fenetre

    # Convertir ces coordonnées monde en indices de grille
    start_grid_x = int(world_x_start_screen // taille_cellule) -1 #+6
    end_grid_x = int(world_x_end_screen // taille_cellule) +1 #-5 # +1 

    start_grid_y = int(world_y_start_screen // taille_cellule) -1 #+2
    end_grid_y = int(world_y_end_screen // taille_cellule) +1 #-1 # +1 
    # S'assurer que les indices restent dans les limites de la grille réelle
    start_grid_x = max(0, start_grid_x)
    end_grid_x = min(largeur_grille, end_grid_x) # Ne pas dépasser largeur_grille - 1, mais range va jusqu'à end-1
    start_grid_y = max(0, start_grid_y)
    end_grid_y = min(hauteur_grille, end_grid_y) # Ne pas dépasser hauteur_grille - 1


    # --- Dessiner uniquement les cellules visibles ---
    for y in range(start_grid_y, end_grid_y):
        for x in range(start_grid_x, end_grid_x):
            # Calcule la position de la cellule à l'écran
            screen_x = x * taille_cellule + camera_x
            screen_y = y * taille_cellule + camera_y

            # Crée un objet pygame.Rect pour la position à l'écran
            rect = pygame.Rect(screen_x, screen_y, taille_cellule, taille_cellule)

            # Dessine le contour du rectangle de la cellule
            #(Ces lignes sont souvent supprimées dans le jeu final pour ne dessiner que les textures)
            pygame.draw.rect(fenetre, couleur_cellule, rect)
            pygame.draw.rect(fenetre, couleur_grille, rect, 1)

            # Dessine la texture en fonction de la grille
            if grille[y][x] is not None:
                fenetre.blit(grille[y][x], rect)
    
    
    # --- Dessiner le joueur ---
    # Dessine le joueur à sa position fixe, par-dessus la grille
    pygame.draw.rect(fenetre, couleur_joueur, (joueur_x_fixe, joueur_y_fixe, taille_joueur, taille_joueur))
    # --- Fin Dessiner le joueur ---
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return "jeu"
run(largeur_fenetre, hauteur_fenetre)