import pygame
import time
import os
class Node:
    def __init__(self,song):
        self.song=song
        self.prev=None
        self.next=None

class Playlist:
    def __init__(self):
            self.head=None
            self.tail=None
            self.current=None
            self.current_position = 0
            
    def addSong(self,song_name):
        newNode=Node(song_name)
        if not self.head:
            self.head=self.tail=self.current=newNode
            print(f"Added: {song_name}")
            return
        self.tail.next=newNode
        self.head.prev=newNode
        newNode.prev=self.tail
        newNode.next=self.head
        self.tail=newNode
        print(f"Added: {song_name}")
        
    def removeSong(self,song_name):
        if not self.head:
            return
        if song_name==self.head.song:
            self.head.next.prev=self.head.prev
            self.head.prev.next=self.head.next
            self.head=self.head.next
            print(f"Removed: {song_name}")
            return 
    
        if song_name==self.tail.song:
            self.tail.prev.next=self.tail.next
            self.tail.next.prev=self.tail.prev
            self.tail=self.tail.prev
            print(f"Removed: {song_name}")
            return
        
        temp=self.head
        while True:
            if temp.song==song_name:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                print(f"Removed: {song_name}")
                return
            temp=temp.next
            if temp==self.head:
                return
    
    def play_song(self):
        if not self.current:
            print("No song in playlist.")
            return
        pygame.mixer.music.load(self.current.song)
        pygame.mixer.music.play(loops=0, start=self.current_position)
        print(f"Playing: {self.current.song}")
        
    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_song()
    
    def stop_song(self):
        pygame.mixer.music.stop()
        
    def pause_song(self):
        if self.current:
            pygame.mixer.music.pause() 
            print(f'Paused: {os.path.basename(self.current.song)}')
            
    def resume_song(self):
        if self.current:
            pygame.mixer.music.unpause() 
            print(f'Resumed: {os.path.basename(self.current.song)}')

    def prev_song(self):
        if self.current and self.current.prev:
            self.stop_song()
            self.current = self.current.prev
            self.play_song()
              
    def display(self):
        temp=self.head
        if not temp:
            print("Playlist is Empty")
            return
        print("Playlist")
        while True:
            print(f"{temp.song}")
            temp=temp.next
            if temp==self.head:
                return
            
    def printing(self):
        print(self.head.prev.song)
        print(self.head.next.song)
        print(self.tail.next.song)
        print(self.tail.prev.song)
        
        
pygame.init()
screen = pygame.display.set_mode((350, 600))
pygame.display.set_caption("PyFy")
font = pygame.font.SysFont(None, 36)

playlist = Playlist()
playlist.addSong("drill.mp3")
playlist.addSong("gunehgaar.mp3")
playlist.addSong("punyapaap.mp3")

play_button_rect = pygame.Rect(100, 100, 150, 50)
pause_button_rect = pygame.Rect(100, 160, 150, 50)
resume_button_rect = pygame.Rect(100, 220, 150, 50)
next_button_rect = pygame.Rect(100, 280, 150, 50)
prev_button_rect = pygame.Rect(100, 340, 150, 50)
exit_button_rect = pygame.Rect(100, 400, 150, 50)

def draw_buttons():
    pygame.draw.rect(screen, (0, 0, 0), play_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), pause_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), resume_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), next_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), prev_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), exit_button_rect, 3)

    play_text = font.render('Play', True, (0, 0, 0))
    screen.blit(play_text, (play_button_rect.x + (play_button_rect.width - play_text.get_width()) // 2,
                            play_button_rect.y + (play_button_rect.height - play_text.get_height()) // 2))
    
    pause_text = font.render('Pause', True, (0, 0, 0))
    screen.blit(pause_text, (pause_button_rect.x + (pause_button_rect.width - pause_text.get_width()) // 2,
                             pause_button_rect.y + (pause_button_rect.height - pause_text.get_height()) // 2))
    
    resume_text = font.render('Resume', True, (0, 0, 0))
    screen.blit(resume_text, (resume_button_rect.x + (resume_button_rect.width - resume_text.get_width()) // 2,
                              resume_button_rect.y + (resume_button_rect.height - resume_text.get_height()) // 2))  
    
    next_text = font.render('Next', True, (0, 0, 0))
    screen.blit(next_text, (next_button_rect.x + (next_button_rect.width - next_text.get_width()) // 2,
                            next_button_rect.y + (next_button_rect.height - next_text.get_height()) // 2))

    prev_text = font.render('Prev', True, (0, 0, 0))
    screen.blit(prev_text, (prev_button_rect.x + (prev_button_rect.width - prev_text.get_width()) // 2,
                            prev_button_rect.y + (prev_button_rect.height - prev_text.get_height()) // 2))

    exit_text = font.render('Exit', True, (0, 0, 0))
    screen.blit(exit_text, (exit_button_rect.x + (exit_button_rect.width - exit_text.get_width()) // 2,
                            exit_button_rect.y + (exit_button_rect.height - exit_text.get_height()) // 2))


running = True
while running:
    screen.fill((66, 189, 66))  
    draw_buttons()
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                playlist.play_song()
            elif pause_button_rect.collidepoint(event.pos):
                playlist.pause_song()
            elif resume_button_rect.collidepoint(event.pos):
                playlist.resume_song()
            elif next_button_rect.collidepoint(event.pos):
                playlist.next_song()
            elif prev_button_rect.collidepoint(event.pos):
                playlist.prev_song()
            elif exit_button_rect.collidepoint(event.pos):
                running = False

    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()