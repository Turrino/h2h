import random


class ModParser:
    @staticmethod
    def parse_all(mods, attribute_dict):
        attributes = {
            "Items": [attribute_dict.keys()],
            "Character":  attribute_dict["Character"]
        }
        parsed = {}
        for key, value in mods.items():
            parsed[key] = ModParser.parse(value, attributes)
        return parsed

    @staticmethod
    def parse(text, attributes):

        splat = text.split(" ")

        if splat[0] == "random":
            if len(splat) != 2:
                raise ValueError('descriptive error here')
            mod = Mod({"percentage": int(splat[1])}, ModParser.rnd)

        elif splat[0] == "has":
            if splat[1] not in attributes["Items"]:
                raise ValueError('descriptive error here')
            amount = int(splat[2]) if len(splat) == 3 else 1
            args = {"item_type": splat[1], "amount": amount}
            mod = Mod(args, ModParser.has_item)

        elif splat[0] == "is":
            if splat[1] not in attributes["Character"] or len(splat) != 4:
                raise ValueError('descriptive error here')
            args = {"attribute": splat[1], "comparison": splat[2], "value": int(splat[3])}
            mod = Mod(args, ModParser.has_attribute)

        else:
            raise ValueError('descriptive error here')

        return mod

    @staticmethod
    def rnd(percentage):
        return random.randrange(0, 100) < percentage

    @staticmethod
    def has_item(fundamentals, item_type, amount=1):
        # todo implement story fundamentals
        return False

    @staticmethod
    def has_attribute(fundamentals, attribute, comparison, value):
        # todo implement story fundamentals
        return True


class Mod:
    def __init__(self, args, process):
        self.args = args
        self.process = process

    def apply(self, fundamentals):
        self.args["fundamentals"] = fundamentals
        return self.process(**self.args)
