# eyed3 module to load audiofiles
import eyed3

from os import listdir

def replaceTitle(mypath, oldWord, newWord):
    for file in listdir(mypath):
        songfile = eyed3.load(f"{mypath}/{file}")
        oldTitleTag = str(songfile.tag.title)
        newTitleTag = oldTitleTag.replace(oldWord,newWord)
        songfile.tag.title = newTitleTag
        songfile.tag.save()
        print(f"{file} - Old Title '{oldTitleTag}' is replaced with title '{newTitleTag}'")

"""
    For example,
    In my music folder, I have splited using genre. 
    But all the song title are having word 'Album' which shows on my music player
    So I need to change all the files title

    Make sure you have only audio files in that folder path

    Also by using eyed3, we can add or remove other metatags 
"""
if __name__ == "__main__":
    folderPath = '' # Give the folder path
    oldWord = 'Album' # Eg- Album
    newWord = 'Romance' 
    replaceTitle()
