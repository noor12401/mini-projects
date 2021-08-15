# Simple Encryption and Decryption

### Description
This program will encrypt and decrypt files using a simple replacing techniques. The programs take a input and split it into a single elements in a list then replace it with two different element and return the text as an encrypted format. The decryption process is just the reverse of the encryption process. It replaces the two element with the appropriate alphabet to decrypt the original text.

### File Breakdown
This project contain three files.
1. Encrypter: It takes the single alphabet and return two random string.
2. Decrypter: It takes the two random string and return the appropriate text.
3. Main: It is the main file that takes the user input, split it into single letters then perform encryption and decryption

### How To Use?
Down all the three files and run the main. OR
1. Download all the three files and put it under single folder.
2. Open cmd or powershell in windows and change your directory to that folder
3. Run `python main.py` on the cmd

### How To Upgrade?
You can upgrade this project by replacing a single origanl text to three or more random text. This will make harder for the user to guess the code. You can even add a password layer which return the text only after user provides the correct password.

### Limitation
Since this works on public cryptography, any user can type a sigle alphabet and get the encrypted text. The user can then type every single letter and can note down the pattern.
