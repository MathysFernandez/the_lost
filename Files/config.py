import pygame

Titre = "The lost"
taille_cellule = 100
taille_joueur = 55
vitesse = 3
FPS = 60
taille_BT_w = 200
taille_BT_h = 50

def get_dimensions():
    largeur_fen = pygame.display.Info().current_w
    hauteur_fen = pygame.display.Info().current_h - 60
    return largeur_fen, hauteur_fen