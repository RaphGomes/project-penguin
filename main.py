def on_a_pressed():
    global Level
    if Level == 0:
        Level = 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def Level_Control():
    if Level == 0:
        scene.set_background_image(assets.image("""
            myImage9
        """))
    if Level == 1:
        pass
Level = 0
Level = 0
Level_Control()