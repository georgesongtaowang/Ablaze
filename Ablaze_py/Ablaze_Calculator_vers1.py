import argparse


class Calculator:
    def __init__(self, args):
        self.mon_exp = args.mon_exp
        self.swr = args.swr
        m = float(self.mon_exp)
        s = float(self.swr)
        MethodsCalling.Fire(m, s)


class MethodsCalling:
    @staticmethod
    def Fire(mon_exp, swr):
        # Calculates the Fire number using safe control rate and monthly expenses.
        annual_exp = mon_exp * 12
        Fire_number = annual_exp / swr
        print(Fire_number)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Finance Calculator used to calculate when financial independence can "
                                                "be reached predict age of retirement")
    parse.add_argument("mon_exp", help="is the monthly expense of the individual")
    parse.add_argument("swr", help="is the safe withdrawal rate")
    val = parse.parse_args()
    Calculator(val)


