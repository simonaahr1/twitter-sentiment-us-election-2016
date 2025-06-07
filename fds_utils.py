from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from multiprocessing import  Pool
import re
import string

def get_data(name, tweets):
    '''
    Returns a subset of information with description 'name' 
    out of tweets.
    
    For dealing with nested jsons pass 'name' as a list, 
    indicating the description at each layer, e. g. 
    ['place', 'country'] for tweet['place']['country'].
    '''
    if type(name) is str:
        data = list(map(lambda tweet: tweet[name], tweets))
    elif type(name) is list:
        data = list(map(lambda tweet: tweet[name[0]][name[1]] if tweet['place'] != None else None, tweets))
    else:
        raise ValueError("Parameter name must be a string or list.")
    return data

def normalize(tweet_tokens):
    '''
    Taken from the digitalocean tutorial.
    
    This function first gets the position tag of each token of a tweet. If the tag starts with
    NN, the token is assigned as a noun. Similarly, if the tag starts with VB, the token is assigned as a verb.
    
    Hyperlinks and stop words (the, a, is, ...) are also removed.
    
    '''
    cleaned_tokens = []
    stop_words = stopwords.words('english')

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        # Keep username mentions
        # token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def transform_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)
