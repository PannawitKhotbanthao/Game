import pygame
import displayText

def close():
    pygame.quit()
    quit()

def button(gameDisplay, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            if action == 'close_intro':
                return 'close_intro'  # ปรับค่าที่ส่งกลับเพื่อใช้ตรวจสอบในโค้ดหลัก
            elif action == 'close_game':
                close()
            elif action == 'continue_game':
                return 'continue_game'
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = displayText.display_text(msg, smallText)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)
