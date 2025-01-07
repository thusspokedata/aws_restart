def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

print(getDoubleAlphabet("abc"))  # abcabc

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = int(input("Please enter a key (whole number from 1-25): "))  # Convert to int
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # Convert the message to uppercase
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)  # Find the index of the current character in the alphabet
        if currentCharacter in alphabet:
            newPosition = (position + cipherKey) % len(alphabet)  # Shift the position with wrap-around
            encryptedMessage += alphabet[newPosition]  # Append the new character
        else:
            encryptedMessage += currentCharacter  # Append non-alphabetic characters as-is
    return encryptedMessage

# Test the function
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
doubleAlphabet = getDoubleAlphabet(alphabet)
message = "Hello World!"
cipherKey = 3  # Example key
encrypted = encryptMessage(message, cipherKey, doubleAlphabet)
print(f"Encrypted message: {encrypted}")

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * cipherKey  # No need to convert cipherKey here since it's already an int
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(f'Message: {myMessage}')
    myCipherKey = getCipherKey()
    print(f'Cipher Key: {myCipherKey}')
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()