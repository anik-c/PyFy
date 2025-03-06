import pygame
class Node:
    def __init__(self,song):
        self.song=song
        self.prev=self.song
        self.next=self.song

class Playlist:
    def __init__(self):
            self.head=None
            self.tail=None
            self.current=None
            
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
        
        
p=Playlist()
p.addSong("happybirthday.mp3")
p.addSong("jinglebell.mp3")
p.addSong("paniparyo.mp3")
p.addSong("paniparena.mp3")
# p.addSong(3)
# p.addSong(4)
p.removeSong("paniparena.mp3")
# p.printing()
# p.display()            