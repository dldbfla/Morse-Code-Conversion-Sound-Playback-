import tkinter as tk
from tkinter import scrolledtext, filedialog
from pydub import AudioSegment
from pydub.generators import Sine

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def text_to_morse_code(text):
    morse_code = ''
    for letter in text.upper():
        if letter in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[letter] + ' '
        elif letter == ' ':
            morse_code += '  ' # Add spaces to separate words
        else:
            morse_code += ''  # Ignore unconvertible characters
    return morse_code

def morse_code_to_audio(morse_code, dot_length=100):
    audio_sequence = AudioSegment.empty()
    dot_sound = Sine(1000).to_audio_segment(duration=dot_length)
    dash_sound = Sine(1000).to_audio_segment(duration=dot_length * 3)
    space_sound = AudioSegment.silent(duration=dot_length)

    for char in morse_code:
        if char == '.':
            audio_sequence += dot_sound
        elif char == '-':
            audio_sequence += dash_sound
        else:  # Space between characters or words
            audio_sequence += space_sound

    return audio_sequence

def create_gui():
    window = tk.Tk()
    window.title("Morse code converter")

    tk.Label(window, text="Enter text:").grid(column=0, row=0, padx=10, pady=10)
    text_input = tk.Entry(window, width=50)
    text_input.grid(column=1, row=0, padx=10, pady=10)

    tk.Label(window, text="Morse code:").grid(column=0, row=1, padx=10, pady=10)
    morse_display = scrolledtext.ScrolledText(window, width=38, height=10)
    morse_display.grid(column=1, row=1, padx=10, pady=10)

    def convert_to_morse():
        text = text_input.get()
        morse_code = text_to_morse_code(text)
        morse_display.delete('1.0', tk.END)
        morse_display.insert(tk.INSERT, morse_code)

    def export_audio():
        morse_code = morse_display.get('1.0', tk.END).strip()
        if morse_code:
            audio_sequence = morse_code_to_audio(morse_code)
            file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
            if file_path:
                audio_sequence.export(file_path, format="mp3")
                tk.messagebox.showinfo("Done", "Your audio file has been saved.")

    convert_button = tk.Button(window, text="Morse code conversion", command=convert_to_morse)
    convert_button.grid(column=1, row=2, padx=10, pady=10)

    export_button = tk.Button(window, text="Export to audio", command=export_audio)
    export_button.grid(column=1, row=3, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
