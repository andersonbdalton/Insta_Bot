""" A bot in a null-shell basically, it does repetitive tasks for someone. 
Completes the assignment faster than a human and gives the human more time to do other stuff."""

# Libraries
import instapy 
import selenium
from selenium import webdriver
from instapy import smart_run
from random import randint
from time import sleep

brower = webdiver.Chorme() 
brower.get('https://www.instagram.com/')

sleep(randint(5,25))


brower.close

# login credentials - I should store in a different file but for now.
insta_user = 'daltonbanderson'
insta_password = 'Anderson@11'

# set headless_browser=True to run InstaPy in the background
session = ipy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    min_followers=850,
                                    min_following=300)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.like_by_tags(["fitness"], amount=10)

