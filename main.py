command = ""
command = command.lower()
started = False
stopped = False
while True:
    
    command = input("> ")
    if command == "start":
        if started:
            print("The Car is already running")
        else:
            started = True
            print("Car has started")
        
            
    elif command == "stop":
        if  stopped:
            print("You have already Pulled Over the car")
        else:
            stopped = True
            print("The car has stopped")
    elif command == "help":
        print("""
start - to satet the car
stop - to stop the car
quit - to quit the game
             """)
    elif command == "quit":
        print("You quit the game")
        break
    else:
        print("I dont understand")