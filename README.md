
# Mouse Autoclicker for AFK World in Type Soul

## Overview

This project is a Python-based mouse autoclicker designed to help players in **AFK World in Type Soul** keep four accounts active simultaneously. The script clicks the center of the four corners of your screen in an alternating sequence to ensure your accounts remain active. The GUI allows for easy control, with customizable start/stop hotkeys and a clear status indicator.

## Features

- **Customizable Hotkeys:** Set your preferred key or key combination to start/stop the autoclicker.
- **GUI Control:** Easy-to-use GUI with a start/stop button and status indicator.
- **Corner Clicking:** The script clicks four times in each of the four corners of the screen to keep your accounts active.
- **Background Operation:** Runs in the background, allowing you to minimize the GUI or continue other tasks.

## Why This Project Was Created

In **AFK World in Type Soul**, keeping multiple accounts active is essential for maintaining progress. This autoclicker was created to automate the process of keeping four accounts active simultaneously, allowing users to focus on other tasks while ensuring they don't get removed for inactivity.

## Requirements

- Python 3.x
- `pyautogui` library
- `keyboard` library
- `tkinter` (included with Python)

You can install the necessary Python libraries using pip:

```bash
pip install pyautogui keyboard
```

## Installation and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AD-Archer/TypeSoul-autoclicker.git
   cd TypeSoul-autoclicker
   ```

2. **Install Dependencies:**

   Open your command prompt or terminal and run the following command:

   ```bash
   pip install pyautogui keyboard
   ```

3. **Run the Script:**

   You can run the script directly from your file browser. Just double-click the script file (`autoclicker.py`), and the GUI will open.

4. **Using the Autoclicker:**

   - **Set Hotkey:** Enter your desired start/stop hotkey in the input field (e.g., `ctrl+shift+a`) and click "Apply Hotkey."
   - **Start/Stop:** Click the "Start/Stop" button or use your custom hotkey to toggle the autoclicker.
   - The status indicator will show "Running" in green when the autoclicker is active and "Stopped" in red when it's inactive.

## Notes

- The script is designed to run on Windows, and it requires that the four corners of your screen are visible and unobstructed by other windows.
- Ensure your Python installation includes `tkinter`, which is typically included by default.

## License

This project is open-source and available.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Acknowledgements

Thanks to the Python community and the developers of `pyautogui` and `keyboard` for providing the tools to make this project possible.
