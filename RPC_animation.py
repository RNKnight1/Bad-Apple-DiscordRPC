from pypresence import Presence
import time


# After extracting frames, go to https://discord.com/developers/applications/ and create an application.
# Navigate to Rich Presence, and upload frames. If your animation has more than 300 frames, you will have to create multiple applications
# After all frames are uploaded, copy and paste the Application IDS into the list below.
# Example: client_ids = ["1234567890", "2345678901", "3456789012"]
client_ids = []

"""print(
    RPC.update(
        state="Lookie Lookie",
        large_image=f"512frame{i:04d}",
        details="A test of qwertyquerty's Python Discord RPC wrapper, pypresence!",
    )
)  # Set the presence"""

# It's recommended to keep the framerate at 5 as it's most consistent that way. With 30 it's smoother but you get dropped frames.
# If you have really good internet however, I won't stop you!
framerate = 5
while True:  # The presence will stay on as long as the program is running
    largest = 300
    i = 1
    for client_id in client_ids:
        RPC = Presence(client_id)
        RPC.connect()
        while i <= largest:
            """RPC.update(
                state="Bad Apple", large_image=f"512frame{i:04d}", details=f"Frame:{i}"
            )  # Set the presence"""
            """time_string = ""
            if i < 1800:
                time_string = f"0:{i // 30:02d}"
            else:"""
            time_string = f"{int(i / 30 / 60)}:{int(i // 30 % 60):02d}"
            print(
                RPC.update(
                    state=f"Framerate: {framerate} (* 6 skip = 30) FPS",
                    large_image=f"512frame{i:04d}",
                    details=f"Frame: {i}\nTimestamp: {time_string}",
                    buttons=[
                        {
                            "label": "【東方】Bad Apple!! ＰＶ【影絵】",
                            "url": f"https://youtu.be/FtutLA63Cp8?t={i//30}",
                        }
                    ],
                )
            )
            # print(f"512frame{i:04d}")
            time.sleep(1 / framerate)
            i += 1  # You can increase this to make it faster. At a framerate of 5 you can set this to 6 for a faster animation, but it looks more stopmotion.
        # Set this to the nearest multiple of 300 to the number of frames.
        if largest <= 6300:
            largest += 300
        else:
            # Change this number to the number of frames
            largest = 6571
        RPC.close()
