#!/usr/bin/env python
# Determine the Twitter 'reach' for a userid
# Copyright Justin Warren <justin@eigenmagic.com>

import sys
import os.path
import argparse
import ConfigParser
from itertools import izip_longest

import twitter

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('twitreach')

def get_reach(tw, args):
    """
    Get the marketing 'reach' of a Twitter user.

    The reach is the total count of follower's followers.
    In this simple version, we over-count because we don't exclude
    duplicates.
    """
    username = args.userids[0]
    followers = tw.followers.ids(screen_name=username)
    reach = get_follower_count(tw, followers['ids'])
    print("Reach for @%s: %s" % (username, '{0:,}'.format(reach)))

def get_follower_count(tw, userids):
    """
    Get the count of how many followers a twitter userid has.
    """
    # We need to chunk this into multiple requests,
    # because twitter has a limit of 100 userids per-request.
    reach = 0
    for chunk in chunker(100, userids):
        userid_str = ','.join(['%s' % x for x in chunk if x is not None])
        users = tw.users.lookup(user_id=userid_str)
        for user in users:
            reach += int(user['followers_count'])
            pass
        pass
    return reach

def chunker(n, iterable):
    """
    Return chunks of items of length n from iterable.

    chunker(3, 'abcdef') -> ('a','b','c'), ('d', 'e', 'f')
    """
    return izip_longest(*[iter(iterable)]*n)
    
def authenticate(args):
    """
    Authenticate with Twitter and return an authenticated
    Twitter() object to use for API calls
    """
    # import the config file
    cp = ConfigParser.SafeConfigParser()
    cp.read(os.path.expanduser(args.config))

    token = cp.get('twitter', 'token')
    token_key = cp.get('twitter', 'token_key')
    con_secret = cp.get('twitter', 'con_secret')
    con_secret_key = cp.get('twitter', 'con_secret_key')

    tw = twitter.Twitter(auth=twitter.OAuth(token,
                                            token_key,
                                            con_secret,
                                            con_secret_key))
    return tw
    
if __name__ == '__main__':

    ap = argparse.ArgumentParser(description="Get Twitter Reach",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument('userids', nargs="+", help="Users to find reach for")

    ap.add_argument('-c', '--config', default='~/.twitreach', help="Config file")


    args = ap.parse_args()
    tw = authenticate(args)
    get_reach(tw, args)
