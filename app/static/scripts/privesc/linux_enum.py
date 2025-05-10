
import os
import platform

def enum_system():
    print(f"OS: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Current user: {os.getenv('USER')}")

if __name__ == "__main__":
    enum_system()
