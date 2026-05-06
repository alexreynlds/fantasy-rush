import random


class Enemy:
    def __init__(self, name, gold, attack, health, mana, stamina, speed):
        self.name = name
        self.gold_reward = gold

        self.max_health = health
        self.max_mana = mana
        self.max_stamina = stamina

        self.health = self.max_health
        self.mana = self.max_mana
        self.stamina = self.max_stamina

        self.attack_power = attack
        self.speed = speed

        # modifiers
        self.is_blocking = False
        self.is_dodging = False

        self.actions = {
            "Attack": {"category": "main", "fn": self.attack, "cost": 0},
        }

    def pay_cost(self, action):
        cat = action["category"]
        cost = action.get("cost", 0)

        if cat == "stamina":
            self.stamina -= cost
        elif cat == "mana":
            self.mana -= cost

    def do_turn(self, other):
        # Keep rolling a move until the enemy has enough resources to use it
        while True:
            action_int = random.randint(1, len(self.actions))
            action_name = list(self.actions.keys())[action_int - 1]
            action_cat = self.actions[action_name]["category"]
            action_cost = self.actions[action_name]["cost"]

            if action_cat == "mana" and self.mana < action_cost:
                continue

            elif action_cat == "stamina" and self.stamina < action_cost:
                continue

            break

        action_function = self.actions[action_name]["fn"]
        action = self.actions[action_name]

        messages = []

        if other.is_blocking:
            other.is_blocking = False
            return f"{self.name} tried to {action_name}, but failed as {other.name} was blocking!"

        if other.is_dodging:
            other.is_dodging = False
            if random.random() < 0.5:
                return f"{self.name} tried to {action_name}, but {other.name} dodged!"
            messages.append(f"{other.name} failed to dodge!")
        else:
            evasion_check = random.random()
            if evasion_check <= other.evasion:
                return f"{self.name} tried to {action_name}, but {other.name} evaded the attack"

        self.pay_cost(action)
        messages.append(action_function(other))
        return messages

    def attack(self, other):
        attack_amount = random.randint(1, self.attack_power)
        other.take_damage(attack_amount)
        return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def take_damage(self, amount):
        self.health -= amount


# name, gold, attack, health, mana, stamina, speed


# Regular enemies
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 3, 2, 12, 0, 5, 2)
        self.actions["Throw Rock"] = {
            "category": "stamina",
            "fn": self.throw_rock,
            "cost": 1,
        }

    def throw_rock(self, other):
        attack_amount = random.randint(1, self.attack_power * 2)
        other.take_damage(attack_amount)
        return f"{self.name} threw a rock at {other.name}... dealing {attack_amount} damage..."


class Kobold(Enemy):
    def __init__(self):
        super().__init__("Kobold", 5, 2, 15, 5, 5, 2)
        self.actions["Throw Pickaxe"] = {
            "category": "stamina",
            "fn": self.throw_pickaxe,
            "cost": 1,
        }
        self.actions["Prized Candle"] = {
            "category": "mana",
            "fn": self.prized_candle,
            "cost": 2,
        }

    def throw_pickaxe(self, other):
        attack_amount = random.randint(1, int(self.attack_power * 1.5))
        other.take_damage(attack_amount)
        return f"{self.name} lobs their pickaxe at {other.name}, dealing {attack_amount} damage..."

    def prized_candle(self, other):
        attack_amount = random.randint(1, int(self.attack_power * 2))
        other.take_damage(attack_amount)
        return f"{self.name} pours magic into their prized candle, sending the flame towards {other.name}, dealing {attack_amount} damage..."


class Bear(Enemy):
    def __init__(self):
        super().__init__("Bear", 6, 3, 25, 0, 10, 6)
        self.actions["Scratch"] = {
            "category": "stamina",
            "fn": self.scratch,
            "cost": 2,
        }

    def scratch(self, other):
        attack_amount = random.randint(1, self.attack_power * 2)
        other.take_damage(attack_amount)
        return f"{self.name} viciously scratches {other.name} dealing {attack_amount} damage"


# Bosses
class Phoenix(Enemy):
    def __init__(self):
        super().__init__("Ancient Phoenix", 0, 2, 5, 0, 5, 2)
        self.has_rebirthed = False
        self.actions["frail_peck"] = {
            "category": "main",
            "fn": self.frail_peck,
            "cost": 0,
        }

    def rebirth(self):
        self.name = "Reborn Phoenix"
        self.attack_power = 4
        self.max_health = 50
        self.health = 50
        self.mana = 25
        self.stamina = 20
        self.speed = 6
        self.actions["frail_peck"] = {
            "category": "main",
            "fn": self.drill_peck,
            "cost": 0,
        }

        self.actions["solar_flare"] = {
            "category": "mana",
            "fn": self.solar_flare,
            "cost": 3,
        }

        self.actions["arial_assult"] = {
            "category": "stamina",
            "fn": self.arial_assult,
            "cost": 3,
        }

        self.actions["restorative_flame"] = {
            "category": "mana",
            "fn": self.restorative_flame,
            "cost": 5,
        }

    def take_damage(self, amount):
        if self.health - amount <= 0 and not self.has_rebirthed:
            self.has_rebirthed = True
            self.rebirth()
            return "The Ancient Phoenix crumbles to dust... and from the ashes it rises, reborn"
        else:
            self.health -= amount

    def frail_peck(self, other):
        attack_amount = random.randint(1, self.attack_power)
        other.take_damage(attack_amount)
        return f"The {self.name} pecks at {other.name} for {attack_amount} damage"

    def drill_peck(self, other):
        attack_amount = random.randint(1, self.attack_power)
        other.take_damage(attack_amount)
        return f"The {self.name} pecks ferociously at {other.name}, causing {attack_amount} damage"

    def solar_flare(self, other):
        attack_amount = random.randint(1, int(self.attack_power * 1.5))
        other.take_damage(attack_amount)
        return f"{self.name} charges up a solar blast and fires it at {other.name}, burning them for {attack_amount} damage"

    def arial_assult(self, other):
        attack_amount = random.randint(1, int(self.attack_power * 1.5))
        other.take_damage(attack_amount)
        return f"{self.name} soars rapidly towards {other.name}, hitting them for {attack_amount} damage"

    def restorative_flame(self, other):
        heal_amount = random.randint(3, self.max_health // 5)
        actual = min(self.health + heal_amount, self.max_health) - self.health
        self.health += actual
        return f"{self.name} plucks one of its feathers and consumes it, restoring {actual} health"


class Hydra(Enemy):
    def __init__(self):
        super().__init__("Hydra", 15, 3, 40, 20, 0, 2)
        self.speed = 2

        self.actions = {
            "Savage Bite": {"category": "main", "fn": self.savage_bite, "cost": 0},
            "Regrow Head": {"category": "mana", "fn": self.regrow_head, "cost": 5},
        }

    def savage_bite(self, other):
        attack_amount = random.randint(1, self.attack_power)
        other.take_damage(attack_amount)
        return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def regrow_head(self, other):
        heal_amount = random.randint(5, 15)
        actual = min(self.health + heal_amount, self.max_health) - self.health
        self.health += actual

        return f"{self.name} regrows one of its heads, healing themselves for {actual}"


regular_enemies = [Goblin, Bear, Kobold]
boss_enemies = [Hydra, Phoenix]
