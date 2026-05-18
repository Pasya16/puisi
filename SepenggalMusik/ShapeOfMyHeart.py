import sys
import time
import pygame

def print_slow(text, delay=0.12):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("shape.mp3")
        pygame.mixer.music.play()
    except pygame.error:
        return

    print("Shape of My Heart - Backstreet Boys")
    print("=========================================")
    time.sleep(1.5)

    lyrics = [
        "I'm lookin' back on things I've done",
        "I never wanna play the same old part",
        "I'll keep you in the dark",
        "Now let me show you the shape of my heart"
    ]

    delays = [0.5, 0.5, 0.5, 1.0]

    sys.stdout.write("\033[1;36m")
    print_slow(lyrics[0], 0.12)
    time.sleep(delays[0])

    print("\033[F\r\033[1;30m" + lyrics[0] + "\033[0m")
    sys.stdout.write("\033[1;35m")
    print_slow(lyrics[1], 0.12)
    time.sleep(delays[1])

    print("\033[F\r\033[1;30m" + lyrics[1] + "\033[0m")
    sys.stdout.write("\033[1;32m")
    print_slow(lyrics[2], 0.12)
    time.sleep(delays[2])

    print("\033[F\r\033[1;30m" + lyrics[2] + "\033[0m")
    sys.stdout.write("\033[1;33m")
    print_slow(lyrics[3], 0.15)
    time.sleep(delays[3])

    print("\033[F\r\033[1;30m" + lyrics[3] + "\033[0m")
    
    time.sleep(5)

if __name__ == "__main__":
    main()