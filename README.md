# Morse-Code-Conversion-Sound-Playback-
Morse code conversion/sound playback (save as mp3) 

## Description. 

This code uses tkinter to generate a GUI, convert input text to Morse code, and export the code to an audio file.

First, the text_to_morse_code function converts the input text to uppercase and then converts each character to Morse code. It uses a dictionary called MORSE_CODE_DICT to find the Morse code for each character, and returns the converted Morse code, separated by spaces.

The morse_code_to_audio function takes a Morse code as input, generates a sound based on that code, and returns a concatenated audio sequence. The dot_length parameter specifies the length of the dot (.), which defaults to 100. It generates sounds corresponding to dots and dashes (-), and silences spaces between letters or words.

The create_gui function creates a GUI window using tkinter, and creates a text input box and a Morse code display window. When the user enters text and clicks the "Morse code conversion" button, the convert_to_morse function is called to convert the text to Morse code and output the converted code to the Morse code display window. Also, when the user clicks the "Export to audio" button, the export_audio function is called to export the Morse code to an audio file.

Each function uses various widgets and functions from tkinter to perform GUI operations.

To run this code, use the following code: if __name__ == "__main__": You can call the create_gui() function below.




## install 

Installing tkinter:
Windows: It is usually installed by default with Python, so no separate installation is required.
macOS: Typically installed by default with Python, so no separate installation is required.
Linux: You can install it using the sudo apt-get install python3-tk command.
Install pydub and pydub.generators:
Open a command prompt or terminal and run the following command to install them
````
pip install pydub
`````
This code is written for the purpose of generating a GUI that converts user-entered text to Morse code, converts Morse code to audio, and exports it.

## Caveats 

A few notes about the code

You must have the tkinter and pydub libraries installed.
You need to add if __name__ == "__main__": before running the code.
The GUI window must be created by calling the create_gui() function.
The text_to_morse_code function, which converts the input text to morse code, and the morse_code_to_audio function, which converts morse code to audio, are already defined and do not require further implementation.
Before exporting an audio file in the export_audio() function, you must select the file path using tkinter's filedialog.
During the process of converting Morse code to audio, you can adjust the length of the sound, which is currently set to dot_length in the code. You can adjust this value as needed.
