import random


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

        self.max_health = 30
        self.max_mana = 10
        self.max_stamina = 10

        self.health = self.max_health
        self.mana = self.max_mana
        self.stamina = self.max_stamina

        self.attack_power = 3
        self.crit_chance = 0.10
        self.speed = 5
        self.evasion = 0.05

        # modifiers
        self.is_blocking = False
        self.is_dodging = False

        self.gold = 5

        self.actions = {
            "Attack": {
                "category": "main",
                "fn": self.attack,
                "cost": 0,
                "desc": "A basic attack with your weapon",
            },
            "Heavy Attack": {
                "category": "stamina",
                "fn": self.heavy_attack,
                "cost": 3,
                "desc": "Empower your blow with stamina",
            },
            "Block": {
                "category": "stamina",
                "fn": self.block,
                "cost": 2,
                "desc": "Block your opponents next attack",
            },
            "Dodge": {
                "category": "stamina",
                "fn": self.dodge,
                "cost": 1,
                "desc": "Attempt to dodge your opponents next attack (50/50)",
            },
        }

    def pay_cost(self, action):
        cat = action["category"]
        cost = action.get("cost", 0)

        if cat == "stamina":
            self.stamina -= cost
        elif cat == "mana":
            self.mana -= cost

    def attack(self, other):
        crit_roll = random.random()
        attack_amount = random.randint(1, self.attack_power)

        if crit_roll <= self.crit_chance:
            attack_amount *= 2
            msg = other.take_damage(attack_amount)
            result = (
                f"CRIT! {self.name} attacks {other.name} for {attack_amount} damage"
            )

            if msg:
                return [result, msg]
            return result
        else:
            msg = other.take_damage(attack_amount)
            result = f"{self.name} attacks {other.name} for {attack_amount} damage"

            if msg:
                return [result, msg]
            return result

    def heavy_attack(self, other):
        crit_roll = random.random()
        attack_amount = random.randint(self.attack_power, self.attack_power * 2)

        if crit_roll <= self.crit_chance:
            attack_amount *= 2
            msg = other.take_damage(attack_amount)
            result = f"CRIT! {self.name} hits {other.name} with a heavy attack for {attack_amount} damage"

            if msg:
                return [result, msg]
            return result
        else:
            msg = other.take_damage(attack_amount)
            result = f"{self.name} hits {other.name} with a heavy attack for {attack_amount} damage"

            if msg:
                return [result, msg]
            return result

    def block(self, other):
        self.is_blocking = True
        return f"{self.name} prepares to block {other.name}'s attack"

    def dodge(self, other):
        self.is_dodging = True
        return f"{self.name} prepares to dodge {other.name}'s attack"

    def fire(self, other):
        attack_amount = random.randint(5, 10)
        msg = other.take_damage(attack_amount)
        result = f"{self.name} blasts {other.name} with fire for {attack_amount} damage"

        if msg:
            return [result, msg]
        return result

    def heal(self, other):
        heal_amount = random.randint(self.max_health // 4, self.max_health // 3)

        actual = min(self.health + heal_amount, self.max_health) - self.health

        self.health += actual

        # self.health += heal_amount
        return f"{self.name} heals themselves for {actual} HP"

    def take_damage(self, amount):
        self.health -= amount
