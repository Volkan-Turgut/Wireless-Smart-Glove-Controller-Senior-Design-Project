import pygame
import random
import threading
import sys
import imageio

# Initialize Pygame
pygame.init()

# Window dimensions
window_width = 400
window_height = 1000



# Grid dimensions and cell size
grid_width = 10
grid_height = 25
grid_size = window_width // grid_width

image = pygame.image.load("screenshot-active.jpg")
image_width = image.get_width()-1
image_height = image.get_height()-10


# Image position
image_x = (window_width - image_width) // 2
image_y = (window_height - image_height) // 2



# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Define shapes and their colors
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

SHAPE_COLORS = [CYAN, YELLOW, ORANGE, BLUE, RED, GREEN, PURPLE]

# Initialize the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")

# Initialize the clock
clock = pygame.time.Clock()

# Game state variables


# Initialize the grid
grid = [[0] * grid_width for _ in range(grid_height)]

# Initialize the current shape and its position
current_shape = random.choice(SHAPES)
current_shape_color = random.choice(SHAPE_COLORS)
shape_x = (grid_width - len(current_shape[0])) // 2
shape_y = 0

# Create a lock to synchronize access to shared game state
lock = threading.Lock()

# Fonts for displaying text
font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 24)


def draw_grid():
    """Draw the game grid."""
    for x in range(0, window_width, grid_size):
        pygame.draw.line(window, WHITE, (x, 0), (x, window_height))
    for y in range(0, window_height, grid_size):
        pygame.draw.line(window, WHITE, (0, y), (window_width, y))


def draw_shape(shape, x, y, color):
    """Draw a shape on the grid."""
    for row in range(len(shape)):

        for col in range(len(shape[row])):
            if shape[row][col]:
                pygame.draw.rect(window, color, (x + col * grid_size, y + row * grid_size, grid_size, grid_size))


def check_collision(shape, x, y, grid):
    """Check if the shape collides with the grid or other placed shapes."""
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if (x + col < 0 or x + col >= grid_width or y + row >= grid_height or grid[y + row][x + col]):
                    return True
    return False

def clear_rows(grid):
    """Clear full rows from the grid and return the number of cleared rows."""
    full_rows = []
    for row in range(grid_height):
        if all(grid[row]):
            full_rows.append(row)
            for r in range(row, 0, -1):
                grid[r] = grid[r - 1][:]
    for row in full_rows:
        grid[0] = [0] * grid_width
    return len(full_rows)



