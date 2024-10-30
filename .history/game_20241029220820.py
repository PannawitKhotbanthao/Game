import pygame
import random
import time
import Things
import intro
import buttons
import displayText
import Paused
import sys
import cv2
import os

display_width = 1200
display_height = 600
background_fps = 30

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
sound = pygame.mixer.Sound("sounds/sound.wav")   
pygame.mixer.music.load('sounds/music.mp3')
#pygame.mixer.music.play(-1)

# โหลดวิดีโอด้วย OpenCV
backImg = 'images/BG.mp4'  # ใส่ path ของไฟล์วิดีโอที่ต้องการ
video_capture = cv2.VideoCapture(backImg)

# Animation settings
background_fps = 30  # อัตราเฟรมสำหรับพื้นหลัง

# โหลดภาพผู้เล่น
ballImg = pygame.image.load('images/football.png')
goalLeftImg = pygame.image.load('images/goalLeft.png')
goalRightImg = pygame.image.load('images/goalRight.png')   
boyFirstLeftNormalImg = pygame.image.load('images/ronaldo.png')
boyFirstRightNormalImg = pygame.image.load('images/ronaldo.png')
boyFirstLeftKickImg = pygame.image.load('images/ronaldo_kick.png')
boyFirstRightKickImg = pygame.image.load('images/ronaldo_kick.png')
# เพิ่มรูปภาพผู้เล่นคนที่สอง
boySecondLeftNormalImg = pygame.image.load('images/messi.png')
boySecondRightNormalImg = pygame.image.load('images/messi.png')
boySecondLeftKickImg = pygame.image.load('images/messi_kick.png')
boySecondRightKickImg = pygame.image.load('images/messi_kick.png')
boyFirstLeftVictoryImg = pygame.image.load('images/ronaldo_action.png')
boySecondRightVictoryImg = pygame.image.load('images/messi_action.png')

# โหลดรูปภาพ action ของ Ronaldo และ Messi
ronaldoActionImg = pygame.image.load('images/ronaldo_action.png')
messiActionImg = pygame.image.load('images/messi_action.png')


display_width = 1200
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Football')
pygame.display.set_icon(ballImg)


# ฟังก์ชัน game_background() สำหรับเล่นวิดีโอเป็นพื้นหลัง
def game_background():
    # อ่านเฟรมจากวิดีโอ
    ret, frame = video_capture.read()
    if ret:
        # แปลงสีจาก BGR (OpenCV) เป็น RGB (Pygame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # ปรับขนาดเฟรมให้พอดีกับหน้าจอและแปลงเป็น Surface
        backImg = pygame.surfarray.make_surface(cv2.resize(frame, (display_width, display_height)))
        # แสดงเฟรมในหน้าจอ Pygame
        screen.blit(backImg, (0, 0))
    else:
        # รีเซ็ตวิดีโอให้เล่นซ้ำเมื่อถึงเฟรมสุดท้าย
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)



white = (255,255,255)  
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red = (255,128,0)
bright_green = (0,255,128)

goal_width = goalLeftImg.get_rect().size[0]
goal_height = goalLeftImg.get_rect().size[1]

gravityAcceleration = 0.3
horizontalAcceleration = 0
verticalSpeed = [0, 0]
horizontalSpeed = [0, 0]
ballrect = ballImg.get_rect()   
ball_width = ballrect.size[0]
ball_height = ballrect.size[1]
ball_x = 600
ball_y = 300

boyGravityAcceleration = 0.3

# ผู้เล่นคนที่หนึ่ง
boyRect = boyFirstRightNormalImg.get_rect()
boy_width = boyRect.size[0]
boy_height = boyRect.size[1]
boy_x = display_width / 2
boy_y = display_height - boy_height
boy_x_change = 0
boy_y_change = 0
boyVerticalSpeed = [0, 0]

