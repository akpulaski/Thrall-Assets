label start: 
    call generalSetUp from _call_generalSetUp
    jump setUpUndergroundCenter
    return 

label selectScene: 
    python: 
        for item in inventoryItems: 
            if item == "lock": 
                hasLock = True
            elif item == "key": 
                hasKey = True 
            elif item == "claw": 
                hasClaw = True 
            elif item == "card": 
                hasCard = True
            elif item == "photo": 
                hasPhoto = True 
        
    if hasPhoto and hasLock and hasClaw and hasCard: 
        $ hasAll = True 
    
    if not hasAll: 
        if location == 1: 
            scene underground bg 
            jump setUpUndergroundLeft
        elif location == 2: 
            scene underground bg 
            jump setUpUndergroundCenter 
        elif location == 3: 
            scene underground bg 
            jump setUpUndergroundRight 
        elif location == 4: 
            scene bank bg 
            jump setUpBank 
    else: 
        jump nextScene


label nextScene: 
    scene black
    show screen inventoryButton 
    "I'm talking but I still want to be able to acces the inventory."
    "I need a few more lines for testing."
    return
