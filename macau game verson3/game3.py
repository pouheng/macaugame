




import pygame
import sys 

# 初始化pygame
pygame.init()

# 設定視窗大小
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 設定遊戲標題
pygame.display.set_caption("Game Title")

# 設定字型
font = pygame.font.SysFont("Arial", 30)

# 載入圖片 
backgroundsupermove1 = pygame.image.load("supermove.png")
backgroundsupermove2 = pygame.image.load("supermove2.png")

# 載入圖片 
background2 = pygame.image.load("background2.png")

# 載入圖片
background = pygame.image.load("background1.png")
character_images = {
    "pouheng": pygame.image.load("pouheng.png"),
    "melody": pygame.image.load("melody.png"),
    "lyba": pygame.image.load("lyba.png")
}


# 停止之前播放中的音樂
pygame.mixer.music.stop()

# 播放新的音樂
pygame.mixer.music.load("the start of everything.mp3")
pygame.mixer.music.play(-1)  # -1 表示持續播放






















# Initialize pygame
pygame.init()

# Window sizeTrue
WINDOW_SIZE = (1280, 720)

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font and font size
FONT_NAME = 'arial'
FONT_SIZE = 24

# Function to display text
def draw_text(surface, text, color, x, y):
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.x = x
    rect.y = y
    surface.blit(text_surface, rect)

# Define the color red in Pygame
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define global variables
day = 1
subscriber = 200
popularity = 10
macau_percent = 60
money = 10000
promotion_activated = False
promotion_image = pygame.image.load("discord_promotion.png")
promotion_rect = promotion_image.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

manage_social_media_width = 200
manage_social_media_height = 60
manage_social_media_rect = pygame.Rect(0, 0, manage_social_media_width, manage_social_media_height)
social_media_activated = False

super_move_media_width = 200
super_move_media_height = 60


