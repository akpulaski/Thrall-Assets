label generalSetUp: 
    default location = 2

    python: 
        #Disables rollback because it messes with inventory system.
        config.rollback_enabled = False 

        #Sprite Management 
        environmentSM = SpriteManager(event = evironmentEvent)
        inventorySM = SpriteManager(update = inventoryUpdate, event = inventoryEvent)

        #General Declarations 
        environmentSprites = []
        inventorySprites = []
        evironmentItems = []
        inventoryItems = []
        environmentItemNames = []
        inventoryItemNames = ["Key", "Lock", "Card", "Claw", "Photo"]
        environmentItemsDeleted = []

        

    
label setUpUndergroundCenter: 
    $ environmentItems = ["photo"]

    python: 
        for item in environmentSprites: 
            item.destroy()
            environmentSM.redraw(0)
        environmentSprites = []

   
    python: 

        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "card": 
                    environmentSprites[-1].x = 200 
                    environmentSprites[-1].y = 900
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100
                elif item == "claw": 
                    environmentSprites[-1].x = 750 
                    environmentSprites[-1].y = 650 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100
                elif item == "photo": 
                    environmentSprites[-1].x = 1300 
                    environmentSprites[-1].y = 900 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100

    scene underground bg
    call screen undergroundCenterScene


label setUpUndergroundLeft: 
    $ environmentItems = ["card"]

    python: 
        for item in environmentSprites: 
            item.destroy() 
            environmentSM.redraw(0)
        environmentSprites = []
        
    python: 

        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "card": 
                    environmentSprites[-1].x = 200 
                    environmentSprites[-1].y = 900
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100

    scene underground bg 
    call screen undergroundLeftScene

label setUpUndergroundRight: 
    $ environmentItems = ["claw"]
    python: 
        for item in environmentSprites: 
            item.destroy()
            environmentSM.redraw(0)
        environmentSprites = []
    

    python:

        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "claw": 
                    environmentSprites[-1].x = 750 
                    environmentSprites[-1].y = 650 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100
    
    scene underground bg 
    call screen undergroundRightScene

label setUpBank: 
    $ environmentItems = ["lock"]

    python: 
        for item in environmentSprites: 
            item.destroy()
            environmentSM.redraw(0)
        environmentSprites = []

    python: 
        for item in environmentItems: 
            if item not in environmentItemsDeleted: 
                idle_image = Image("items/{}_idle.png".format(item))
                hover_image = Image("items/{}_hover.png".format(item))
                t = Transform(child = idle_image, zoom = .25)
                environmentSprites.append(environmentSM.create(t))
                environmentSprites[-1].type = item
                environmentSprites[-1].idle_image = idle_image
                environmentSprites[-1].hover_image = hover_image
                if item == "lock": 
                    environmentSprites[-1].x = 1600 
                    environmentSprites[-1].y = 1000 
                    environmentSprites[-1].width = 100
                    environmentSprites[-1].height = 100 
    
    scene bank bg 
    call screen bankScene