# ผู้เล่นคนที่สอง
boySecondRect = boySecondRightNormalImg.get_rect()
boySecond_width = boySecondRect.size[0]
boySecond_height = boySecondRect.size[1]
boySecond_x = display_width / 4
boySecond_y = display_height - boySecond_height
boySecond_x_change = 0
boySecond_y_change = 0
boySecondVerticalSpeed = [0, 0]

score_left = 0
score_right = 0

game_background()

def goal(x1, y1, x2, y2):
    gameDisplay.blit(goalLeftImg, (x1, y1))
    gameDisplay.blit(goalRightImg, (x2, y2))

def ball(x, y):
    gameDisplay.blit(ballImg, (x, y))

def firstBoy(type, x, y):
    if type == 'normal left':
        gameDisplay.blit(boyFirstLeftNormalImg, (x, y))
    elif type == 'normal right':
        gameDisplay.blit(boyFirstRightNormalImg, (x, y))
    elif type == 'kick left':
        gameDisplay.blit(boyFirstLeftKickImg, (x, y))
    elif type == 'kick right':
        gameDisplay.blit(boyFirstRightKickImg, (x, y))

def secondBoy(type, x, y):
    if type == 'normal left':
        gameDisplay.blit(boySecondLeftNormalImg, (x, y))
    elif type == 'normal right':
        gameDisplay.blit(boySecondRightNormalImg, (x, y))
    elif type == 'kick left':
        gameDisplay.blit(boySecondLeftKickImg, (x, y))
    elif type == 'kick right':
        gameDisplay.blit(boySecondRightKickImg, (x, y))

intro.game_intro(gameDisplay, display_width, display_height, sound)

# ตั้งค่าตัวจับเวลาแยกสำหรับพื้นหลัง
background_timer = pygame.time.get_ticks()
background_update_interval = 1000 // background_fps  # ระยะห่างเวลาสำหรับพื้นหลัง

