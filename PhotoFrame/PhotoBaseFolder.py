# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:23:53 2020

@author: karel
"""
import os
import random

class PhotoBaseFolder:
    def __init__(self, folderName = r"D:\Photos_Freya"):
        self.folder = folderName
        self.index = 0
        self.subfolderlist = []
        
    def checkFolder(self):
        if os.path.isdir(self.folder):
            return True
        else:
            raise ValueError
            
    def subFolderList(self):
        if self.checkFolder():
            return dirs = os.listdir(self.folder)
    
    def set_subfolderlist(self):
        self.subfolderlist = self.subFolderList()
        
    def set_randomindex(self):
        self.index = random.randint(0, len(self.subfolderlist))
        
    def nextindex(self):
        self.index = (self.index + 1) % len(self.subfolderlist)
        
    def getsubfolder(self):
        return os.path.join(self.folder, self.subfolderlist[self.index])
    
    def getsubfolderphotolist(self):
        photoFolder = self.getsubfolder()
        photolist = []
        for root, dirs, files in os.walk(photoFolder):
            for file in files:
                if file.endswith(('.jpg', '.JPG')):
                    photolist.append(os.path.join(root, file))
                    
        return photolist