def rotate_shape(shape):
    """Rotate the shape clockwise around its center."""
    rows = len(shape)
    cols = len(shape[0])
    rotated_shape = [[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            rotated_shape[col][rows - 1 - row] = shape[row][col]

    return rotated_shape




# def draw_menu():
#     """Draw the menu page."""
#     window.fill(BLACK)
#     title_text = font_large.render("Tetris", True, WHITE)
#     title_rect = title_text.get_rect(center=(window_width // 2, window_height // 2 - 50))
#     window.blit(title_text, title_rect)

#     instructions_text = font_small.render("Press ENTER to start", True, WHITE)
#     instructions_rect = instructions_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
#     window.blit(instructions_text, instructions_rect)

#     pygame.display.flip()

def end_game():
    """Display the game over screen."""
    countdown_duration = 5  # Countdown duration in seconds
    countdown_start_time = pygame.time.get_ticks()  # Get the current time
    

    while True:
        # Calculate the remaining time
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - countdown_start_time) // 1000
        remaining_time = countdown_duration - elapsed_time

        # Draw the game over screen
        window.fill(BLACK)
        game_over_text = font_large.render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(game_over_text, game_over_rect)

        final_score_text = font_small.render("Final Score: " + str(score), True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
        window.blit(final_score_text, final_score_rect)

        countdown_text = font_small.render("Restarting in " + str(remaining_time) + " seconds", True, WHITE)
        countdown_rect = countdown_text.get_rect(center=(window_width // 2, window_height // 2 + 100))
        window.blit(countdown_text, countdown_rect)

        pygame.display.flip()
        # Check if the countdown is complete
        if remaining_time <= 0:
            game_reset()
            break

        pygame.time.delay(1000)  # Delay for 1 second 
        
        
        




def game_loop():
    """Main game loop."""
    global score, grid, current_shape, current_shape_color, shape_x, shape_y
    game_over_flag = False
    pause_flag = False
    score = 0

    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not pause_flag and not check_collision(current_shape, shape_x - 1, shape_y, grid) and shape_x > 0:
                        shape_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not pause_flag and not check_collision(current_shape, shape_x + 1, shape_y, grid) and shape_x + len(current_shape[0]) < grid_width:
                        shape_x += 1
                elif event.key == pygame.K_DOWN:
                    if not pause_flag and not check_collision(current_shape, shape_x, shape_y+1, grid) and shape_y + len(current_shape) < grid_height:
                        while not check_collision(current_shape, shape_x, shape_y+1, grid) and shape_y + len(current_shape) < grid_height:
                         shape_y += 1  
                elif event.key == pygame.K_SPACE:
                    if not pause_flag:
                        rotated_shape = rotate_shape(current_shape)
                        if not check_collision(rotated_shape, shape_x, shape_y, grid):
                            current_shape = rotated_shape
                elif event.key == pygame.K_p:
                    if not game_over_flag:
                        pause_flag = not pause_flag

        if not pause_flag:
            if not check_collision(current_shape, shape_x, shape_y + 1, grid) and shape_y + len(current_shape) < grid_height:
                shape_y += 1
            else:
                for row in range(len(current_shape)):
                    for col in range(len(current_shape[row])):
                        if current_shape[row][col]:
                            grid[shape_y + row][shape_x + col] = 1

                score += clear_rows(grid)
                current_shape = random.choice(SHAPES)
                current_shape_color = random.choice(SHAPE_COLORS)
                shape_x = (grid_width - len(current_shape[0])) // 2
                shape_y = 0

                if check_collision(current_shape, shape_x, shape_y, grid):
                    game_over_flag = True
                    end_game()

        window.fill(BLACK)
    
        draw_grid()

        for row in range(grid_height):
            for col in range(grid_width):
                if grid[row][col]:
                    pygame.draw.rect(window, current_shape_color, (col * grid_size, row * grid_size, grid_size, grid_size))

        draw_shape(current_shape, shape_x * grid_size, shape_y * grid_size, current_shape_color)

        score_text = font_small.render("Score: " + str(score), True, RED)
        window.blit(score_text, (10, 15))

        if pause_flag:
            draw_pause_menu()

        pygame.display.flip()
        clock.tick(5)





def game_reset():
    """Reset the game state and start a new game."""
    global game_over_flag, pause_flag, score, grid, current_shape, current_shape_color, shape_x, shape_y
    game_over_flag = False
    pause_flag = False
    score = 0
    grid = [[0] * grid_width for _ in range(grid_height)]
    current_shape = random.choice(SHAPES)
    current_shape_color = random.choice(SHAPE_COLORS)
    shape_x = (grid_width - len(current_shape[0])) // 2
    shape_y = 0
    game_loop()

def draw_pause_menu():
    """Draw the pause menu page."""
    window.fill(BLACK)
    window.blit(image, (image_x, image_y+50)) 
    pause_text = font_large.render("Paused", True, WHITE)
    pause_rect = pause_text.get_rect(center=(window_width // 2, window_height // 2 - 50))
    window.blit(pause_text, pause_rect)

    resume_text = font_small.render("1. Resume", True, WHITE)
    resume_rect = resume_text.get_rect(center=(window_width // 2, window_height // 2 + 10))
    window.blit(resume_text, resume_rect)

    restart_text = font_small.render("2. Restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(window_width // 2, window_height // 2 + 40))
    window.blit(restart_text, restart_rect)
    

    how_to_play_text = font_small.render("3. How to Play", True, WHITE)
    how_to_play_rect = how_to_play_text.get_rect(center=(window_width // 2, window_height // 2 + 70))
    window.blit(how_to_play_text, how_to_play_rect)

    quit_game_text = font_small.render("4. Quit Game", True, WHITE)
    quit_game_rect = quit_game_text.get_rect(center=(window_width // 2, window_height // 2 + 100))
    window.blit(quit_game_text, quit_game_rect)

    

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop()
                      # Resume game
                elif event.key == pygame.K_2:
                    game_reset()
                elif event.key == pygame.K_3:
                    draw_how_to_play_menu()
                    return
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()




def draw_how_to_play_menu():
    """Draw the How to Play menu page."""
    window.fill(BLACK)
    window.blit(image, (image_x, image_y)) 
    title_text = font_large.render("HOW TO PLAY", True, WHITE)
    title_rect = title_text.get_rect(center=(window_width // 2, window_height // 3 ))
    window.blit(title_text, title_rect)

    instructions_text = font_small.render("   Interactive Tetris played same as Tetris game.", True, WHITE)
    instructions_text2 = font_small.render("You can go right/left and you can rotate the block.", True, WHITE)
    instructions_text3 = font_small.render("The Commands are:", True, WHITE)
    instructions_text4 = font_small.render("Turn Right:", True, WHITE)
    instructions_text5 = font_small.render("Turn Left:", True, WHITE)
    instructions_text6 = font_small.render("Release the block:", True, WHITE)
    instructions_text7 = font_small.render("Rotate:", True, WHITE)
    instructions_text8 = font_small.render("Pause:", True, WHITE)
    instructions_rect = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 30))
    instructions_rect2 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 50))
    instructions_rect3 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 70))
    instructions_rect4 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 100))
    instructions_rect5 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 135))
    instructions_rect6 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 165))
    instructions_rect7 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 195))
    instructions_rect8 = instructions_text.get_rect(center=(window_width // 2, window_height // 3 + 225))



    window.blit(instructions_text, instructions_rect)
    window.blit(instructions_text2, instructions_rect2)
    window.blit(instructions_text3, instructions_rect3)
    window.blit(instructions_text4, instructions_rect4)
    window.blit(instructions_text5, instructions_rect5)
    window.blit(instructions_text6, instructions_rect6)
    window.blit(instructions_text7, instructions_rect7)
    window.blit(instructions_text8, instructions_rect8) 

    


    back_text = font_small.render("Press 1 to go back", True, WHITE)
    back_rect = back_text.get_rect(center=(window_width // 2, window_height // 2 + 95))
    window.blit(back_text, back_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                draw_pause_menu()
                return
def main():
    """Main function to run the game."""
    while 1:
        game_loop()
        
          
         
  

if __name__ == "__main__":
    main()

