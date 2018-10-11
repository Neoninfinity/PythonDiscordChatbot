#Imports all neccessary libraries
import discord #The discord api wrapper for python https://github.com/Rapptz/discord.py 
import asyncio # Python3.4 library multiplexing over sockets and waiting for co-routines to finish. Doing this can requerst data from multiple servers and act only when needed
import sys 
from function_Hello import hello,reponseToHowAreYou,goodbye,random,responses
from keywords import key
from GoogleSearch import gsearch #Library from google API https://github.com/google/google-api-python-client
from picturesearch import place # Google place library
from Nutrition import *
keywords = key
# defines the client
client = discord.Client()




"""This coroutine waits until the client is all ready then prints to console"""
@client.event
async def on_ready():#Ready from the discord Library
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    
    
# Functions that could compose of a library
def is_number(s):
    """Takes in a string and checks to see if its a valid integer"""
    if s.isdigit() == True: # isdigit is a function from the standard library
        return True
    else:
        return False
    
def messageSend(string,channel):
    tmp = await(client.send_message(channel, string))

def CreateServer(server_Name,Key,add):
    fileName = server_Name + ".py"
    f = open(fileName,"w")
    f.write("import discord\n\
             import asyncio \n\
             import sys\n"
             "client.run("+Key+")\n"
             )
    if add == "search":
        f.write("from diserv import googlesearch\n\
        use googlesearch() to search google")
    elif add == "places":
         f.write("from diserv import closestPlace\n\
        use closestPlace(place,x) to find the closest place from x")
            
    f.close()
        
    
    
#Functions are put in here

"""Takes in a message and removes commands then searches query with results of n"""
def googlesearch(message,value):
    print("Message is ",message.content)
    #phrase = (message.content).replace('!gsearch', '')
    wordlist = message.content.split()
    try:
        wordlist.remove("!gsearch")
    
    except ValueError:
        index =  wordlist.index(value)
        wordlist = wordlist[index:] #
        wordlist.remove(value)
        print("word list is ", wordlist)
        
    phrase = ""
    intv = 1
    if not wordlist:
        OUTPUT = "Oops something didn't go right\nTo google search format like this: '!gsearch [term] [value]'"
        return OUTPUT
    for x in wordlist:
        if is_number(x) == False:
            phrase = str(phrase) +str(x)+(" ")
            continue
        else:
            intv = int(x)
            break
        
    listneeded = gsearch(phrase,intv)
    OUTPUT = ""
    for x in listneeded:
        OUTPUT = OUTPUT + x +"\n"
    return OUTPUT       
   
def closestPlace(message,value):
    print("Message is ",message.content)
    #phrase = (message.content).replace('!gsearch', '')
    wordlist = message.content.split()
    try:
        wordlist.remove("!psearch")
    
    except ValueError:
        index =  wordlist.index("from")
        wordlist = wordlist[index-1:]
        print("word list", wordlist)
        
    intv = 1
    if not wordlist:
        OUTPUT = "Oops something didn't go right\nTo place search format like this: '!psearch [current location] [destination]'"
        return OUTPUT

    listneeded = place(wordlist[2],wordlist[0])
    OUTPUT = ""
    for x in listneeded:
        OUTPUT = OUTPUT + str(x) +"\n"
    return OUTPUT
    
