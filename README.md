# MIDS-SARD-Project
W205 Project

## Setup

    sudo pip install -r depends.txt

## Use

    ./twitter-stream-track.py <keywords file> <directory to store twitter logs in>/

## Token File

Store your twitter credentials in a file located ~/.twitterapi/sard.yml in yaml format.

    consumer_key: notrealslkdjf324hd8
    consumer_secret: thesearentrealalkjdsflaksjdf348ofjwsdlkAA2gallyourkeyarebelongtous
    access_token:  thesearentrealWYxOAuwA7v
    access_secret: notanactualkeyll8qAS6B84Ghbecausethatwouldbedumb

## Keywords file

Keywords file must be one keyword per line. Up to 400 keywords can be tracked by a single
streaming application connection.
