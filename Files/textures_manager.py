import pygame

def placer_texture(taille_cellule,largeur_grille,hauteur_grille, grille):
    try:
        floor = pygame.image.load("Assets/ciel.png").convert_alpha()
        floor = pygame.transform.scale(floor, (taille_cellule, taille_cellule))
        mur = pygame.image.load("Assets/pierre.png").convert_alpha()
        mur = pygame.transform.scale(mur, (taille_cellule, taille_cellule))
        changement = pygame.image.load("Assets/pierre_opt.png").convert_alpha()
        changement = pygame.transform.scale(changement, (taille_cellule, taille_cellule))
        
        
    except pygame.error as e:
        print("Erreur lors du chargement des textures (texture_manager)")
        pygame.quit()
        exit()
    
    # map de collision à tester la collisions (sans filtre)
    collision_map = {}
    
    
    for j in range(largeur_grille):
        for i in range(hauteur_grille):
            if grille[i][j] == 0 :
                grille[i][j] = floor
            elif grille[i][j] == 1 :
                grille[i][j] = mur
                
                # Créer un rectangle représentant la position du mur dans le monde
                x = j * taille_cellule
                y = i * taille_cellule
                rect_mur = pygame.Rect(x, y, taille_cellule, taille_cellule)

                # Stocker le rectangle de collision dans notre map de collision par grille
                # On stocke le rect directement, c'est suffisant pour la collision
                collision_map[(j, i)] = rect_mur # Clé (grid_x, grid_y)
            elif grille[i][j] == 2 :
                grille[i][j] = changement
    return grille, collision_map