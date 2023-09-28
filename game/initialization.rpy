init python: 

    #some function definitions go here 
    def addToInventory(items): 
        for item in items: 
            inventoryItems.append(item)
   
        for enitem in environmentSprites: 
            if  enitem.type == item: 
                removeEnvironmentItem(item=enitem)
                break
        environmentSM.redraw(0)
        renpy.restart_interaction()

    def evironmentEvent(event, x, y, at): 
        if event.type == renpy.pygame_sdl2.MOUSEMOTION: 
            for item in environmentSprites: 
                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.width: 
                    t = Transform(child=item.hover_image, zoom = .25)
                    item.set_child(t)
                    environmentSM.redraw(0)
                else: 
                    t = Transform(child= item.idle_image, zoom = .25)
                    item.set_child(t)
                    environmentSM.redraw(0)
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP: 
            if event.button == 1: 
                for item in environmentSprites: 
          
                    if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height: 
                        if item.type == "claw": 
                            for bottle in environmentItemsDeleted: 
                                if bottle == "bottle": 
                                    addToInventory(["claw"])
                        elif item.type == "photo": 
                            addToInventory(["photo"])
                        elif item.type == "card": 
                            for rock in environmentItemsDeleted: 
                                if rock == "rock1": 
                                    addToInventory(["card"])
                                    break
                        elif item.type == "rock1": 
                            removeEnvironmentItem(item)
                        elif item.type == "rock2": 
                            removeEnvironmentItem(item)
                        elif item.type == "bottle": 
                            removeEnvironmentItem(item)
                        elif item.type == "lock": 
                            addToInventory(["lock"])
               
    def inventoryEvent(event, x, y, at): 
        if event.type == renpy.pygame_sdl2.MOUSEMOTION: 
            for item in inventorySprites: 
                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.width: 
                    t = Transform(child=item.hover_image, zoom = .75)
                    item.set_child(t)
                    inventorySM.redraw(0)
                else: 
                    t = Transform(child= item.idle_image, zoom = .75)
                    item.set_child(t)
                    inventorySM.redraw(0)
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP: 
            if event.button == 1: 
                for item in inventorySprites: 
                    if item.x <= x <= item.x + item.width and item.y <= y + item.height: 
                        if item.type == "claw": 
                            SetVariable("invItemSelected", 1)
                        elif item.type == "photo": 
                            renpy.show_screen("inspectInventory", "photo")
                        elif item.type == "card": 
                            SetVariable("invItemSelected", 3)
                        elif item.type == "lock": 
                            SetVariable("invItemSelected", 4)
                        elif item.type == "key": 
                            SetVariable("invItemSelected", 5)
                        #renpy.jump("inventoryInformation")
    
    def removeEnvironmentItem(item): 
        item.destroy()
        environmentItemsDeleted.append(item.type)
        environmentSprites.pop(environmentSprites.index(item))
        environmentItems.pop(environmentItems.index(item.type))
     