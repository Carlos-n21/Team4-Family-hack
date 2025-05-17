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
    }
};