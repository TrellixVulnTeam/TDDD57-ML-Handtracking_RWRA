import pygame
import time
import random
import cv2
import mediapipe as mp
from hand import Hand
from box import Box

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.surface.fill((255,255,255))

        #Load camera (webcam)
        self.cap = cv2.VideoCapture(0) 

        self.start_time = time.time()

        self.hands = Hand()

        self.box1 = Box(100, 100, 50, 100, pygame.Color(220, 20, 20))
        self.box2 = Box(250, 100, 60, 40, pygame.Color(220, 20, 180))
        self.box3 = Box(500, 100, 100, 100, pygame.Color(20, 20, 220))


    def load_camera(self):
        #Store the current frame from webcam
        _, self.frame = self.cap.read()
    
    def draw(self):
        #Draw
        curr_time = time.time() - self.start_time

        # Initialing Color
        self.surface.fill((0,0,0))

        # Drawing Rectangle, Rect(left, top, width, height)
        self.box1.draw(self.surface)
        self.box2.draw(self.surface)
        self.box3.draw(self.surface)
        
        #Draw rectangles to inser the boxes in
        pygame.draw.rect(self.surface, (66, 150, 178), pygame.Rect(300, 400, 150, 150), 1)
        pygame.draw.rect(self.surface, (66, 150, 178), pygame.Rect(500, 400, 40, 40), 1)
        pygame.draw.rect(self.surface, (66, 150, 178), pygame.Rect(600, 400, 80, 80), 1)
    
    
    #Controll the boxes is being selectede or not  
    def check_the_boxes(self):
        self.box1.collide(self.hands)
        self.box2.collide(self.hands)
        self.box3.collide(self.hands)   
      
        
    def update(self):
        self.load_camera()

        #Draw landmarks and process hand positions
        self.frame = self.hands.process_hands(self.frame)

        # --- LAB 1: hold over to select & pinch to select --
        #Compare hand position to boxes
        #Change color saturation if marker is covering one of the boxes
        self.check_the_boxes()

        
        self.draw()       
        
        #Draw hand marker based on hand position
        self.hands.draw_marker(self.surface)
        
        #Show webcam with landmarks on screen
        cv2.imshow("Frame", cv2.flip(self.frame, 1))
        cv2.waitKey(1)
        
        pygame.display.update()