import pygame
import buttons
import displayText
import intro

def paused(gameDisplay, display_width, display_height, message, pause=False, winner=None, winner_img=None):
    # กำหนดฟอนต์และตำแหน่งแสดงข้อความ
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = displayText.display_text(message, largeText, white)
    TextRect.center = ((display_width / 2), (display_height / 5))
    gameDisplay.blit(TextSurf, TextRect)
    
    boyFirstLeftVictoryImg = pygame.image.load('images/ronaldo_action.png')
    boySecondRightVictoryImg = pygame.image.load('images/messi_action.png')


    # แสดงข้อความผู้ชนะและท่าดีใจ
    if winner:
        font = pygame.font.Font('freesansbold.ttf', 50)
        winner_text_surface, winner_text_rect = displayText.display_text(winner, font)
        winner_text_rect.center = (display_width / 2, display_height / 2)
        gameDisplay.blit(winner_text_surface, winner_text_rect)

        if "Player 1" in winner:
            gameDisplay.blit(boyFirstLeftVictoryImg, (display_width / 2 - 50, display_height / 2 + 100))
        elif "Player 2" in winner:
            gameDisplay.blit(boySecondRightVictoryImg, (display_width / 2 - 50, display_height / 2 + 100))

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # ปุ่ม 'กลับสู่หน้าเริ่มต้น' และ 'ออกจากเกม'
        startAction = buttons.button(gameDisplay, "กลับสู่หน้าเริ่มต้น", 350, 400, 200, 50, green, bright_green, 'back_to_intro')
        exitAction = buttons.button(gameDisplay, "ออก", 750, 400, 100, 50, red, bright_red, 'exit_game')
        
        if startAction == 'back_to_intro':
            intro.game_intro(gameDisplay, display_width, display_height, sound)  # เรียกหน้าเริ่มต้น
            pause = False
        elif exitAction == 'exit_game':
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(15)
