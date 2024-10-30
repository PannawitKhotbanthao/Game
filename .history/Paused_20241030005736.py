import pygame
import buttons
import displayText
import intro  # Import หน้าเริ่มต้น

clock = pygame.time.Clock()

# กำหนดสี
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bright_red = (255, 128, 0)
bright_green = (0, 255, 128)

def paused(gameDisplay, display_width, display_height, message, pause=False, winner=None):
    """
    ฟังก์ชันแสดงข้อความพักเกม/ประกาศผู้ชนะ และแสดงปุ่มเลือก.
    - winner: ข้อความผู้ชนะที่จะประกาศเมื่อจบเกม เช่น "Player 1 ชนะ!"
    """

    # กำหนดฟอนต์และตำแหน่งแสดงข้อความ
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = displayText.display_text(message, largeText, white)
    TextRect.center = ((display_width / 2), (display_height / 5))
    gameDisplay.blit(TextSurf, TextRect)

    # แสดงข้อความผู้ชนะ ถ้ามีผู้ชนะ
    if winner:
        font = pygame.font.Font('freesansbold.ttf', 50)
        winner_text_surface, winner_text_rect = displayText.display_text(winner, font)
        winner_text_rect.center = (display_width / 2, display_height / 2)
        gameDisplay.blit(winner_text_surface, winner_text_rect)

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