# Develop the game scene
def develop_scene():
    # Access global variables
    global day, subscriber, popularity, macau_percent, money, promotion_activated, promotion_image, promotion_rect,manage_social_media_rect,manage_social_media_width,manage_social_media_height,social_media_activated
    global super_move_media_width,super_move_media_height

    promotion_activated = False
    social_media_activated = False





    # 停止之前播放中的音樂
    pygame.mixer.music.stop()

    # 播放新的音樂
    pygame.mixer.music.load("game loop.mp3")
    pygame.mixer.music.play(-1)  # -1 表示持續播放

    # Create window
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Next day button
    next_day_x = WINDOW_SIZE[0] - 200
    next_day_y = WINDOW_SIZE[1] - 80
    next_day_width = 160
    next_day_height = 60
    next_day_rect = pygame.Rect(next_day_x, next_day_y, next_day_width, next_day_height)



    # Manage super move button
    super_move_media_width = 200
    super_move_media_height = 60
    super_move_media_rect = pygame.Rect(0, 0, super_move_media_width, super_move_media_height)
    super_move_media_rect.bottomleft = (manage_social_media_rect.right + 20, promotion_rect.bottom)
    # Manage Social Media button
    manage_social_media_width = 200
    manage_social_media_height = 60
    manage_social_media_rect = pygame.Rect(0, 0, manage_social_media_width, manage_social_media_height)
    manage_social_media_rect.bottomleft = (promotion_rect.right + 20, promotion_rect.bottom)

    
    # Discord Promotion button
    promotion_width = 200
    promotion_height = 60
    promotion_rect = pygame.Rect(0, 0, promotion_width, promotion_height)
    promotion_rect.bottomleft = (20, WINDOW_SIZE[1] - 20)

    # Load promotion image
    promotion_image = pygame.image.load('discord_promotion.png')
    promotion_image_rect = promotion_image.get_rect()
    promotion_image_rect.center = screen.get_rect().center
    # Load social media icon image
    social_media_icon = pygame.image.load('manage_social_media.png')
    social_media_icon_rect = social_media_icon.get_rect()
    social_media_icon_rect.center = screen.get_rect().center




    # 游戏循环
    running = True
    while running:
        # 事件循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查是否点击了下一天按钮
                if next_day_rect.collidepoint(event.pos):
                    # 根据订阅者数量和当前的澳门观众比例计算下降数量
                    macau_drop = max(0, int(subscriber * (macau_percent / 100)))
                    if subscriber > 0:
                        max_drop = max(0.1, 0.5 - subscriber / 20000) # 計算最大下降幅度
                        if subscriber < 1000: # 如果訂閱數很低
                            macau_drop_percent = min(0.01, macau_drop / subscriber) # 將下降比例限制在 10% 以下
                        else:
                            macau_drop_percent = min(1, macau_drop / subscriber) # 計算實際下降比例
                        macau_percent = max(0.1, macau_percent - (macau_drop_percent * (1 + subscriber / 4000) * max_drop))

                    # 更新值
                    subscriber += popularity
                    money += int(subscriber / 30)
                    popularity = max(0, popularity - 1)
                    day += 1
                    if day == 2:
                        second_day_dialogue_scene(screen, font, background, character_images)
                    if day == 3:
                        day_Three_dialogue_scene(screen, font, background, character_images)
                    if promotion_activated:
                        popularity += 1.5
                        money += 0.1
                    if social_media_activated:
                        popularity += 1.3
                        money += 0.1
                        macau_percent += 0.05


                # Check if clicked on Manage super move button
                if super_move_media_rect.collidepoint(event.pos):
                    supermove_scene()

                # Check if clicked on Manage Social Media button
                elif manage_social_media_rect.collidepoint(event.pos):
                    if social_media_activated:
                        social_media_activated = False
                    else:
                        social_media_activated = True
                        promotion_activated = False

                # Check if clicked on Discord Promotion button
                elif promotion_rect.collidepoint(event.pos):
                    if promotion_activated:
                        promotion_activated = False
                    else:
                        promotion_activated = True
                        social_media_activated = False

        # 更新屏幕
        screen.fill(BLACK)
        # 繪製背景圖
        screen.blit(background2, (0, 0))

        # Draw game values
        draw_text(screen, 'Day: {}'.format(day), WHITE, 20, 20)
        pygame.draw.rect(screen, BLACK, pygame.Rect(185, 20, 200, 30))
        draw_text(screen, 'Subscriber: {}'.format(subscriber), WHITE, 200, 30)
        pygame.draw.rect(screen, BLACK, pygame.Rect(415, 20, 200, 30))
        draw_text(screen, 'Popularity: {}'.format(popularity), WHITE, 420, 30)
        pygame.draw.rect(screen, BLACK, pygame.Rect(645, 20, 200, 30))
        draw_text(screen, 'Macau Percent: {}%'.format(macau_percent), WHITE, 630, 30)
        pygame.draw.rect(screen, BLACK, pygame.Rect(895, 20, 200, 30))
        draw_text(screen, 'Money: {} mop'.format(money), WHITE, 900, 30)
        if day >= 2:
            pygame.draw.rect(screen, BLUE, manage_social_media_rect)
            manage_social_media_text = font.render('Manage Social Media', True, WHITE)
            screen.blit(manage_social_media_text, (manage_social_media_rect.x + 10, manage_social_media_rect.y + 10))

        if day >= 3:
            pygame.draw.rect(screen, RED, super_move_media_rect)
            Super_Move_media_text = font.render('Super Move', True, WHITE)
            screen.blit(Super_Move_media_text, (super_move_media_rect.x + 10, super_move_media_rect.y + 10))




        # Draw next day button
        pygame.draw.rect(screen, WHITE, next_day_rect)
        draw_text(screen, 'Next Day', BLACK, next_day_x + 10, next_day_y + 10)

        # Display promotion image if activated
        if promotion_activated:
            screen.blit(promotion_image, promotion_image_rect)

        # Display social_media_activated image if activated
        if social_media_activated:
            screen.blit(social_media_icon, social_media_icon_rect)

        # Draw Discord Promotion button
        pygame.draw.rect(screen, WHITE, promotion_rect)
        draw_text(screen, 'Discord Promotion', BLACK, promotion_rect.x + 10, promotion_rect.y + 10)

        # Update screen
        pygame.display.update()

    # Quit pygame
    pygame.quit()





























from pygame.locals import *




# Global variables
BUTTONS = 10

