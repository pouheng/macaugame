import pygame

# Initialize pygame
pygame.init()


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

















