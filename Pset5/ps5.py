
# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
        
    def get_title(self):
        return self.title
        
    def get_description(self):
        return self.description
        
    def get_link(self):
        return self.link
        
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def is_phrase_in(self, text):
                
        punctuation = list(string.punctuation)
        text = text.lower()
        
        ## SUBSTITUTE PUNCTUATION FOR SPACES
        for i in punctuation:
            text = text.replace(i, ' ')
        
        ## SPLIT PHRASE AND TEXT BY SPACES
        split_phrase = self.phrase.split()  
        split_text = text.split()   
           
        ## FIND FIRST WORD, AND LOOK FOR NEXT WORDS
        try:
            index = split_text.index(split_phrase[0])
            index_final = split_text.index(split_phrase[-1])  
            if index_final > index:
                for i in range(1, len(split_phrase)):                          
                    if not split_phrase[i] == split_text[index+i]:
                        return False
            else:
                return False
        except ValueError or IndexError:           
            return False
        
        return True
    
    def evaluate(self, text):        
        return self.is_phrase_in(text)

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):       
    def evaluate(self, NewsStory):          
        title = NewsStory.get_title()
        return self.is_phrase_in(title)        
    
    
# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):       
    def evaluate(self, NewsStory):          
        description = NewsStory.get_description()
        return self.is_phrase_in(description)    

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.


class TimeTrigger(Trigger):
    def __init__(self, timestring):
        self.time = datetime.strptime(timestring, '%d %b %Y %H:%M:%S').replace(tzinfo=pytz.timezone("EST"))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):   
    def evaluate(self, NewsStory):        
        pubdate = NewsStory.pubdate.replace(tzinfo=pytz.timezone("EST"))
                
        if self.time > pubdate:
            return True
        return False      

class AfterTrigger(TimeTrigger):   
    def evaluate(self, NewsStory):
        pubdate = NewsStory.pubdate.replace(tzinfo=pytz.timezone("EST"))
        
        if self.time < pubdate:
            return True
        return False          
    

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self, Trigger):
        self.Trigger = Trigger       
        
    def evaluate(self, text):        
        return not self.Trigger.evaluate(text)
        

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self, Trigger, anotherTrigger):
        self.Trigger = Trigger  
        self.anotherTrigger = anotherTrigger
        
    def evaluate(self, text):        
        return self.Trigger.evaluate(text) and self.anotherTrigger.evaluate(text)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, Trigger, anotherTrigger):
        self.Trigger = Trigger  
        self.anotherTrigger = anotherTrigger
        
    def evaluate(self, text):        
        return self.Trigger.evaluate(text) or self.anotherTrigger.evaluate(text)
    

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    
    stories_return = []
    
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i):
                stories_return.append(i)                
   
    return list(set(stories_return))


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    triggerTypes = {
        'TITLE': TitleTrigger,
        'DESCRIPTION': DescriptionTrigger,
        'AFTER': AfterTrigger,
        'BEFORE': BeforeTrigger, 
        'AND': AndTrigger, 
        'OR': OrTrigger, 
        'NOT': NotTrigger       
        }
    
    triggerDict = {}
    triggerList = []
    
    for i in lines:
        trigger = i.split(',')
        if (trigger[1] == 'AND' or trigger[1] == 'OR') and trigger[0] != 'ADD':
            mytrigger = triggerTypes[trigger[1]](triggerDict[trigger[2]], triggerDict[trigger[3]])
        elif trigger[0] != 'ADD':
            mytrigger = triggerTypes[trigger[1]](trigger[2])
        triggerDict[trigger[0]] = mytrigger
        
        if trigger[0] == 'ADD':
            for j in range(1, len(trigger)):
                triggerList.append(triggerDict[trigger[j]])
            
    return triggerList


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        ##t1 = TitleTrigger("election")
        ##t2 = DescriptionTrigger("Trump")
        ##t3 = DescriptionTrigger("Clinton")
        ##t4 = AndTrigger(t2, t3)
        ##triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
    

