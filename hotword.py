#!/usr/bin/env python

#RUN AS PYTHON 2

from __future__ import print_function
'''
#only import game when you get the keyword to play it
#import game module to play the game
from game_2 import main
'''

import argparse
import os.path
import json
#imported the credentials
import google.oauth2.credentials
#import needed modules here
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.event import Event
from google.assistant.library.event import IterableEventQueue
from google.assistant.library.file_helpers import existing_file



#prints out events dont mess
def process_event(event):
    """Pretty prints events.

    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.

    Args:
        event(event.Event): The current event to process.
    """
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()
    #print(Event.getText() + "peanut butter")
    #if event.args == ['hello']:
        #print("hello")

    #if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        #print(EventType.ON_RECOGNIZING_SPEECH_FINISHED.get('text'))

    #if event.type == EventType.ON_NO_RESPONSE:
        #from game_2 import main
    if event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT:
        from game_2 import main

    print(event)

    #print(event.keys())
    #if 'RPG' in event:
        #from game_2 import main
    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()

#make new event



def main():

    #this parses all of the arguments from the spoken word
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    #RPG = Event(5,{'RPG game':True, 'start roleplayingg game': True})
    args = parser.parse_args()
    #loads credential client secret
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))
#goes through all of the events
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event)
        #for event in Event():
            #process_event(event)

if __name__ == '__main__':
    main()
