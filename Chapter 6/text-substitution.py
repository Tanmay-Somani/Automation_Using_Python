import keyboard

text_substitutions = {
    "hru": "How are you",
    "hlw": "Hello",
    "PROfile": "my linkedin is https://www.linkedin.com/in/tcode/"
    # Add more substitutions as required by you
}

typed_chars = ""

def expand_text(e):
    global typed_chars

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "space":
            for trigger, replacement in text_substitutions.items():
                if typed_chars.endswith(trigger):
                    typed_chars = typed_chars[:-len(trigger)] + replacement
                    keyboard.write(typed_chars)
                    print(typed_chars)
                    typed_chars = ""
                    break

            if typed_chars:
                keyboard.write(typed_chars)
                typed_chars = ""
        else:
            typed_chars += e.name

# Hooking the keyboard event
keyboard.hook(expand_text)

# Keeping the script running
keyboard.wait("esc")
