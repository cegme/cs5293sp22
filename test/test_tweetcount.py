import tweetcounter

def test_tweetsfile():
    filename = "resources/tweets.json"
    
    thecount = tweetcounter.counttweets(filename)
    assert thecount ==  10972
