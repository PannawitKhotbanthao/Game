import pygame
import displayText

def close():
    pygame.quit()
    quit()

def button(gameDisplay, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # ตรวจสอบว่าตำแหน่งของเมาส์อยู่ในพื้นที่ของปุ่มหรือไม่
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        # ตรวจสอบว่ามีการคลิกซ้ายและ action ไม่เป็น None
        if click[0] == 1 and action is not None:
            if action == 'close_intro':
                return 'closeIntroClicked'
            elif action == 'close_game':
                close()  # ปิดเกมโดยเรียกฟังก์ชัน close()
            elif action == 'continue_game':
                return 'continueGame'
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # แสดงข้อความบนปุ่ม
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = displayText.display_text(msg, smallText)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)
