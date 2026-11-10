import pygame
from player import Player
from oiseau import Oiseau
from constants import *
import json

class Game:
    
    def __init__(self):
        # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        
        # Etat du jeu
        self.is_playing = False

        # Charger l'image d'arrière plan
        self.bg_image = pygame.image.load("assets/bg.jpg")

        # Redimensionner l'image d'arrière plan
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Créer le joueur
        self.player = Player()
        
        # Créer le groupe d'oiseaux
        self.oiseaux = pygame.sprite.Group()
        
        # Créer des variables pour le score, les vies, la limite de spawn, et la vitesse de spawn (cycle)
        self.score = 0
        self.lives = 5
        self.spawnlimit = 5
        self.cycle = 0
        self.limite_cycle = 30
        
        # Charger les polices d'écriture
        self.font_base = pygame.font.SysFont('Impact', 30)
        self.font_smaller = pygame.font.SysFont('Impact', 25)
        
        # Créer la boucle du jeu (maintenir la fenetre allumé)
        self.running = True
    
    
    
    def update(self):
        # actualiser l'ecran du jeu
        self.screen.blit(self.bg_image, (0, 0))
        self.oiseaux.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
            
        # actualiser le score
        score_text = self.font_base.render(f"Score : {self.score}", False, "white")
        self.screen.blit(score_text, (10, 10))
        # actualiser le nombre de vies
        lives_display = self.font_base.render(f"Vies : {self.lives}", False, "white")
        self.screen.blit(lives_display, (500, 10))         
    
    def check_collision(self):
        # vérifier que le joueur attrape l'oiseau
        if pygame.sprite.spritecollide(self.player, self.oiseaux, True, collided=None):
            self.score += 1
    
    def check_mort(self):
        for oi in self.oiseaux:
            if oi.rect.y > 580:
                oi.kill()
                return True
        return False
    
    # Augmente la difficulté
    def difficulté(self):
        match self.score:
            case 50:
                #print("score :", self.score, "limite :", self.spawnlimit, "cycle :", self.limite_cycle)
                self.spawnlimit = 7
                self.limite_cycle = 20
            case 100:
                #print("score :", self.score, "limite :", self.spawnlimit, "cycle :", self.limite_cycle)
                self.spawnlimit = 10
                self.limite_cycle = 10
            case 170:
                #print("score :", self.score, "limite :", self.spawnlimit, "cycle :", self.limite_cycle)
                self.spawnlimit = 15
                self.limite_cycle = 5
            case 200:
                #print("score :", self.score, "limite :", self.spawnlimit, "cycle :", self.limite_cycle)
                self.spawnlimit = 20
            
    def keyboard(self):
        # récupérer les touches enclenchées
        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
            self.player.move_right()
        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_q]:
            self.player.move_left()
            
    def spawn_oiseaux(self):
        if len(self.oiseaux) < self.spawnlimit and self.cycle==0:   # système de cycle pour ajouter des oiseaux seulement en dessous de la limite et seulement au bout d'un certain temps (self.limite_cycle)
            self.oiseaux.add(Oiseau())
        for instance in self.oiseaux:
            instance.tomber()
            
        # incrémentation du système de cycle
        if self.cycle<self.limite_cycle:
            self.cycle+=1
        else:
            self.cycle=0
    
    
    
    # Ecran de fin
    def game_over_screen(self):
        affichage_score=self.font_smaller.render(f"Score final : {self.score}", False, "white")
        self.screen.blit(affichage_score, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2))
        
        message_game_over=self.font_smaller.render("Appuyez sur entrée pour revenir au menu principal", False, "white")
        self.screen.blit(message_game_over, (50, SCREEN_HEIGHT/2+50))
        
        while self.is_playing:
            if self.keys[pygame.K_ESCAPE] or self.keys[pygame.K_RETURN]:
                self.is_playing = False
            self.clock.tick(60)
        
        
    # Le jeu
    def playing(self):
        while self.is_playing:
            self.keyboard()
            self.check_collision()
            if self.check_mort():
                self.lives-=1
            self.spawn_oiseaux()
            
            # Quitter rapidement avec esc durant la partie
            if self.keys[pygame.K_ESCAPE]:
                    # le joueur ferme le jeu
                    self.running = False
                    pygame.quit()
            
            # mise à jour de l'affichage et du score
            self.update()
                
            # Augmentation de difficulté
            self.difficulté()
            
            if self.lives<=0:
                self.game_over_screen()                
                
            pygame.display.flip()
            self.clock.tick(60)
        return self.score

            
            
    def run(self):
        
        # fermer le jeu
        while self.running:
            # parcourir les evenements de pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # le joueur ferme le jeu
                    self.running = False
                    pygame.quit()
                if self.keys[pygame.K_ESCAPE]:
                    # le joueur ferme le jeu
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.is_playing = True
                        final_score = self.playing()
                        
                        # ajouter final_score au json
                        with open('historique_scores.json', 'r+', encoding="utf-8") as file :
                            temp = []
                            temp.append(json.load(file))
                        temp.append(final_score)
                        with open('historique_scores.json', 'w', encoding="utf-8") as file :
                            json.dump(max(temp),file,indent = 4)
                            

            # Menu principal
        
            # Afficher et actualiser l'écran
            self.screen.blit(self.bg_image, (0, 0))
            
            # Afficher contexte et instructions : espace pour commencer et esc pour quitter
            regles1 = self.font_smaller.render("Les oiseaux sont en train d'apprendre à voler", False, "white")
            regles2 = self.font_smaller.render("mais certains ont du mal.",False,"white")
            regles3 = self.font_smaller.render("Rattrapez-les avant qu'ils tombent!", False, "white")
            regles4 = self.font_smaller.render("Laissez-en tomber 5 et vous serez renvoyé de la réserve.",False,"white")
            self.screen.blit(regles1, (80, SCREEN_HEIGHT/2-120))
            self.screen.blit(regles2, (180, SCREEN_HEIGHT/2-90))
            self.screen.blit(regles3, (130, SCREEN_HEIGHT/2-60))
            self.screen.blit(regles4, (20, SCREEN_HEIGHT/2-30))
            
            menu_instructions = self.font_base.render("Appuyez sur espace pour commencer", False, "white")
            self.screen.blit(menu_instructions, (SCREEN_WIDTH/6, SCREEN_HEIGHT/2+60))            
            
            # ici afficher meilleur score en haut à gauche ou au milieu
            with open('historique_scores.json', 'r+', encoding="utf-8") as file :
                temp = json.load(file)
            best_score = self.font_base.render(f"Meilleur score : {temp}", False, "white")
            self.screen.blit(best_score, (150,10))
            
            self.clock.tick(60)
