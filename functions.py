import requests
import pygame
import time

pygame.init()
pygame.display.set_caption('DESPO Robot Visualizer')
screen = pygame.display.set_mode((800, 600))

print("Downloading Robot Sprite.")
with open('robot.png', 'wb') as spritedownload:
    spritedownload.write(requests.get('https://github.com/ThatError404/Project-DESPO/blob/main/Images/Robot.png?raw=true').content)
robot_sprite = pygame.image.load('robot.png')
robot_sprite = pygame.transform.scale(robot_sprite, (64, 64))
print("Downloaded Robot Sprite.")
print("Starting Robot Visualizer.")

rotation = "rotation"

def draw_robot(x, y):
    screen.fill((0, 0, 0))
    screen.blit(robot_sprite, (x, y))
    pygame.display.update()
    time.sleep(0.01)

def backward(idk, type, times):
    print("Robot Moving Backwards (Down): " + str(times) + " Times |  Movement Type: " + str(type))
    if type == rotation:
        for i in range(0, times):
            time.sleep(0.1)
            rx = robot_sprite.get_rect
            ry = robot_sprite.get_rect().y
            draw_robot(rx, ry + 10)
        time.sleep(1)

draw_robot(365, 250)
backward(0, rotation, 50)

print("Robot Finished.")
time.sleep(3)
pygame.quit()