# Add button class
class Button():
    def __init__(self, x, y, width, height, text, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.image = image
        self.active = False

    def draw(self, screen, font, color):
        pygame.draw.rect(screen, color, self.rect)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def toggle(self):
        self.active = not self.active

# Return button
return_width = 80
return_height = 40
return_x = WINDOW_SIZE[0] - return_width - 20  # 20 是按钮与窗口边缘的距离
return_y = 20
return_rect = pygame.Rect(return_x, return_y, return_width, return_height)


# Develop supermove_scene
def supermove_scene():
    # Access global variables
    global day, subscriber, popularity, macau_percent, money
    global super_move_media_width,super_move_media_height,return_rect,return_y,return_x,return_height,return_width

    promotion_activated = False
    social_media_activated = False

    # Next day button
    next_day_x = WINDOW_SIZE[0] - 200
    next_day_y = WINDOW_SIZE[1] - 80
    next_day_width = 160
    next_day_height = 60
    next_day_rect = pygame.Rect(next_day_x, next_day_y, next_day_width, next_day_height)


    # Create buttons
    buttons = []
    button_width = 120
    button_height = 60
    button_margin = 10
    button_start_x = 20
    button_start_y = 90

    for i in range(BUTTONS):
        x = button_start_x + (button_width + button_margin) * (i % 5)
        y = button_start_y + (button_height + button_margin) * (i // 5)
        buttons.append(Button(x, y, button_width, button_height, 'Action {}'.format(i+1)))

    # Return button
    return_width = 80
    return_height = 40
    return_x = WINDOW_SIZE[0] - return_width - 20  # 20 是按钮与窗口边缘的距离
    return_y = 20
    return_rect = pygame.Rect(return_x, return_y, return_width, return_height)


    # 停止之前播放中的音樂
    pygame.mixer.music.stop()

    # 播放新的音樂
    pygame.mixer.music.load("supermove.mp3")
    pygame.mixer.music.play(-1)  # -1 表示持續播放

    # Create window
    screen = pygame.display.set_mode(WINDOW_SIZE)



    # 游戏循环
    running = True
    while running:
        # 事件循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查是否点击了下一天按钮
                if next_day_rect.collidepoint(event.pos):
                    # 根据订阅者数量和当前的澳门观众比例计算下降数量
                    macau_drop = max(0, int(subscriber * (macau_percent / 100)))
                    if subscriber > 0:
                        max_drop = max(0.1, 0.5 - subscriber / 20000) # 計算最大下降幅度
                        if subscriber < 1000: # 如果訂閱數很低
                            macau_drop_percent = min(0.01, macau_drop / subscriber) # 將下降比例限制在 10% 以下
                        else:
                            macau_drop_percent = min(1, macau_drop / subscriber) # 計算實際下降比例
                        macau_percent = max(0.1, macau_percent - (macau_drop_percent * (1 + subscriber / 4000) * max_drop))

                    # 更新值
                    subscriber += popularity
                    money += int(subscriber / 30)
                    popularity = max(0, popularity - 1)
                    day += 1
                    if day == 2:
                        second_day_dialogue_scene(screen, font, background, character_images)
                    if day == 3:
                        day_Three_dialogue_scene(screen, font, background, character_images)
                    if promotion_activated:
                        popularity += 1.5
                        money += 0.1
                    if social_media_activated:
                        popularity += 1.3
                        money += 0.1
                        macau_percent += 0.05
                # 检查是否点击了返回按钮
                if return_rect.collidepoint(event.pos):
                    develop_scene()

                # 检查是否点击了按钮
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, button in enumerate(buttons):
                        if button.rect.collidepoint(event.pos):
                            if button.active:
                                button.toggle()
                            else:
                                # Deactivate other buttons
                                for other_button in buttons:
                                    other_button.active = False
                                button.toggle()
                                # 显示图片
                                image_path = 'action_{}_image.png'.format(i+1)
                                action_image = pygame.image.load(image_path)



        font = pygame.font.SysFont(None, 24)



        # 繪製背景圖
        screen.blit(backgroundsupermove1, (0, 0))

        # Check if button is active and update background image accordingly
        if any(button.active for button in buttons):
            screen.blit(backgroundsupermove2, (0, 0))





        # Draw game values
        draw_text(screen, 'Day: {}'.format(day), WHITE, 20, 20)
        pygame.draw.rect(screen, BLACK, pygame.Rect(185, 20, 200, 30))
        draw_text(screen, 'Subscriber: {}'.format(subscriber), WHITE, 200, 30)
        pygame.draw.rect(screen, BLACK, pygame.Rect(415, 20, 200, 30))
        draw_text(screen, 'Popularity: {}'.format(popularity), WHITE, 420, 30)
        pygame.draw.rect(screen, BLACK, pygame.Rect(645, 20, 200, 30))
        draw_text(screen, 'Macau Percent: {}%'.format(macau_percent), WHITE, 630, 30)
        pygame.draw.rect(screen, BLACK, pygame.Rect(895, 20, 200, 30))
        draw_text(screen, 'Money: {} mop'.format(money), WHITE, 900, 30)



        # Draw buttons
        for button in buttons:
            button_color = WHITE if not button.active else (128, 128, 128)
            button.draw(screen, font, button_color)

        # Draw action image if any button is active
        for button in buttons:
            if button.active:
                image_rect = action_image.get_rect()
                image_rect.midleft = (400, WINDOW_SIZE[1] // 2 + 50)
                screen.blit(action_image, image_rect)
                break


        # Draw next day button
        pygame.draw.rect(screen, WHITE, next_day_rect)
        draw_text(screen, 'Next Day', BLACK, next_day_x + 10, next_day_y + 10)
        
        # 绘制返回按钮
        pygame.draw.rect(screen, WHITE, return_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render("Return", True, BLACK)
        text_rect = text.get_rect(center=return_rect.center)
        screen.blit(text, text_rect)




        # Update screen
        pygame.display.update()


    # Quit pygame
    pygame.quit()



























# Define the day_Three_dialogue_scene  function for the day_Three day
def day_Three_dialogue_scene(screen, font, background, character_image):
    # Define the dialogue
    dialogue = [
        ("Pouheng works during the day and does live streaming \nand videos at night. Everything is to ensure a stable\n income for the studio to continue operating.", "melody"),
        ("Looking at Pouheng's tireless efforts, I feel that I\n must use all my Full range of skills to help him.", "melody"),
        ("Good evening, Melody. \nHave you thought of anything today?", "pouheng"),
        ("Currently, only the basic : Patreon can compensate for\n the deficiency of not being able to earn revenue\n from YouTube in Macau.", "melody"),
        ("Although my subscriber count is not enough to monetize\n, But still thanks.", "pouheng"),
        ("...", "melody"),
        ("Regarding the overall direction, we can unite all Macau\n VTubers and break through the walls in Macau. But\n will they follow you?", "melody"),
        ("If they are Macau VTubers, they should be able to \nunderstand our ideas. We may have the possibility\n of unity.", "pouheng"),
        ("Well, let's not talk about this now, I have other plans. \nSince you have chosen me. Then I will absolutely \nhave to fulfill your dream.", "melody"),
        ("Thank you, I am a little moved.", "pouheng"),
        ("(New action Super Move, abbreviated as SM,\nand new Manager Points, abbreviated as MP,\n10 mp have been added.)", "melody")
    ]



    # Stop any previously playing music
    pygame.mixer.music.stop()

    # Load and play new music for the dialogue scene
    pygame.mixer.music.load("conversation2.mp3")
    pygame.mixer.music.play(-1)

    dialogue_index = 0
    while dialogue_index < len(dialogue):
        # Draw the background and character images
        screen.blit(background, (0, 0))
        character_image = character_images[dialogue[dialogue_index][1]]
        character_rect = character_image.get_rect()
        character_rect.bottomleft = (50, screen_height - 50)
        screen.blit(character_image, character_rect)

        # Draw the dialogue box and text
        dialogue_box_rect = pygame.Rect(400, 400, 800,200)
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box_rect)
        dialogue_text = font.render(dialogue[dialogue_index][0], True, (0, 0, 0))
        dialogue_text_rect = dialogue_text.get_rect()
        dialogue_text_rect.topleft = (dialogue_box_rect.left + 50, dialogue_box_rect.top + 50)

        # Calculate the height of the dialogue box
        line_spacing = 5
        dialogue_lines = dialogue[dialogue_index][0].split("\n")
        dialogue_height = sum(font.size(line)[1] + line_spacing for line in dialogue_lines)
        dialogue_box_rect.height = dialogue_height + 100

        # Adjust the size of the dialogue box
        if dialogue_text_rect.width > dialogue_box_rect.width - 100:
            dialogue_box_rect.width = dialogue_text_rect.width + 100

        dialogue_box_rect.top = screen_height - 200 - dialogue_height - 50

        # Draw the dialogue box and text
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box_rect)
        dialogue_text_rect.topleft = (dialogue_box_rect.left + 50, dialogue_box_rect.top + 50)
        for line in dialogue_lines:
            line_surface = font.render(line, True, (0, 0, 0))
            screen.blit(line_surface, dialogue_text_rect)
            dialogue_text_rect.top += line_surface.get_height() + line_spacing

        # Update the display
        pygame.display.update()

        # Listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Advance the dialogue
                    dialogue_index += 1
                    if dialogue_index == len(dialogue):
                        # If the dialogue is finished, return to the game scene
                        develop_scene() # Go to the next scene


















# Define the dialogue scene function for the second day
def second_day_dialogue_scene(screen, font, background, character_image):
    # Define the dialogue
    dialogue = [
        ("Melody, how do you feel about \nyour first day of work?", "pouheng"),
        ("It's good. The studio is comfortable,\n but the situation is not optimistic.", "melody"),
        ("You haven't carefully managed social media \nin the past 10 years. You don't know how to create exaggerated\n effects or how to act crazy. You always present the content\n you think is best in a straightforward manner.", "melody"),
        ("Although your voice is low and pleasant, \nit's difficult to achieve any \nexaggerated effects because of that...", "melody"),
        ("However, the most serious problem is still on YouTube.\n Should we consider changing the platform?", "melody"),
        ("Calm down a little. If even you are panicking,\n then I have no one to rely on.", "pouheng"),
        ("Um, sorry.", "melody"),
        ("If it's not necessary, I won't give up on YouTube \nbecause that's where my dream started.\n When I was in elementary school,\n I watched my favorite YouTubers, and I decided to \nbecome one of them and bring joy.", "pouheng"),
        ("So there's no need to panic. We can\n take it slow, one step at a time.\nI've gotten used to not having an \naudience for the past 10 years", "pouheng"),
        ("(Although I really want to tell him that traffic doesn't\n accumulate slowly step by step, but usually bursts out in an\n instant, but looking at him, with his\n determined gaze and his heart-wrenching story,\n I don't have the heart to say it.)", "melody"),
        ("Okay, I understand. In any case, let's\n think of some solutions first.", "melody")
    ]



    # Stop any previously playing music
    pygame.mixer.music.stop()

    # Load and play new music for the dialogue scene
    pygame.mixer.music.load("conversation.mp3")
    pygame.mixer.music.play(-1)

    dialogue_index = 0
    while dialogue_index < len(dialogue):
        # Draw the background and character images
        screen.blit(background, (0, 0))
        character_image = character_images[dialogue[dialogue_index][1]]
        character_rect = character_image.get_rect()
        character_rect.bottomleft = (50, screen_height - 50)
        screen.blit(character_image, character_rect)

        # Draw the dialogue box and text
        dialogue_box_rect = pygame.Rect(400, 400, 800,200)
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box_rect)
        dialogue_text = font.render(dialogue[dialogue_index][0], True, (0, 0, 0))
        dialogue_text_rect = dialogue_text.get_rect()
        dialogue_text_rect.topleft = (dialogue_box_rect.left + 50, dialogue_box_rect.top + 50)

        # Calculate the height of the dialogue box
        line_spacing = 5
        dialogue_lines = dialogue[dialogue_index][0].split("\n")
        dialogue_height = sum(font.size(line)[1] + line_spacing for line in dialogue_lines)
        dialogue_box_rect.height = dialogue_height + 100

        # Adjust the size of the dialogue box
        if dialogue_text_rect.width > dialogue_box_rect.width - 100:
            dialogue_box_rect.width = dialogue_text_rect.width + 100

        dialogue_box_rect.top = screen_height - 200 - dialogue_height - 50

        # Draw the dialogue box and text
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box_rect)
        dialogue_text_rect.topleft = (dialogue_box_rect.left + 50, dialogue_box_rect.top + 50)
        for line in dialogue_lines:
            line_surface = font.render(line, True, (0, 0, 0))
            screen.blit(line_surface, dialogue_text_rect)
            dialogue_text_rect.top += line_surface.get_height() + line_spacing

        # Update the display
        pygame.display.update()

        # Listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Advance the dialogue
                    dialogue_index += 1
                    if dialogue_index == len(dialogue):
                        # If the dialogue is finished, return to the game scene
                        develop_scene() # Go to the next scene






