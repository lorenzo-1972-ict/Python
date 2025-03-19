import os
import time

try:
    # Sniffer
    with open("log.txt", "w") as f:
        f.write("Sniffing...")
    time.sleep(5)
    print("Data sniffed!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This will always execute")
    os.remove("log.txt")
print("This will execute after the try/except block")