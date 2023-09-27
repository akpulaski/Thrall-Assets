init python: 

    #some function definitions go here 
    def addToInventory(items): 
        for item in items: 
            inventoryItems.append(item)
            item_image = Image("items/{}_idle.png")
            t = Transform(child= item_image, zoom = .5)
            inventorySprites.append(inventorySM.create(t))
            inventorySprites[-1].type = item
            inventorySprites[-1].item_image = item_image
   
        for enitem in environmentSprites: 
            if  enitem.type == item: 
                removeEnvironmentItem(item=enitem)
                break

        inventorySM.redraw(0)
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
                            addToInventory(["claw"])
                        elif item.type == "photo": 
                            addToInventory(["photo"])
                        elif item.type == "card": 
                            addToInventory(["card"])
                        
               
    def inventoryEvent(event, x, y, at): 
        pass 

    def inventoryUpdate(st): 
        pass 
    
    def removeEnvironmentItem(item): 
        item.destroy()
        environmentItemsDeleted.append(item.type)
        environmentSprites.pop(environmentSprites.index(item))
        environmentItems.pop(environmentItems.index(item.type))
     
