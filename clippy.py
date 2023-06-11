import tkinter as tk
import pyperclip
import threading
import time

# Create a Tkinter window
window = tk.Tk()
window.title("Clippy")
window.geometry("400x400")


# Function to update the clipboard history
def update_history():
    # Create a list to store clipboard history
    clipboard_history = []
    while True:
        # Get the current clipboard content
        current_clipboard = pyperclip.paste()

        if current_clipboard in clipboard_history:
            if current_clipboard == clipboard_history[-1]:
                continue
            clipboard_history.remove(current_clipboard)

        # Add the current clipboard content to the history
        clipboard_history.append(current_clipboard)

        # Limit the history to 10 items
        if len(clipboard_history) > 10:
            clipboard_history.pop(0)

        # Clear the previous history displayed in the text area
        text_area.delete(1.0, tk.END)

        # Update the text area with the updated clipboard history
        for item in clipboard_history[::-1]:
            text_area.insert(tk.END, item + "\n"*2)
        time.sleep(1)


# Function to handle manual copying of text
def manual_copy():
    # Get the selected text in the text area
    selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)

    # Clear the selection in the text area
    text_area.tag_remove(tk.SEL, "1.0", tk.END)

    # Update the clipboard with the selected text
    pyperclip.copy(selected_text)


# Create a button to manually copy selected text
copy_button = tk.Button(window, text="Copy Selected", command=manual_copy)
copy_button.pack()

# Create a text area to display the clipboard history
text_area = tk.Text(window, height=10, width=50)
text_area.config(state=tk.NORMAL)
text_area.pack()

clipboard_thread = threading.Thread(target=update_history)
clipboard_thread.daemon = True
# Start the clipboard update loop
clipboard_thread.start()

# Run the Tkinter event loop
window.mainloop()
