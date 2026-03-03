# BellP7.py - Modified
# Programmer: Nora Bell
# Purpose: Prevent crash on player death and show Game Over message

import pygame
from Sprite import AnimatedSprite
from ParallaxScrollingBackground import ParallaxScrollingBackground as Bg
from OrcSpawner import OrcSpawner
from Projectile import Arrow
from Sound import SoundEngine
import random
def game():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()


    soundEngine = SoundEngine()
    soundEngine.loadSound("walk0" , "InfiniFantasy/Assets/SFX/Dirt Walk 1.ogg")
    soundEngine.loadSound("walk1" , "InfiniFantasy/Assets/SFX/Dirt Walk 2.ogg")
    soundEngine.loadSound("walk2" , "InfiniFantasy/Assets/SFX/Dirt Walk 3.ogg")
    soundEngine.loadSound("walk3" , "InfiniFantasy/Assets/SFX/Dirt Walk 4.ogg")
    soundEngine.loadSound("walk4" , "InfiniFantasy/Assets/SFX/Dirt Walk 5.ogg")
    soundEngine.loadSound("playerAttackSuccess" , "InfiniFantasy/Assets/SFX/Bow Impact Hit 1.ogg")
    soundEngine.loadSound("playerAttackInitial" , "InfiniFantasy/Assets/SFX/Bow Take Out 1.ogg")
    soundEngine.loadSound("OrcAttackHit" , "InfiniFantasy/Assets/SFX/Sword Impact Hit 1.ogg")

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("InfiniFantasy")
    clock = pygame.time.Clock()

    playerCharacter = AnimatedSprite(position=(100, 580), characterType='ranger')
    spawner = OrcSpawner(screen.get_width(), 580)
    projectiles = pygame.sprite.Group()
    projectileImagePath = "InfiniFantasy/Assets/Arrow/Arrow01(100x100).png"
    layerPath = [
        ('InfiniFantasy/Assets/Background/Layer_0011_0.png', 0.1),
        ('InfiniFantasy/Assets/Background/Layer_0010_1.png', 0.15),
        ('InfiniFantasy/Assets/Background/Layer_0009_2.png', 0.2),
        ('InfiniFantasy/Assets/Background/Layer_0008_3.png', 0.25),
        ('InfiniFantasy/Assets/Background/Layer_0007_Lights.png', 0.3),
        ('InfiniFantasy/Assets/Background/Layer_0006_4.png', 0.35),
        ('InfiniFantasy/Assets/Background/Layer_0005_5.png', 0.4),
        ('InfiniFantasy/Assets/Background/Layer_0004_Lights.png', 0.45),
        ('InfiniFantasy/Assets/Background/Layer_0003_6.png', 0.5),
        ('InfiniFantasy/Assets/Background/Layer_0002_7.png', 0.55),
        ('InfiniFantasy/Assets/Background/Layer_0001_8.png', 0.6),
        ('InfiniFantasy/Assets/Background/Layer_0000_9.png', 0.65)
    ]
    background = Bg(layerPath, screen.get_size())

    attackCooldown = 1000
    jumpCooldown = 1000
    damageCooldown = 500
    stepCooldown = 250
    orcAttackCooldown = 300
    orcLastSwing = -orcAttackCooldown
    lastAttack = -attackCooldown
    lastJump = -jumpCooldown
    lastDamageTime = -damageCooldown
    timeSinceLastStep = -stepCooldown
    scrollSpeed = 5
    midScreenX = screen.get_width() // 2
    jumpKeyPressedLastFrame = False
    playerDead = False
    killCount = 0
    font = pygame.font.SysFont("Arial", 24)
    running = True
    soundEngine.loopBackgroundMusic('InfiniFantasy/Assets/Music/Forest Day Rain.ogg')
    rain_frames = []
    weather_sheet = pygame.image.load("InfiniFantasy/Assets/Foreground/rain effect.png").convert_alpha()
    for i in range(6):
            frame = weather_sheet.subsurface(pygame.Rect(i * 50, 0, 50, 50))
            rain_frames.append(frame)
    while running:
        clock.tick(60)
        currentTick = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keyPress = pygame.key.get_pressed()

        if not playerDead:
            # Movement
            if keyPress[pygame.K_RIGHT]:
                if currentTick - timeSinceLastStep >= 250:
                    soundEngine.playSound(f"walk{random.randint (0,4)}") #play a random walking sound for each 'step'
                    timeSinceLastStep = currentTick
                playerCharacter.set_animation_state('walk')
                playerCharacter.flipped = False
                if playerCharacter.rect.centerx <= midScreenX:
                    playerCharacter.rect.x += scrollSpeed
                else:
                    background.update(scrollSpeed)
                    for orc in spawner.spawnedOrcs:
                        orc.rect.x -= scrollSpeed
            elif keyPress[pygame.K_LEFT]:
                if currentTick - timeSinceLastStep >= 250:
                    soundEngine.playSound(f"walk{random.randint (0,4)}")
                    timeSinceLastStep = currentTick
                playerCharacter.set_animation_state('walk')
                playerCharacter.flipped = True
                playerCharacter.rect.x -= scrollSpeed
                background.update(-scrollSpeed)
                for orc in spawner.spawnedOrcs:
                    orc.rect.x += scrollSpeed
            elif keyPress[pygame.K_z]:
                if currentTick - lastAttack > attackCooldown:
                    soundEngine.playSound("playerAttackInitial")
                    playerCharacter.set_animation_state('attack')
                    lastAttack = currentTick
                    projectileSpawned = False
            else:
                if currentTick - lastAttack >= 800:
                    playerCharacter.set_animation_state('idle')

            # Jump
            jumpPressed = keyPress[pygame.K_x]
            if (
                jumpPressed and
                not jumpKeyPressedLastFrame and
                not playerCharacter.isJumping and
                playerCharacter.rect.bottom >= 598
            ):
                playerCharacter.velocityY = playerCharacter.jumpStrength
                playerCharacter.isJumping = True
            jumpKeyPressedLastFrame = jumpPressed

            playerCharacter.hasGravity()
            playerCharacter.rect.left = max(playerCharacter.rect.left, 0)
            playerCharacter.rect.right = min(playerCharacter.rect.right, screen.get_width())

            # Spawn projectile
            if playerCharacter.state == 'attack' and playerCharacter.currentFrame == len(playerCharacter.frames) - 1:
                if not projectileSpawned:
                    direction = "left" if playerCharacter.flipped else "right"
                    projX = playerCharacter.rect.centerx + (30 if direction == "right" else -30)
                    projY = playerCharacter.rect.centery
                    projectile = Arrow((projX, projY), direction, projectileImagePath)
                    projectiles.add(projectile)
                    projectileSpawned = True

        # Projectile collision with orcs
        for projectile in projectiles:
            for orc in spawner.spawnedOrcs:
                if orc.hitbox.colliderect(projectile.hitbox) and currentTick-lastAttack>=100:
                    soundEngine.playSound("playerAttackSuccess")
                    if hasattr(orc, "healthPoints"):
                        orc.healthPoints -= 50
                        projectile.kill()
                        if orc.healthPoints <= 0:
                            orc.set_animation_state('death')
                            orc.timeOfDeath = currentTick
                        else:
                            orc.set_animation_state('hurt')
        
        
        # Orc behavior
        for orc in spawner.spawnedOrcs:
            if orc.healthPoints <= 0 and not hasattr(orc, "timeOfDeath"):
                orc.set_animation_state('death')
                orc.timeOfDeath = currentTick
            if hasattr(orc, 'timeOfDeath'):
                if orc.timeOfDeath==currentTick:
                    killCount += 1
                #print(f"Kill Count : {killCount}, Current Tick:{currentTick}")
                
            distanceToEnemy = abs(playerCharacter.rect.centerx - orc.rect.centerx)
            if distanceToEnemy < 100 and not hasattr(orc, 'hurt' or 'death'):
                orc.set_animation_state('attack')
            else:
                orc.set_animation_state('idle')

            if hasattr(orc, 'timeOfDeath') and currentTick - orc.timeOfDeath > 1000:
                spawner.spawnedOrcs.remove(orc)

            if not playerDead and orc.state == 'attack' and playerCharacter.hitbox.colliderect(orc.hitbox):
                if currentTick - orcLastSwing >= 300:
                    soundEngine.playSound("OrcAttackHit")
                    orcLastSwing = currentTick
                if currentTick - lastDamageTime >= damageCooldown:
                    playerCharacter.set_animation_state('hurt')
                    playerCharacter.healthPoints -= 10
                    #print("Player Took Damage")
                    #print(f"HP: {playerCharacter.healthPoints}")
                    lastDamageTime = currentTick
                    if playerCharacter.healthPoints <= 0:
                        playerCharacter.set_animation_state('death')
                        playerCharacter.timeOfDeath = currentTick
                        playerDead = True
        

            #print(f"Orc state: {orc.state}, Distance: {distanceToEnemy}")

        if not playerDead:
            playerCharacter.frameUpdate()
            
        if playerDead and currentTick - playerCharacter.timeOfDeath >=1000:
            font = pygame.font.SysFont("Times New Roman", 48)
            text = font.render("You Died", True, (200, 0, 0))
            screen.blit(text, (screen.get_width() // 2 - 180, screen.get_height() // 2 - 50))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        

        spawner.update(currentTick)
        projectiles.update()

        screen.fill((0, 0, 0))
        background.draw(screen)
        if not playerDead:
            playerCharacter.draw(screen)
        spawner.draw(screen)
        for projectile in projectiles:
            projectile.draw(screen)

        scoreText = font.render(f"Kills: {killCount}", True, (255, 255, 255))
        outline = font.render(f"Kills: {killCount}", True, (0, 0, 0))
        screen.blit(outline, (21, 521))
        screen.blit(scoreText, (20, 520))
        for _ in range(5):
            frame = random.choice(rain_frames)
            x = random.randint(0, screen.get_width()-50)
            y = random.randint(0, screen.get_height()-50)
            screen.blit(frame, (x, y))

        pygame.display.flip()

        
        
if __name__ == "__main__":
    stillPlaying = True
    while stillPlaying:  
        game()
        # Ask if player wants to play again
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        font = pygame.font.SysFont("Arial", 36)
        prompt = font.render("Play again? (Y/N)", True, (255, 255, 255))
        screen.blit(prompt, (screen.get_width() // 2 - 150, screen.get_height() // 2 + 20))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stillPlaying = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting = False
                        stillPlaying = True
                    elif event.key == pygame.K_n:
                        waiting = False
                        stillPlaying = False
        pygame.quit()


pygame.quit()