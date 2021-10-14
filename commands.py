commands = [ "move piece at location to location", "undo that move", "start the game"
]

commandDictionary  = {}


#function to call when the game is chosen
# takes a list of valid commands for that game and makes a dictionary with each word used in all of the commands
def makeDictionary(commands):
    for command in commands:
        words = command.split()
        for word in words:
            commandDictionary[word] = 1


#function to be called after recieving speech to text data from api
# runs through the returned message and removes all words that arnt used for any of the valid commands for that game
def parseCommand(voiceMessage):
    words = voiceMessage.split()
    validWords = ""
    for word in words:
        if word in commandDictionary:
            validWords += word
            validWords += " "
    return validWords


