import discord
import time
from discord.voice_client import VoiceClient
from datetime import datetime
token = 'insert token here'

client = discord.Client()
pfp_path = r"C:\Users\Joe\Documents\bot_assets\gibby.jpg"
fp = open(pfp_path, 'rb')
pfp = fp.read()

channelID = 0
currentUser = "hergaderga"
connected = False
connection = ''

@client.event
async def on_ready():
    
    print('We have logged in as {0.user}'.format(client))
    
    #await client.user.edit(avatar=pfp, nick="FatBot") #used for resetting the default look
    
    # !!!SELF NOTE!!! below code needs to be refactored to better find the users targetted.
    
    for guild in client.guilds:
                for channel in guild.voice_channels:
                    if channel.id == 831237328840032316: 
                        channel_to_change = channel
                    if channel.id == 435837024155467776: 
                        second_channel = channel

@client.event
async def on_voice_state_update(member,before,after):   #registers whenever anyone leaves or joins a voice call
    global connected
    if connected == False:                          #check that the bot is not currently in use
        global currentUser
        currentUser = user_check()                  #user_check checks if one of the users in the call is a targetted user
        await changePPAndName(currentUser)

    if after.channel == None:                       #check if a user left or joined
        connected = False                   
        if currentUser is not None:                 #if a user left the channel, check if the user who left is the user that the bot is currently emulating
            if member.id == int(currentUser):
                await connection.disconnect()       #if the user leaving is the user the bot is actively emulating, the bot disconnects as well

def user_check():

    for guild in client.guilds:
        for channel in guild.voice_channels:
            global channelID
            channelID = channel.id
            if channelID == 435837024155467776:                 #!!!SELF NOTE!!! channel identification needs to change (linked to above self note)                      
                for user in list(channel.voice_states.keys()):  #checks to see if one of the targetted users is in the correct call, if so it returns their ID's
                    if user == 289947791999107073:              #!!!SELF NOTE!!! this also needs refactoring into a lift of users
                        return '289947791999107073'
                    elif user == 178475947421335552:
                        return '178475947421335552'
                    elif user == 240563423820120066:
                        return '240563423820120066'

@client.event
async def changePPAndName(userID):                              #!!!SELF NOTE!!! refactorable to remove duplicate code.

    if userID != '776128574318051378':                  #check that the bot is not trying to join on itself
    
        if userID == '289947791999107073':              #check if the ID parsed is a relevant ID to connect with
            for guild in client.guilds:
                for channel in guild.voice_channels:
                    print(channel.id)
                    print("yeeeee     :    " + channelID)
                    if channel.id == channelID:
                        pfp_path = r"C:\Users\Joe\Documents\bot_assets\sean.png"    #find the currently filed profile picture. Must be downloaded manually from the browser version of discord
                        fp = open(pfp_path, 'rb')
                        pfp = fp.read()
                        global connected
                        connected = True
                        await client.user.edit(username = "Casaboo")                #change the bots username
                        await client.user.edit(avatar=pfp)                          #change the bots profile picture
                        global connection
                        connection = await channel.connect()                        #connect to the relevant channel
                        
        elif userID == '178475947421335552':
            for guild in client.guilds:
                for channel in guild.voice_channels:
                    if channel.id == channelID:
                        pfp_path = r"C:\Users\Joe\Documents\bot_assets\joe.jpg"
                        fp = open(pfp_path, 'rb')
                        pfp = fp.read()
                        connected = True
                        await client.user.edit(username = "Gibby")
                        await client.user.edit(avatar=pfp)
                        print("hi")
                        connection = await channel.connect()
                        
        elif userID == '240563423820120066':
            for guild in client.guilds:
                for channel in guild.voice_channels:
                    if channel.id == channelID:
                        pfp_path = r"C:\Users\Joe\Documents\bot_assets\callum.png"
                        fp = open(pfp_path, 'rb')
                        pfp = fp.read()
                        connected = True
                        await client.user.edit(username = "TheMidget5066")
                        await client.user.edit(avatar=pfp)
                        connection = await channel.connect()

    

client.run(token)
