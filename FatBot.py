import discord
from discord.voice_client import VoiceClient

token = 'insert your token here'                            #input your discord developer token

client = discord.Client()
pfp_path = r"your default picture path"
fp = open(pfp_path,'rb')
pfp = fp.read()

userIDList = []                                             #input the user ID's you want to target
channelIDList = []                                          #input the channel ID's you want fatbot to be active in

channelID = 0
currentUser = 'temp'
connected = False
connection = ''

@client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(client))

    #await client.user.edit(avatar=pfp, nick="FatBot") #used for resetting the default look


@client.event
async def on_voice_state_update(member,before,after):   #registers whenever anyone leaves or joins a voice call
    oldUser = currentUser
    global connected
    if connected == False:                          #check that the bot is not currently in use
        global currentUser
        currentUser = user_check()                  #user_check checks if one of the users in the call is a targetted user
        if currentUser != oldUser:                  #check if the user currently being used is being requested again, if so, don't update the profile picture and name. This prevents discord throttling
            await changePPAndName(currentUser)


    if after.channel == None:                       #check if a user left or joined
        connected = False                   
        if currentUser is not None:                 #if a user left the channel, check if the user who left is the user that the bot is currently emulating
            if member.id == int(currentUser):
                await connection.disconnect()       #if the user leaving is the user the bot is actively emulating, the bot disconnects as well



def user_check():
    
    for guild in client.guilds:
        for channel in guild.voice_channels:
            if channel.id in channelIDList:
                global channelID
                channelID = channel.id
                for user in list(channel.voice_states.keys()):
                    if user in userIDList:
                        global currentUser
                        currentUser = user
                        return user                 #only need the first match as only need 1 person at a time

@client.event
async def changePPAndName(userID):

    if userID != '776128574318051378':              #check that the bot isnt trying to duplicate itself 


        for guild in client.guilds:                 #ensure that it is the correct channel 
            for channel in guild.voice_channels:
                if channel.id == channelID:
                    if currentUser == first client:
                        pfp_path = r"the required path for the picture"             #input the path of the picture for the required profile picture update
                        fp = open(pfp_path, 'rb')
                        pfp = fp.read()
                        connected = True
                        await client.user.edit(username = "clients username")       #input the clients username
                        await client.user.edit(avatar=pfp)
                        connection = await channel.connect()
                    elif currentUser == second client:
                        print("yeee")
                        pfp_path = r"C:\Users\Joe\Documents\bot_assets\sean.png"    
                        fp = open(pfp_path, 'rb')
                        pfp = fp.read()
                        connected = True
                        await client.user.edit(username = "clients username")                   #change the bots username
                        await client.user.edit(avatar=pfp)                                      #change the bots profile picture
                        connection = await channel.connect()                                    #connect to the relevant channel

                        
                    

client.run(token)
