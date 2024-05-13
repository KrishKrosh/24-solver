import itertools

class CardGameSolver:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.numbers = list(range(1, 14))  # 1 through 13
        self.target = 24

    def change_target(self, target):
        self.target = target

    def generate_permutations(self, num):
        if len(num) == 1:
            return [num]
        else:
            perms = []
            for i in range(len(num)):
                for perm in self.generate_permutations(num[:i] + num[i+1:]):
                    perms.append(num[i] + perm)
            return perms

    def generate_operation_combinations(self):
        combs = []
        for op1 in self.operators:
            for op2 in self.operators:
                for op3 in self.operators:
                    combs.append([f" {op1} ", f" {op2} ", f" {op3} "])
        return combs

    def generate_hands(self):
        hands = []
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if j == i:
                    continue
                for k in range(len(self.numbers)):
                    if k == i or k == j:
                        continue
                    for l in range(len(self.numbers)):
                        if l == i or l == j or l == k:
                            continue
                        hands.append([self.numbers[i], self.numbers[j], self.numbers[k], self.numbers[l]])
        return hands

    def solve(self, hand):
        solutions = set()
        # Generate all permutations of numbers as strings
        perms = [''.join([str(x) for x in p]) for p in itertools.permutations(hand)]
        operation_combs = self.generate_operation_combinations()

        for perm in perms:
            for op_comb in operation_combs:
                # Create expressions ensuring explicit multiplication
                expressions = [
                    # Expression: (((a + b) + c) + d)
                    f"(({perm[0]}{op_comb[0]}{perm[1]}){op_comb[1]}{perm[2]}){op_comb[2]}{perm[3]}",

                    # Expression: (a + b) + (c + d)
                    f"({perm[0]}{op_comb[0]}{perm[1]}){op_comb[1]}({perm[2]}{op_comb[2]}{perm[3]})",

                    # Expression: a + (b + (c + d))
                    f"{perm[0]}{op_comb[0]}({perm[1]}{op_comb[1]}({perm[2]}{op_comb[2]}{perm[3]}))",
                ]
                for expr in expressions:
                    try:
                        if eval(expr) == self.target:
                            solutions.add(expr)
                    except ZeroDivisionError:
                        continue
        
        return solutions
