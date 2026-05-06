class Item:
    def __init__(self, name, cost, category, effect, desc):
        self.name = name
        self.cost = cost
        self.category = category
        self.effect = effect
        self.desc = desc


def apply_health_potion(player):
    player.health = min(player.health + 5, player.max_health)


def apply_mana_potion(player):
    player.mana = min(player.mana + 5, player.max_mana)


def apply_stamina_potion(player):
    player.stamina = min(player.stamina + 5, player.max_stamina)


def apply_lightning_boots(player):
    player.speed += 1


def apply_lucky_clover(player):
    player.crit_chance += 0.05


def apply_heart_container(player):
    player.max_health += 5
    player.health = min(player.health + 5, player.max_health)


def apply_touch_grass_manual(player):
    player.max_stamina += 5
    player.stamina = min(player.stamina + 5, player.max_stamina)


def apply_ancient_tome(player):
    player.max_mana += 5
    player.mana = min(player.mana + 5, player.max_mana)


def apply_heal_spell_tome(player):
    player.actions["Heal"] = {
        "category": "mana",
        "fn": player.heal,
        "cost": 3,
        "desc": "Heal yourself",
    }


def apply_fire_spell_tome(player):
    player.actions["Fire"] = {
        "category": "mana",
        "fn": player.fire,
        "cost": 4,
        "desc": "Set your opponent on fire",
    }


health_potion = Item(
    "Health Potion", 4, "consumable", apply_health_potion, "Restore Health"
)
mana_potion = Item("Mana Potion", 3, "consumable", apply_mana_potion, "mana")
stamina_potion = Item(
    "Stamina Potion", 3, "consumable", apply_stamina_potion, "Restore Stamina"
)

lightning_boots = Item(
    "Lightning Boots", 8, "equipment", apply_lightning_boots, "Restore Mana"
)
lucky_clover = Item(
    "Lucky Clover", 8, "equipment", apply_lucky_clover, "Increase your crit chance"
)
heart_container = Item(
    "Heart Container", 6, "equipment", apply_heart_container, "Increase your max health"
)
touch_grass_manual = Item(
    "Manual on How to Touch Grass",
    6,
    "equipment",
    apply_touch_grass_manual,
    "Increase your max stamina",
)
ancient_tome = Item(
    "Ancient Tome",
    6,
    "equipment",
    apply_ancient_tome,
    "Increase your max mana",
)

heal = Item(
    "Heal Spell Tome", 5, "ability", apply_heal_spell_tome, "A basic healing spell"
)
fire = Item(
    "Fire Spell Tome", 5, "ability", apply_fire_spell_tome, "A first blast spell"
)

shop_items = [
    health_potion,
    mana_potion,
    stamina_potion,
    lightning_boots,
    lucky_clover,
    touch_grass_manual,
    ancient_tome,
    heart_container,
    heal,
    fire,
]
