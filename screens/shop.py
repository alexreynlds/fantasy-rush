import os
import random
from console import console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich.console import Group
from item import shop_items


def print_shop(player):
    consumables = []
    equipment = []
    abilities = []

    for item in shop_items:
        if item.category == "equipment":
            equipment.append(item)
        elif item.category == "ability":
            abilities.append(item)
        else:
            consumables.append(item)

    current_shop_items = consumables + random.sample(equipment, k=3) + abilities
    current_shop_items = [
        item
        for item in current_shop_items
        if item.category != "ability" or item.name.split()[0] not in player.actions
    ]

    while True:
        clear = lambda: os.system("clear")

        # Player Stats
        # Displaying all of the possible  the player can take
        player_table = Table(title=player.name, show_header=False, border_style="blue")
        player_table.add_column("Stat", style="cyan")
        player_table.add_column("Value", style="white")
        player_table.add_column("Stat2", style="cyan")
        player_table.add_column("Value2", style="white")
        player_table.add_row(
            "HP",
            f"{str(player.health)}/{str(player.max_health)}",
            "Crit chance",
            str(player.crit_chance),
        )
        player_table.add_row(
            "Stamina",
            f"{str(player.stamina)}/{str(player.max_stamina)}",
            "Speed",
            str(player.speed),
        )
        player_table.add_row(
            "Mana",
            f"{str(player.mana)}/{str(player.max_mana)}",
            "Evasion",
            str(player.evasion * 100) + "%",
        )

        shop_table = Table(
            title="Shop Inventory", show_header=True, border_style="blue"
        )
        categories = {"consumable": [], "equipment": [], "ability": []}

        for i, item in enumerate(current_shop_items, start=1):
            cat = item.category
            cost = item.cost
            cost_label = f"{cost} gold" if cost > 0 else "Free"
            entry = f"[{i}] {item.name} - {cost_label}\n    - {item.desc}"
            categories[cat].append(entry)

        # Get the longest category list to determine the max row (col height)
        max_rows = max(len(v) for v in categories.values())
        for cat in categories:
            categories[cat] += [""] * (max_rows - len(categories[cat]))
            shop_table.add_column(cat.capitalize())

        # Construct the rows of the table and add them
        for row in zip(
            categories["consumable"], categories["equipment"], categories["ability"]
        ):
            shop_table.add_row(*row)

        quit_text = Text('Enter "q" to quit the shop')

        # Organising the printout and printing it
        body = Group(player_table, shop_table, quit_text)

        header = Text(
            f"Welcome to the shop | {player.gold} Gold",
            style="bold yellow",
            justify="center",
        )

        # Print the shop screen for the user
        clear()
        console.print(Panel(body, title=header, border_style="green", padding=(1, 2)))

        while True:
            choice = input(">> ")
            if choice == "q":
                return
            if choice.isdigit() and 1 <= int(choice) <= len(current_shop_items):
                choice = int(choice)
                item = current_shop_items[choice - 1]
                if player.gold >= item.cost:
                    player.gold -= item.cost
                    item.effect(player)
                    current_shop_items.remove(item)
                    print(f"Bought {item.name}!")
                    input("Press Enter to continue")
                    break
                else:
                    print("Not enough gold")
            else:
                print("Invalid option")
