import pygame
import buttons
import displayText
import intro

def display_victory(gameDisplay, display_width, display_height, message, winner_img, winner_text):
    """
    ฟังก์ชันแสดงผลผู้ชนะ รวมถึงภาพท่าดีใจและปุ่มเลือก.
    - message: ข้อความแสดงสถานะ (เช่น "Game Over")
    - winner_img: ภาพท่าดีใจของผู้ชนะ
    - winner_text: ข้อความประกาศผู้ชนะ (เช่น "Player 1 ชนะ!")
    """

    # แสดงข้อความสถานะเกม
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = displayText.display_text(message, largeText, (255, 255, 255))
    TextRect.center = (display_width / 2, display_height / 5)
    gameDisplay.blit(TextSurf, TextRect)

    # แสดงข้อความประกาศผู้ชนะ
    font = pygame.font.Font('freesansbold.ttf', 50)
    winner_text_surface, winner_text_rect = displayText.display_text(winner_text, font)
    winner_text_rect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(winner_text_surface, winner_text_rect)

    # แสดงภาพผู้ชนะ (ท่าดีใจ)
    gameDisplay.blit(winner_img, (display_width / 2 - 50, display_height / 2 + 100))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # แสดงปุ่ม 'กลับสู่หน้าเริ่มต้น' และ 'ออกจากเกม'
        startAction = buttons.button(gameDisplay, "กลับสู่หน้าเริ่มต้น", 350, 400, 200, 50, (0, 255, 0), (0, 200, 0), 'back_to_intro')
        exitAction = buttons.button(gameDisplay, "ออก", 750, 400, 100, 50, (255, 0, 0), (200, 0, 0), 'exit_game')

        if startAction == 'back_to_intro':
            intro.game_intro(gameDisplay, display_width, display_height, None)  # เรียกหน้าเริ่มต้น
            return  # ออกจากฟังก์ชันเพื่อเริ่มใหม่ในโค้ดหลัก
        elif exitAction == 'exit_game':
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)
