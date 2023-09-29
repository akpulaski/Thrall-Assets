label start: 
    call generalSetUp
    jump setUpUndergroundCenter
    return 

label selectScene: 
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

label showInventory: 
    show inventory bg 
    jump setUpInventory
