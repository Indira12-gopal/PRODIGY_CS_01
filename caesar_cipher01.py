def caesar_cipher(text,shift,mode):
    result =""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base=ord('A')
            else:
                base=ord('a')
            result+=chr(base + (ord(char) - base + shift)%26)
        else:
            result+=char
    return result
end=False
while not end:
    print("CAESAR CIPHER PROGRAM")
    mode= input("ENCRYPT OR DECRYPT:").upper()
    shift=int(input("Enter shift value:"))
    text=input("Enter text:")
    if mode=='ENCRYPT':
        print("Encrypted Text:",caesar_cipher(text,shift,'ECRYPT'))
    elif mode=='DECRYPT':
        print("Decrypted Text:",caesar_cipher(text,-shift,'DECRYPT'))
    else:
        print("invalid input!")
    play_again=input("Type 'yes' to continue 'no' to exit:")
    if play_again=='no':
        end=True

            
    
