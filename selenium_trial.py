""" A bot in a null-shell basically, it does repetitive tasks for someone. 
Completes the assignment faster than a human and gives the human more time to do other stuff."""

# Libraries
import selenium 
import instapy
from selenium import webdriver
from instapy import smart_run
from random import randint
from time import sleep

brower = webdiver.Chorme() 
brower.get('https://www.instagram.com/')

sleep(randint(5,25))


brower.close