command = ""

while True:
    command = input(">:").lower()

    if command == "start":
        print("Car started. Ready to go!")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "quit":
        break
    else:
        print("I don't understand this...")
