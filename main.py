import pygame 
import random 
import math 



pygame.init()
screen = pygame.display.set_mode((1000,800))

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1000,800))
full_heart = pygame.image.load("health.png")
full_heart = pygame.transform.scale(full_heart, (50,50))
empty_heart = pygame.image.load("empty.png")
empty_heart = pygame.transform.scale(empty_heart, (35,35))

princess = pygame.image.load("princess.png")
princess = pygame.transform.scale(princess, (100,100))
princess_rect = princess.get_rect()
enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (150,150))
enemy_rect = enemy.get_rect()
coin = pygame.image.load("coin.png") 
coin = pygame.transform.scale(coin,(50,50))
coin_rect = coin.get_rect()
platform = pygame.image.load("platform.png")
platform = pygame.transform.scale(platform, (250,80))

player_health = 5
score = 0
font = pygame.font.SysFont('bodoni', 26)

clock = pygame.time.Clock()

princess_rect.center = [50,650]
enemy_rect.center = [100,100]
def main():
    global score 
    global player_health
    running = True 
    
    enemy_speed = 4

    coin_rect.center = [1100,900]
    y_velocity = 0

    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        screen.blit(background, (0,0))
        screen.blit(platform, (450,300)) 

        for heart in range(player_health):
            screen.blit(full_heart,(heart * 35, 30))
        
        for i in range(player_health):
            screen.blit(empty_heart, (i * 35, 30))
 

        screen.blit(princess, princess_rect)
        screen.blit(enemy, enemy_rect)
        screen.blit(coin, coin_rect)

        score_text = font.render("Score: " + str(score) , True, pygame.Color(0,0,0))
        screen.blit(score_text, (875,10))
        princess_rect.centery += y_velocity 

        #get direction from enemy to playr 
        dx = princess_rect[0] - enemy_rect[0]
        dy = princess_rect[1] - enemy_rect[1]
        distance = math.sqrt(dx**2 + dy**2) 

        # normalize direction aka unitize 
        dx /= distance 
        dy /= distance

        #update enemy position
        enemy_rect[0] += dx * enemy_speed
        enemy_rect[1] += dy * enemy_speed

        pygame.display.flip()
        clock.tick(60)

         
        if princess_rect.colliderect(enemy_rect):
            player_health -= 1
            # enemy_rect.centery = 1100

            # coin_rect.center= [princess_rect.centerx +100, princess_rect.centery]
        
           
        if princess_rect.colliderect(coin_rect):
            score += 1 
            coin_rect.center = [random.randint(0,1000) , random.randint(100,600)]
       
        # show score 
        
        if princess_rect.bottom > 700: 
            y_velocity = 0 
        elif princess_rect.bottom <= 400: 
            y_velocity += 3
        else: 
            y_velocity += .025
        
        if princess_rect.left < 0: 
            princess_rect.center = [50,650]
        elif princess_rect.right > 1000: 
            princess_rect.center = [50,650]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y_velocity = -3.7
        if keys[pygame.K_d]:
            princess_rect.centerx += 5
        if keys[pygame.K_a]:
            princess_rect.centerx -= 5


    pygame.quit()

# def health():
#     hx , hy = 100, 100
#     hearts = [health, health, health, health]
#     for i in range(len(hearts)):
#         screen.blit(hearts[i], (hx, hy))
#         hx += 25
#         print("health " + i)

main()

