// Object containing all guides and troubleshooting steps for different devices
export const allGuides = {
    "mobile": {
        "type": "Mobile devices",
        "icon": "fa-solid fa-mobile-screen",
        "guide": [
            {
                "title": "Connect to Wi-Fi",
                "items": ["Open the Settings app.", "Tap Wi-Fi",
                    "Make sure the Wi-Fi is turned on.",
                    "You should see a list of available networks. Tap the one you want to join.",
                    "Enter the password if asked, and then hit Connect."
                ]
            },
            {
                "title": "Change screen brightness",
                "items": ["Swipe down from the top of your screen.",
                    "You should see a little brightness slider - move it left or right to make your screen darker or brighter.",
                    "Or, you can go to <strong>Settings</strong> > <strong>Display</strong> and adjust it there.",
                ]
            },
            {
                "title": "Set an alarm",
                "items": ["Open the <strong>Clock</strong> app.",
                    "Tap the <strong>Alarm</strong> tab.",
                    "Tap the <strong>+</strong> icon to add a new alarm.",
                    "Set the time and any other preferences, then tap <strong>Save</strong>."
                ]
            },

        ],
        "troubleshoot": [
            {
                "title": "Sound not working",
                "items": ["Check the volume settings to ensure it's turned up.",
                    "Test with a different app to rule out the possibility of app-related issues.",
                    "If you are using headphones, make sure they are plugged in properly.",
                    "If the issue persists, try restarting your phone or resetting sound settings."
                ]
            },
            {
                "title": "Bluetooth not connecting",
                "items": ["Make sure Bluetooth is turned on in your <strong>Settings</strong>.",
                    "Ensure the device you are connecting to is also in a pairing mode or discoverable.",
                    "Try 'forgetting' the device in your Bluetooth settings and reconnecting.",
                    "If the issue persists, restart both devices and try again."
                ]
            },
            {
                "title": "Mobile App not working properly",
                "items": ["First, try closing and restarting the app.",
                    "If that doesn't help, check for updates for the app in the app store.",
                    "If it is still not working, try restarting your phone.",
                    "As a last resort, clear the app's cache or reinstall it."
                ]
            },
        ]
    },
    "computer": {
        "type": "Desktop/Laptop",
        "icon": "fa-solid fa-computer",
        "guide": [
            {
                "title": "Launch an Application",
                "items": [
                    "On Windows: Click the 'Start' button (the Windows icon) in the bottom-left corner of your screen.",
                    " Then, type the name of the application you want to open into the search box.",
                    "When the app appears in the search results, click on it to open.",
                    "On Mac: Click on the 'Finder' (the smiling face icon) in the dock at the bottom of your screen.",
                    "Then, click on the 'Applications' folder in the left sidebar.",
                    "Find the application you want to open, and double-click on it to launch.",
                ]
            },
            {
                "title": "Adjust screen resolution",
                "items": ["Right-click on the desktop and select 'Display Settings' (Windows) or 'System Preferences' > 'Displays' (macOS).",
                    "Under 'Display Resolution', select your preferred resolution from the dropdown list.",
                    "Click 'Apply' to make the change, then 'Keep Changes' if satisfied."
                ]
            },
            {
                "title": "Change desktop wallpaper",
                "items": [
                    "Right-click on the desktop and select 'Personalize' (Windows) or 'Change Desktop Background' (macOS).",
                    "Select an image or click 'Browse' to choose a custom picture.",
                    "Click 'Apply' (Windows) or 'Set Desktop Picture' (macOS) to apply the wallpaper."
                ]
            },

        ],
        "troubleshoot": [
            {
                "title": "Sound not working",
                "items": [
                    "Make sure your computer volume is turned up. You can find the volume icon at the bottom-right corner of the screen (Windows) or top-right (Mac).",
                    "Check if your speakers or headphones are properly connected to the computer.",
                    "Make sure the correct speaker is selected. You can do this in the sound settings.",
                    "If the sound still does not work, restarting your computer to might fix the problem."
                ]
            },
            {
                "title": "System running slowly",
                "items": [
                    "Close any programs or windows you are not using. You can click the 'X' in the corner to close them.",
                    "Try restarting your computer. It can help clear up any problems.",
                    "Check if your computer needs any updates.",
                ]
            },
            {
                "title": "Run system updates",
                "items": [
                    "On Windows: Click on the 'Start' button, then go to 'Settings' > 'Update & Security' > 'Windows Update' and click 'Check for Updates'.",
                    "On Mac: Click on the Apple menu at the top-left corner, then select 'System Preferences' > 'Software Update' and click 'Update Now'.",
                    "After the update, restart your computer to apply the changes.",
                    "It is a good idea to check for updates regularly to keep your computer running smoothly."                    
                ]
            },
        ]
    },    
};