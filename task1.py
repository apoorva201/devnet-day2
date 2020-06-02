import requests
import json
url = "https://deckofcardsapi.com/api/deck/"	#### this is the base url
resp=requests.get(url+"new/")                                ### this should not return any errors,
						##### note we append “new/”to make a new deck  
print(resp)                                                       #### this should show a 200
print(resp.text)				##### this should show the response body, you see the deck id, 

#### we need to get the deck id so we can do things. It is in text, we need it in json.
deck=json.loads(resp.text)
decknumber=deck["deck_id"]
print(decknumber)

draw2url=url+decknumber+"/draw/?count=2"
print(draw2url)                                            ####### I keep doing this a debug. 
cards=requests.get(draw2url)		############ get   2 cards from deck
print(cards)				######## print it, its in text
jsoncards=json.loads(cards.text)		######## load it into json
print(json.dumps(jsoncards, indent=2))   ###### print it pretty like

