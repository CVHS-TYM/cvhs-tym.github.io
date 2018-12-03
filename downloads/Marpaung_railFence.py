#Two-Rail Fence Cypher
#Encryption function by Daniel Kelley (https://www.youtube.com/watch?v=qOlJwi9mu2Q)
#Decryption and command syntax by Timothy Marpaung (cvhs-tym.github.io)
#Online Rail Fence Cypher: http://crypto.interactive-maths.com/rail-fence-cipher.html
#WOAH HIS VERSION OF THE DECYPHER IS SO MUCH CLEANER WHAT

#Here's some notes on the program, unnecessary but I think they add to it.
#This function is pretty much identical to the tutorial
def Scramble2Text(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0

    for ch in plainText:
        if charCount%2 is 0:
            evenChars += ch
        else:
            oddChars += ch
        charCount += 1
    cipherText = evenChars+oddChars
    return(cipherText)

#This just reverses the steps
def decryptMessage(cipherText):
    evenChars = ""
    oddChars = ""
    decryptedMessage = ""
    charCount = 0

    #Here, we split the input into two parts:
    #The first half is even, and the second half is odd.
    #We can be absolutely sure about this splitting due to how the encryption works (for two-rail that is).
    for ch in cipherText:
        if charCount < len(cipherText)*0.5:
            evenChars += ch
        else:
            oddChars += ch
        charCount += 1
    #We re-use the character count accumulator variable here.
    charCount = 0
    for ch in cipherText: #We use this simple iterator to go through each character, possibly can be simplified
        if charCount < len(evenChars): #We have to use this here, otherwise the program will break (out of range).
            decryptedMessage += evenChars[charCount]
        if charCount < len(oddChars):
            decryptedMessage += oddChars[charCount]
        charCount += 1
    return(decryptedMessage)

#This is specifically used for the "clear" command.
bunchofnewlines = ''
for i in range(50):bunchofnewlines+='\n' #We can use a single line since its so simple. Bad practice? I've seen it around

#We use these for our variable 'help' command that has an input
et = ('e','enc','encrypt')
dt = ('d','dec','decrypt')
ct = ('clr','clear')
print('Encrypt or Decrypt. Do \'help\' for info.')
#msg = "placeholder"
while True:
    cmd = input('command: ')
    if cmd[:8].lower() == "encrypt ":
        msg = Scramble2Text(cmd[8:])
    elif cmd[:4].lower() == "enc ":
        msg = Scramble2Text(cmd[4:])
    elif cmd[:2].lower() == "e ":
        msg = Scramble2Text(cmd[2:])

    elif cmd[:8].lower() == "decrypt ":
        msg = decryptMessage(cmd[8:])
    elif cmd[:4].lower() == "dec ":
        msg = decryptMessage(cmd[4:])
    elif cmd[:2].lower() == "d ":
        msg = decryptMessage(cmd[2:])

    elif cmd[:4].lower() == "help":
        if cmd[5:].lower() in et:
            msg = "[e/enc/encrypt TEXT]: Encrypts the plaintext message with a two-rail cypher."
        elif cmd[5:].lower() in dt:
            msg = "[d/dec/decrypt TEXT]: Decrypts the plaintext cipher-text with a two-rail cypher decryption"
        elif cmd[5:].lower() in ct:
            msg = "[clr/clear]: Pseudo clears the shell with newline spam"
        elif cmd[5:].lower() == "help":
            msg = "[help/help CMD] Returns the commands, or shows info about a command."

        else: #Probably a better way for this specific statement but "it just works"
            msg = "e/enc/encrypt | d/dec/decrypt | clr/clear"

    elif cmd.lower() in ct:
        msg = bunchofnewlines
    else:
        msg = "Unknown Command."
    print(str(msg)+"\n")

#The reason why I used multiple 'if statements' for the encrypt and decrypt rather than 'in' statements is because
    #I didn't know how to do it in a single line, which would be simple.
#Take for example, the variables for help.
    #I can just easily do "if [the rest of the command after help] [is in] [this list]" then do this single thing
#However, that runs into a problem because the commands are set up specifically that:
    #Each one checks for a certain length, and the result inputs the rest of it into the corresponding command
    #If I did:
        #if cmd in ('e','enc','encrypt':
    #I would have no way of properly checking for the rest of the command to use as an input
    #An even worse way would be,
        #if cmd in ('e','enc',encrypt':
            #Scramble2Text(cmd[#:])
    #as it would be arbitrary(?) and not really work.
    #There's probably a way around it, like having the command have equal lengths but aliases should be allowed to
    #be shorter.
