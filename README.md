# twitreach

## Description

twitreach is a quick Python hack to figure out the marketing concept of 
'reach' for a given user. Reach is loosely defined at the audience that 
might see any of your tweets, and is more than your direct followers, it 
also includes your followers' followers.

twitreach calculates how many people follow your followers in total, and
prints out that number.

## Requirements
twitreach requires at least Python 2.7, and the twitter API library.

Install the library from PyPI with pip

```
sudo pip install twitter
```
or your distribution's package manager, e.g., for Ubuntu:

```
apt-get install python-twitter
```

## Usage

```
twitreach.py [-h] [-c CONFIG] userids [userids ...]
```

twitreach requires a configuration file, which contains application OAuth
information so you can access the Twitter API. To set this up, go to the
Twitter apps console https://apps.twitter.com and sign in with your Twitter
ID. Follow the Twitter documentation for creating an app and getting the
application keys.

Populate a config file. twitreach looks for one in your home directory
called .twitreach, or use the -c command line flag to point at another one.
An example file with the syntax is included as twitreach.conf.example.

## Known Limitations
This is a quick hack, so it's wrong in several ways.

Firstly, it's going to overcount, because it doesn't remove duplicates. If
someone follows several of your followers, they'll be counted every time.
This will artificially inflate your 'reach' number.

## License

twitreach is released under the MIT license. For more information,
check out the LICENSE file.