"""Triggered when message recieved from client"""
@client.event
async def on_message(message):
    #####################################
    
    ##### Test Function from discord library
    if message.content.startswith('!test'): # checks if a message starts with a specific string
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    ####function end 
    elif message.author.id == ("375255240326250496"): # This is the ID of the bot
        return 0
    elif message.content.startswith('!gsearch'): ## if starts with !gsearch
        OUTPUT = googlesearch(message,"")
        tmp = await client.send_message(message.channel, OUTPUT)
        return 0
    elif message.content.startswith('!adminshutdown'):
        tmp = await client.send_message(message.channel, "Shutting down, Goodbye!")
        sys.exit()
        
    elif message.content.startswith('!stweet'):#function not implemented
        OUTPUT = TwitSearch()
        tmp = await client.send_message(message.channel, OUTPUT)
        return 0
        
    elif message.content.startswith('!introduce'):
        await client.send_message(message.channel, "Hi I'm Nirvana a handy assistant\nI'm going to be the best bot around!!")
        return 0
    elif message.content.startswith('!calorie'):
        msg = (message.content).replace('!calorie', '')
        OUTPUT = Calorie(msg)
        msg1 = "You have consumed " + str(OUTPUT[0]) +" calories"+ "\nwhich is " + str(OUTPUT[1]) +"% of your daily allowance!"
        await client.send_message(message.channel, msg1)
        return 0
    elif message.content.startswith('!fat'):
        msg = (message.content).replace('!fat', '')
        OUTPUT = Fat(msg)
        await client.send_message(message.channel, OUTPUT)
        return 0
    elif message.content.startswith('!sugar'):
        msg = (message.content).replace('!sugar', '')
        OUTPUT = Sugar(msg)
        await client.send_message(message.channel, OUTPUT)
        return 0
    else:
        print("No response for select input")
    
    #########################################MAIN NIRVANA CODE#######################################################################
    sentence = message.content
    sentence = sentence.lower()
    brokenString = sentence.split(" ")
    #print(("author is",type(message.author.id),message.content))
    if (len(set(brokenString).intersection(keywords))) > 0 or sentence in keywords.keys():
        ## Keyword checking goes here (if statements)
        funcLoad = 0
        newstring = sentence
        for x in brokenString:
            if x in keywords.keys():
                keyword = x
                newstring = newstring.replace(keyword,"")
                print(x,newstring)
                funcLoad = keywords[x]
            elif sentence in keywords.keys():
                funcLoad = keywords[sentence]
                break
            else:
                print("")
                
        has_key = lambda a, d: any(k in a for k in d) # https://stackoverflow.com/questions/32096654/python-check-if-string-contains-dictionary-key
        newbrok = newstring.split()
        if has_key(newstring,keywords) == True:
            print("loaded")
            for key in keywords:
                if key in newstring and len(key) > 3:
                    print(key)
                    funcLoad= keywords[key]
                 

        print("funcload is ", funcLoad)

        #Depending on the keyword the different number function will be loaded 
        #The numbers are listed in the keywords.py
        
        if funcLoad == 1:
            OUTPUT = hello(sentence)
            tmp = await client.send_message(message.channel, OUTPUT)
        elif funcLoad == 2:
            print("placeholder")
        elif funcLoad == 3:
            tmp = await client.send_message(message.channel, "No problem, heres what i've found:\n")
            OUTPUT = googlesearch(message,keyword)
            tmp = await client.send_message(message.channel, OUTPUT)
        elif funcLoad == 4:
            tmp = await client.send_message(message.channel, "Heres the closest place I have found:\n")
            OUTPUT = closestPlace(message,keyword)
            tmp = await client.send_message(message.channel, OUTPUT)
        elif funcLoad == 5: 
            OUTPUT = reponseToHowAreYou(sentence)
            tmp = await client.send_message(message.channel, OUTPUT) # 
        elif funcLoad == 6: 
            OUTPUT = goodbye(sentence)
            tmp = await client.send_message(message.channel, OUTPUT)
        elif funcLoad == 7: 
            OUTPUT = random(sentence)
            tmp = await client.send_message(message.channel, OUTPUT)
        elif funcLoad == 8: 
            OUTPUT = responses(sentence)
            tmp = await client.send_message(message.channel, OUTPUT)
        else:
            print("Function not found")
            
    else:  
        tmp = await client.send_message(message.channel, "Sorry, I couldn't understand you")

client.run('Mzc1MjU1MjQwMzI2MjUwNDk2.DO23Qg.TAlBUyCq5MyE7UMH4hSLZz1WP-E')