# 定義對話場景
def dialogue_scene(screen, font, background, character_images):
    # 繪製對話場景
    dialogue = [
        ("Hello I'm pouheng!\nare you my new manager?\n(Please press spacebar to continue)", "pouheng"),
        ("yes I just got off the plane, \nmacau is such a beautiful place.", "melody"),
        (" ok… let me introduce myself. \nI'm a vtuber as you already\n know.I'm confident in my editing \nskills and  streaming..", "pouheng"),
        (" hmm but you don't have any viewers…", "melody"),
        ("yes. in macau youtube will not \nprovide membership and super chat \n not even advertisement, so in the place \nthat won't give you to money, \nYou won't promote their videos, will you?", "pouheng"),
        (" yes, and that's my job, hmm… \nmy name is melody ,nice to meet you!", "melody"),
        (" yeah, let's get started!", "pouheng")
    ]

    # 停止之前播放中的音樂
    pygame.mixer.music.stop()

    # 播放新的音樂
    pygame.mixer.music.load("conversation.mp3")
    pygame.mixer.music.play(-1)  # -1 表示持續播放


    dialogue_index = 0
    while dialogue_index < len(dialogue):
        # 繪製背景圖和角色頭像
        screen.blit(background, (0, 0))
        character_image = character_images[dialogue[dialogue_index][1]]
        character_rect = character_image.get_rect()
        character_rect.bottomleft = (50, screen_height - 50)
        screen.blit(character_image, character_rect)

        # 繪製對話框和文字
        dialogue_box_rect = pygame.Rect(400, 400, 800, 200)
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box_rect)
        dialogue_text = font.render(dialogue[dialogue_index][0], True, (0, 0, 0))
        dialogue_text_rect = dialogue_text.get_rect()
        dialogue_text_rect.topleft = (dialogue_box_rect.left + 50, dialogue_box_rect.top + 50)

        # 計算對話框的高度
        line_spacing = 5
        dialogue_lines = dialogue[dialogue_index][0].split("\n")
        dialogue_height = sum(font.size(line)[1] + line_spacing for line in dialogue_lines)
        dialogue_box_rect.height = dialogue_height + 100

        # 調整對話框的大小
        if dialogue_text_rect.width > dialogue_box_rect.width - 100:
            dialogue_box_rect.width = dialogue_text_rect.width + 100

        dialogue_box_rect.top = screen_height - 200 - dialogue_height - 50

        # 繪製對話框和文字
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box_rect)
        dialogue_text_rect.topleft = (dialogue_box_rect.left + 50, dialogue_box_rect.top+ 50)
        for line in dialogue_lines:
            line_surface = font.render(line, True, (0, 0, 0))
            screen.blit(line_surface, dialogue_text_rect)
            dialogue_text_rect.top += line_surface.get_height() + line_spacing

        # 更新畫面
        pygame.display.update()

        # 監聽事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 推進對話
                    dialogue_index += 1
                    if dialogue_index == 7:
                        develop_scene() # 进入下一个场景