crashed = False
while not crashed:

    for event in pygame.event.get():  # ตรวจสอบเหตุการณ์ต่างๆ
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            # ผู้เล่นคนที่หนึ่ง
            if event.key == pygame.K_LEFT:
                boy_x_change = -15
            if event.key == pygame.K_RIGHT:
                boy_x_change = 15
            if event.key == pygame.K_UP:
                boy_y_change = -15
            if event.key == pygame.K_DOWN:
                if boy_y < display_height - boy_height:
                    boy_y_change = 15

            # ผู้เล่นคนที่สอง
            if event.key == pygame.K_a:
                boySecond_x_change = -15
            if event.key == pygame.K_d:
                boySecond_x_change = 15
            if event.key == pygame.K_w:
                boySecond_y_change = -15
            if event.key == pygame.K_s:
                if boySecond_y < display_height - boySecond_height:
                    boySecond_y_change = 15

            if event.key == pygame.K_p:
                Paused.paused(gameDisplay, display_width, display_height, True)

        if event.type == pygame.KEYUP:
            # ผู้เล่นคนที่หนึ่ง
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                boy_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                boy_y_change = 0

            # ผู้เล่นคนที่สอง
            if event.key == pygame.K_a or event.key == pygame.K_d:
                boySecond_x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                boySecond_y_change = 0
                
    # อัปเดตพื้นหลังเมื่อถึงเวลาที่กำหนด
    current_time = pygame.time.get_ticks()
    if current_time - background_timer > background_update_interval:
        game_background()  # อัปเดตเฟรมของพื้นหลัง
        background_timer = current_time  # รีเซ็ตตัวจับเวลา

    # วาดวัตถุอื่นๆ และการควบคุมอัตราเฟรมแยกจากพื้นหลัง
    goal(0, display_height - goal_height, display_width - goal_width, display_height - goal_height)


    # การอัพเดตตำแหน่งของผู้เล่นคนที่หนึ่ง
    boy_x += boy_x_change
    boy_y += boy_y_change

    boyVerticalSpeed[0] = boyGravityAcceleration + boyVerticalSpeed[1]
    boy_y += boyVerticalSpeed[0]
    boyVerticalSpeed[1] = boyVerticalSpeed[0]

    if boy_x < 0:
        boy_x = 0
    if boy_x > (display_width - boy_width):
        boy_x = display_width - boy_width
    if boy_y < 0:
        boy_y = 0
        boyVerticalSpeed = [0, 0]
    if boy_y > display_height - boy_height:
        boy_y = display_height - boy_height
        boyVerticalSpeed = [-boyVerticalSpeed[0] * 0.7, -boyVerticalSpeed[1] * 0.7]

    # การอัพเดตตำแหน่งของผู้เล่นคนที่สอง
    boySecond_x += boySecond_x_change
    boySecond_y += boySecond_y_change

    boySecondVerticalSpeed[0] = boyGravityAcceleration + boySecondVerticalSpeed[1]
    boySecond_y += boySecondVerticalSpeed[0]
    boySecondVerticalSpeed[1] = boySecondVerticalSpeed[0]

    if boySecond_x < 0:
        boySecond_x = 0
    if boySecond_x > (display_width - boySecond_width):
        boySecond_x = display_width - boySecond_width
    if boySecond_y < 0:
        boySecond_y = 0
        boySecondVerticalSpeed = [0, 0]
    if boySecond_y > display_height - boySecond_height:
        boySecond_y = display_height - boySecond_height
        boySecondVerticalSpeed = [-boySecondVerticalSpeed[0] * 0.7, -boySecondVerticalSpeed[1] * 0.7]

    # การอัพเดตตำแหน่งของลูกบอล
    verticalSpeed[0] = gravityAcceleration + verticalSpeed[1]
    ball_y += verticalSpeed[0]
    verticalSpeed[1] = verticalSpeed[0]

    horizontalSpeed[0] = horizontalAcceleration + horizontalSpeed[1]
    ball_x += horizontalSpeed[0]
    horizontalSpeed[1] = horizontalSpeed[0]

    if ball_x < 0:
        ball_x = 0
        horizontalSpeed = [-horizontalSpeed[0] * 0.7, -horizontalSpeed[1] * 0.7]
    if ball_x > (display_width - ball_width):
        ball_x = display_width - ball_width
        horizontalSpeed = [-horizontalSpeed[0] * 0.7, -horizontalSpeed[1] * 0.7]
    if ball_y < 0:
        ball_y = 0
        verticalSpeed = [0, 0]
    if ball_y > (display_height - ball_height):
        ball_y = display_height - ball_height
        verticalSpeed = [-verticalSpeed[0] * 0.7, -verticalSpeed[1] * 0.7]
        if ball_y == (display_height - ball_height):
            horizontalSpeed = [horizontalSpeed[0] * 0.95, horizontalSpeed[1] * 0.95]
            
    # การตรวจจับการชนของลูกบอลกับผู้เล่นคนที่หนึ่ง
    if ball_x > boy_x + boy_width - 10 and ball_x < boy_x + boy_width + 10 and ball_y + (ball_height / 2) > boy_y and ball_y + (ball_height / 2) < boy_y + boy_height:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        firstBoy('kick right', boy_x, boy_y)
    elif ball_x + ball_width < boy_x + 10 and ball_x + ball_width > boy_x - 10 and ball_y + (ball_height / 2) > boy_y and ball_y + (ball_height / 2) < boy_y + boy_height:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = -10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        firstBoy('kick left', boy_x, boy_y)
    elif ball_x + (ball_width / 2) > boy_x and ball_x + (ball_width / 2) < boy_x + boy_width and ball_y + (ball_height) < boy_y + 10 and ball_y + (ball_height) > boy_y - 10:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        firstBoy('kick right', boy_x, boy_y)
    else:
        if ball_x >= (display_width / 2):
            firstBoy('normal right', boy_x, boy_y)
        else:
            firstBoy('normal left', boy_x, boy_y)

    # การตรวจจับการชนของลูกบอลกับผู้เล่นคนที่สอง
    if ball_x > boySecond_x + boySecond_width - 10 and ball_x < boySecond_x + boySecond_width + 10 and ball_y + (ball_height / 2) > boySecond_y and ball_y + (ball_height / 2) < boySecond_y + boySecond_height:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        secondBoy('kick right', boySecond_x, boySecond_y)
    elif ball_x + ball_width < boySecond_x + 10 and ball_x + ball_width > boySecond_x - 10 and ball_y + (ball_height / 2) > boySecond_y and ball_y + (ball_height / 2) < boySecond_y + boySecond_height:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = -10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        secondBoy('kick left', boySecond_x, boySecond_y)
    elif ball_x + (ball_width / 2) > boySecond_x and ball_x + (ball_width / 2) < boySecond_x + boySecond_width and ball_y + (ball_height) < boySecond_y + 10 and ball_y + (ball_height) > boySecond_y - 10:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10
        secondBoy('kick right', boySecond_x, boySecond_y)
    else:
        if ball_x >= (display_width / 2):
            secondBoy('normal right', boySecond_x, boySecond_y)
        else:
            secondBoy('normal left', boySecond_x, boySecond_y)

    # ตรวจสอบการทำประตู
    if ball_x > 0 and ball_x < goal_width - ball_width and ball_y < display_height and ball_y > display_height - goal_height:
        score_left += 1
        Paused.paused(gameDisplay, display_width, display_height, 'Player 1 scores', True)
        
    # ลบภาพผู้เล่นเก่าออกโดยการเติมพื้นหลังในบริเวณที่ผู้เล่นอยู่
        gameDisplay.blit(backImg, (0, 0))  # ล้างหน้าจอหรือใช้สีพื้นหลังที่เหมาะสม
    # แสดงภาพฉลองชัยสำหรับ Player 1 ที่ตำแหน่งลูกบอลหรือกลางจอ
        gameDisplay.blit(boyFirstLeftVictoryImg, (display_width / 2 - 50, display_height / 2 - 50))
        pygame.display.update()
        pygame.time.delay(1000)  # หน่วงเวลาเพื่อให้ภาพแสดงสักครู่ 
               
        ball_x = 600
        ball_y = 300 - (ball_width / 2)
        gravityAcceleration = 0.3
        horizontalAcceleration = 0
        verticalSpeed = [0, 0]
        horizontalSpeed = [0, 0]

    if ball_x > (display_width - goal_width) and ball_x < display_width and ball_y < display_height and ball_y > display_height - goal_height:
        score_right += 1
        Paused.paused(gameDisplay, display_width, display_height, 'Player 2 scores', True)
        # ลบภาพผู้เล่นเก่าออกโดยการเติมพื้นหลังในบริเวณที่ผู้เล่นอยู่
        gameDisplay.blit(backImg, (0, 0))  # ล้างหน้าจอหรือใช้สีพื้นหลังที่เหมาะสม
        # แสดงภาพฉลองชัยสำหรับ Player 2 ที่ตำแหน่งลูกบอลหรือกลางจอ
        gameDisplay.blit(boySecondRightVictoryImg, (display_width / 2 - 50, display_height / 2 - 50))
        pygame.display.update()
        pygame.time.delay(1000)  # หน่วงเวลาเพื่อให้ภาพแสดงสักครู่
        
        ball_x = 600
        ball_y = 300 - (ball_width / 2)
        gravityAcceleration = 0.3
        horizontalAcceleration = 0
        verticalSpeed = [0, 0]
        horizontalSpeed = [0, 0]

    # แสดงคะแนน
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = displayText.display_text(str(score_left) + " | " + str(score_right), largeText)
    TextRect.center = ((display_width / 2), 20)
    gameDisplay.blit(TextSurf, TextRect)

    # แสดงลูกบอล
    gameDisplay.blit(ballImg, (ball_x, ball_y))

    pygame.display.update()
    clock.tick(30)
    
    pygame.display.flip()
    clock.tick(background_fps)

# ปิดการจับภาพและออกจาก Pygame เมื่อสิ้นสุดการใช้งาน
video_capture.release()
pygame.quit()
quit()
sys.exit()

# เรียกใช้หน้าจอเริ่มต้น
start_screen()