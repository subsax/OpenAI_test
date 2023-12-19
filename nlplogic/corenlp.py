from textblob import TextBlob
import wikipedia 


#write a function to create the search for wikipedia

def search_wiki(name):
    print(f"seraching the name:{name}")
    return wikipedia.search(name)


#To summarize the wikipedia

def summarize_wiki(name):
    print(f"summarize the name:{name}")
    return wikipedia.summarize(name)

#getting the text blob
def get_the_text_blob(text):
    print(f"the text blob object")
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """find wikipedia name and get the phrases"""
    text = summarize_wiki(name)
    text_blob=get_the_text_blob(text)
    phrases=blob.noun_phrases
    return phrases


    