# 難度選擇場景
def difficulty_select_scene(screen, font, background, character_images):
    # 繪製背景圖
    screen.blit(background, (0, 0))

    # 繪製文字
    title_text = font.render("Difficulty Select", True, (255, 255, 255))
    title_rect = title_text.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.top = 100
    screen.blit(title_text, title_rect)

    option1_text = font.render("Macau People Mode", True, (255, 255, 255))
    option1_rect = option1_text.get_rect()
    option1_rect.centerx = screen.get_rect().centerx
    option1_rect.top = 300
    screen.blit(option1_text, option1_rect)

    option2_text = font.render("Extreme Hardcore Mode", True, (255, 255, 255))
    option2_rect = option2_text.get_rect()
    option2_rect.centerx = screen.get_rect().centerx
    option2_rect.top = 400
    screen.blit(option2_text, option2_rect)

    # 創建新的字體對象，並使用它來繪製更小的提示文字
    small_font = pygame.font.Font(None, 24)
    hint_text = small_font.render("Pro tips: they're all the same", True, (255, 255, 255))
    hint_rect = hint_text.get_rect()
    hint_rect.centerx = screen.get_rect().centerx
    hint_rect.top = 500
    screen.blit(hint_text, hint_rect)

    pygame.display.update()

    # 監聽事件
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # 檢查是否按下其中一個選項
                if option1_rect.collidepoint(event.pos) or option2_rect.collidepoint(event.pos):
                    # 進入對話場景
                    dialogue_scene(screen, font, background, character_images)
                    return 

        # 更新畫面
        pygame.display.update()

    

# 繪製標題介面
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                # 進入難度選擇場景
                difficulty_select_scene(screen, font, background, character_images)




    # 繪製背景圖
    screen.blit(background, (0, 0))

    # 繪製按鈕
    start_button = font.render("Start Game", True, (255, 255, 255))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(start_button, start_button_rect)

    continue_button = font.render("Continue Game", True, (255, 255, 255))
    continue_button_rect = continue_button.get_rect()
    continue_button_rect.center = (screen_width // 2, screen_height // 2 + 50)
    screen.blit(continue_button, continue_button_rect)

    quit_button = font.render("Quit Game", True, (255, 255, 255))
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.center = (screen_width // 2, screen_height // 2 + 100)
    screen.blit(quit_button, quit_button_rect)

    # 更新畫面
    pygame.display.update()



























