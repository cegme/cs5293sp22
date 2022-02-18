import tweetcounter

import pytest

@pytest.fixture()
def twfilename():
    return "resources/tweets.json"


def test_tweetsfile(twfilename):
    
    thecount = tweetcounter.counttweets(twfilename)
    assert thecount ==  10972

@pytest.mark.parametrize("terms,total", [('Vomit',702), ('vomit',8523)])
def test_search(terms,total, twfilename):
    tweets = tweetcounter.searchterms(twfilename, terms)
    assert tweets is not None
    assert len(tweets) > 0
    assert len(tweets) == total



