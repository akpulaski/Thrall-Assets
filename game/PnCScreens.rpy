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
        action[Jump("showInventory")]

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
        action[Jump("showInventory")]

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
        action[Jump("showInventory")]

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
        action[Jump("showInventory")]


screen inventoryScene: 
    add inventorySM

    imagebutton: 
        auto "nav/gear_%s.png"
        xpos 50 
        ypos 50
        action[Jump("selectScene")]
