def welcome_screen():
    print(r"""
Welcome to...

 /$$$$$$$$                   /$$                                         /$$$$$$$                      /$$      
| $$_____/                  | $$                                        | $$__  $$                    | $$      
| $$    /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$ /$$   /$$      | $$  \ $$ /$$   /$$  /$$$$$$$| $$$$$$$ 
| $$$$$|____  $$| $$__  $$|_  $$_/   |____  $$ /$$_____/| $$  | $$      | $$$$$$$/| $$  | $$ /$$_____/| $$__  $$
| $$__/ /$$$$$$$| $$  \ $$  | $$      /$$$$$$$|  $$$$$$ | $$  | $$      | $$__  $$| $$  | $$|  $$$$$$ | $$  \ $$
| $$   /$$__  $$| $$  | $$  | $$ /$$ /$$__  $$ \____  $$| $$  | $$      | $$  \ $$| $$  | $$ \____  $$| $$  | $$
| $$  |  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$ /$$$$$$$/|  $$$$$$$      | $$  | $$|  $$$$$$/ /$$$$$$$/| $$  | $$
|__/   \_______/|__/  |__/   \___/   \_______/|_______/  \____  $$      |__/  |__/ \______/ |_______/ |__/  |__/
                                                         /$$  | $$                                              
                                                        |  $$$$$$/                                              
                                                         \______/                                                         

Every story needs as a hero... what's your name?
    """)

    name = input(">> ")

    print("""
Great! And for nothing of importance, what is your favourite animal?
          """)

    animal = input(">> ")

    print(
        f"""
OH NO! Your most favourite pet {animal} has fallen ill! The only cure is the reward for winning the kingdom's arena battle... So your only option is to fight!\n\nThe rules of the arena are simple... survive 20 rounds and defeat all of the enemies! Good luck."""
    )

    input("Press enter to begin...")
    return name
