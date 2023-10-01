screen undergroundCenterScene: 
    add environmentSM
    imagebutton:
        auto "nav/left_%s.png"
        xpos 50 
        ypos 500
        action[SetVariable("location", location - 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/right_%s.png"
        xpos 1750 
        ypos 500 
        action[SetVariable("location", location + 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/up_%s.png"
        xpos 900 
        ypos 50
        action[SetVariable("location", 4), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Show("inventoryScene")]

screen undergroundLeftScene: 
    add environmentSM
    imagebutton: 
        auto "nav/right_%s.png"
        xpos 1750 
        ypos 500 
        action[SetVariable("location", location + 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/up_%s.png"
        xpos 900 
        ypos 50
        action[SetVariable("location", 4), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Show("inventoryScene")]

screen undergroundRightScene: 
    add environmentSM
    imagebutton: 
        auto "nav/left_%s.png"
        xpos 50 
        ypos 500
        action[SetVariable("location", location - 1), Jump("selectScene")]
    imagebutton: 
        auto "nav/up_%s.png"
        xpos 900 
        ypos 50
        action[SetVariable("location", 4), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Show("inventoryScene")]

screen bankScene: 
    add environmentSM
    imagebutton: 
        auto "nav/left_%s.png"
        xpos 50 
        ypos 500 
        action[SetVariable("location", 2), Jump("selectScene")]
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Show("inventoryScene")]

screen inventoryButton: 
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50
        ypos 50
        action[Show("inventoryScene")]


screen inventoryScene: 
    image "backgrounds/inventory bg.png"
    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50 
        ypos 50
        action[Hide("infoScene"), Hide("inventoryScene")]
    for item in inventoryItems: 
        if item == "claw":
            imagebutton: 
                auto "items/claw_%s.png" at smaller 
                xpos 600 
                ypos 700 
                action[Show("infoScene", item = "claw")]
        if item == "lock": 
            imagebutton: 
                auto "items/lock_%s.png" at smaller 
                xpos 350
                ypos 300
                action[Show("infoScene", item ="lock")]
        if item == "key": 
            imagebutton: 
                auto "items/key_%s.png" at smaller 
                xpos 350 
                ypos 700 
                action[Show("infoScene", item = "key")]
        if item == "card": 
            imagebutton: 
                auto "items/card_%s.png" at smaller
                xpos 600 
                ypos 250 
                action [Show("infoScene", item = "card")]
        if item == "photo": 
            imagebutton: 
                auto "items/photo_%s.png" at smaller
                xpos 500
                ypos 500 
                action[Show("infoScene", item = "photo")]
        
        #textbutton "Move On" xalign .75 yalign .75 action[Hide("infoScene"), Hide("inventoryScene"), Jump("nextScene")]

screen infoScene(item = None): 
    if item == "photo": 
        text "Photo" at nameLoc
        text "She looks so familiar." at descLoc 
        text "Almost evil. I think I saw" at descLoc2
        text "her on a wanted poster before..." at descLoc3
    elif item == "claw": 
        text "Claw" at nameLoc
        text "A bloody golden claw?" at descLoc
        text "Royal lycans use them as weapons." at descLoc2
    elif item == "lock": 
        text "Lock" at nameLoc
        text "I have a lock." at descLoc 
        text "But where's the key?" at descLoc2
    elif item == "card": 
        text "Card" at nameLoc
        text "Lok-Yin Kwong? Blood Banker." at descLoc
        text "Who can this be?" at descLoc2
    elif item == "key": 
        text "Key" at nameLoc
        text "It seems I had the key to my soul all along..." at descLoc1



