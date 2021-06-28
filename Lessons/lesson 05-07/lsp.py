class Calc:

    def do_operation(self, arg1, arg2):
        return f"operation on {arg1} and {arg2}"

class Sum_Calc(Calc):

    def do_operation(self, arg1, arg2):
        return arg1+arg2

    def do_operation_with_print(self, arg1, arg2):
        res = super().do_operation(arg1, arg2)
        print(res)
        return res

class Sub_Calc(Calc):

    def do_operation(self, arg1, arg2):
        return arg1-arg2

class Mult_Calc(Calc):

    def do_operation(self, arg1, arg2):
        return arg1*arg2

class Div_Calc(Calc):

    def do_operation(self, arg1, arg2):
        return arg1/arg2

arg1 = 10
arg2 = 5

Calc().do_operation(arg1, arg2)

Sum_Calc().do_operation_with_print(arg1, arg2)

operations = [Calc(), Sum_Calc(), Sub_Calc(), Mult_Calc(), Div_Calc()]
for op in operations:
    print(op.do_operation(arg1, arg2))