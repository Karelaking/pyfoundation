import math


class Trigonometry:
    def sin(*args):
        if isinstance(args[0], float):
            return math.sin((args[0] * math.pi) / 180)
        elif isinstance(args[0], int):
            return math.sin((args[0] * math.pi) / 180)
        else:
            if not all(isinstance(n, float) and n >= 0 for n in args[0]):
                pass
            elif not all(isinstance(n, int) and n >= 0 for n in args[0]):
                pass
            return [math.sin((n * math.pi) / 180) for n in args[0]]

    def cos(*args):
        if isinstance(args[0], float):
            return math.cos((args[0] * math.pi) / 180)
        elif isinstance(args[0], int):
            return math.cos((args[0] * math.pi) / 180)
        else:
            if not all(isinstance(n, float) and n >= 0 for n in args[0]):
                pass
            elif not all(isinstance(n, int) and n >= 0 for n in args[0]):
                pass
            return [math.cos((n * math.pi) / 180) for n in args[0]]

    def tan(*args):
        if isinstance(args[0], float):
            return math.tan((args[0] * math.pi) / 180)
        elif isinstance(args[0], int):
            return math.tan((args[0] * math.pi) / 180)
        else:
            if not all(isinstance(n, float) and n >= 0 for n in args[0]):
                pass
            elif not all(isinstance(n, int) and n >= 0 for n in args[0]):
                pass
            return [math.tan((n * math.pi) / 180) for n in args[0]]

    def cosec(*args):
        if isinstance(args[0], float):
            return 1 / math.sin((args[0] * math.pi) / 180)
        elif isinstance(args[0], int):
            return 1 / math.sin((args[0] * math.pi) / 180)
        else:
            if not all(isinstance(n, float) and n >= 0 for n in args[0]):
                pass
            elif not all(isinstance(n, int) and n >= 0 for n in args[0]):
                pass
            return [1 / math.sin((n * math.pi) / 180) for n in args[0]]

    def sec(*args):
        if isinstance(args[0], float):
            return math.cos((args[0] * math.pi) / 180)
        elif isinstance(args[0], int):
            return math.cos((args[0] * math.pi) / 180)
        else:
            if not all(isinstance(n, float) and n >= 0 for n in args[0]):
                pass
            elif not all(isinstance(n, int) and n >= 0 for n in args[0]):
                pass
            return [1 / math.cos((n * math.pi) / 180) for n in args[0]]

    def cot(*args):
        if isinstance(args[0], float):
            return 1 / math.tan((args[0] * math.pi) / 180)
        elif isinstance(args[0], int):
            return 1 / math.tan((args[0] * math.pi) / 180)
        else:
            if not all(isinstance(n, float) and n >= 0 for n in args[0]):
                pass
            elif not all(isinstance(n, int) and n >= 0 for n in args[0]):
                pass
            return [1 / math.tan((n * math.pi) / 180) for n in args[0]]


