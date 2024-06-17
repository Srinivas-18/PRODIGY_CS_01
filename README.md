This code is a graphical user interface (GUI) implementation of a Caesar Cipher, a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down the alphabet. The GUI is built using the Tkinter library in Python. 

--Class CaesarCipher--
This class represents the Caesar Cipher algorithm. It has two methods: encrypt and decrypt.

The __init__ method initializes the cipher with a shift value, which determines how many positions each letter in the plaintext should be shifted.
The encrypt method takes a message as input and returns the encrypted message. It iterates over each character in the message, and if the character is a letter, it shifts it by the specified amount using the ASCII values of the characters.
The decrypt method is similar to the encrypt method, but it shifts the characters in the opposite direction to decrypt the message.

--Class GUI--
This class represents the graphical user interface of the Caesar Cipher application. It has several methods:

The __init__ method initializes the GUI components, such as labels, text entries, and buttons.
The encrypt method is called when the "Encrypt" button is clicked. It retrieves the message and shift value from the GUI, creates a CaesarCipher object, encrypts the message, and displays the result in the GUI.
The decrypt method is similar to the encrypt method, but it decrypts the message instead.

--Main Application--
The main application creates a Tkinter window and an instance of the GUI class. It then starts the GUI event loop using "root.mainloop()"

-------How to Use-------
To use this application, follow these steps:

1.Run the code to launch the GUI.
2.Enter a message in the "Enter a message:" text box.
3.Enter a shift value in the "Enter a shift value:" text box.
4.Click the "Encrypt" button to encrypt the message.
5.The encrypted message will be displayed in the "Result:" text box.
6.To decrypt the message, click the "Decrypt" button.

Note that this implementation only works with alphabetic characters and preserves the case of the original message. Non-alphabetic characters, such as spaces and punctuation, are left unchanged.
