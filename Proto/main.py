import pygame
import random

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_PARTICLES = 50
MAX_SPEED = 2
PARTICLE_SIZE = 5
ENERGY_LOSS = 0.1  # énergie perdue par frame
REPRODUCTION_THRESHOLD = 150  # énergie nécessaire pour se reproduire
INITIAL_ENERGY = 100

# --- Initialisation Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Life")
clock = pygame.time.Clock()

# --- Classe Particule ---
class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.energy = INITIAL_ENERGY

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Rebondir sur les bords
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

        # Perte d'énergie
        self.energy -= ENERGY_LOSS

    def interact(self, other):
        # Exemple simple : si proche, voler un peu d'énergie
        dx = self.x - other.x
        dy = self.y - other.y
        dist_sq = dx*dx + dy*dy
        if dist_sq < 100:  # distance de contact
            transfer = 0.5
            if self.energy > transfer:
                self.energy -= transfer
                other.energy += transfer

    def reproduce(self):
        if self.energy > REPRODUCTION_THRESHOLD:
            self.energy /= 2
            child = Particle()
            child.x = self.x + random.uniform(-10, 10)
            child.y = self.y + random.uniform(-10, 10)
            return child
        return None

    def draw(self, screen):
        color = (255, max(0, int(self.energy)), 0)  # plus vert si énergie haute
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), PARTICLE_SIZE)

# --- Création des particules ---
particles = [Particle() for _ in range(NUM_PARTICLES)]

# --- Boucle principale ---
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des particules
    new_particles = []
    for p in particles:
        p.move()
        # Interaction avec les autres
        for other in particles:
            if other != p:
                p.interact(other)
        # Reproduction
        child = p.reproduce()
        if child:
            new_particles.append(child)
        # Dessiner
        p.draw(screen)

    # Ajouter les nouveaux enfants
    particles.extend(new_particles)
    # Supprimer les particules mortes
    particles = [p for p in particles if p.energy > 0]

    # Affichage
    pygame.display.flip()

pygame.quit()
