"""Bounded AST interpreter: expressions are data and are never executed as Python."""

import ast
import math
import operator


class CalculationError(ValueError):
    """An invalid, undefined, or overly expensive calculation."""


def calculate(expression: str, angle_mode: str = "rad") -> float:
    if angle_mode not in {"rad", "deg"}:
        raise CalculationError("Angle mode must be rad or deg.")
    if not expression.strip() or len(expression) > 256:
        raise CalculationError("Enter an expression of 1–256 characters.")
    expression = expression.replace("^", "**").replace("π", "pi")
    expression = expression.replace("×", "*").replace("÷", "/").replace("−", "-")
    try:
        tree = ast.parse(expression.strip(), mode="eval")
    except (SyntaxError, ValueError, RecursionError) as exc:
        raise CalculationError("Check the expression and parentheses.") from exc
    if sum(1 for _ in ast.walk(tree)) > 128:
        raise CalculationError("Expression is too complex.")

    def trig(fn, value):
        return fn(math.radians(value) if angle_mode == "deg" else value)

    def inverse(fn, value):
        result = fn(value)
        return math.degrees(result) if angle_mode == "deg" else result

    def tangent(value):
        radians = math.radians(value) if angle_mode == "deg" else value
        if abs(math.cos(radians)) < 1e-12:
            raise CalculationError("Tangent is undefined at this angle.")
        return math.tan(radians)

    def factorial(value):
        if not float(value).is_integer() or not 0 <= value <= 170:
            raise CalculationError("Factorial needs an integer from 0 to 170.")
        return math.factorial(int(value))

    functions = {
        "sin": lambda x: trig(math.sin, x),
        "cos": lambda x: trig(math.cos, x),
        "tan": tangent,
        "asin": lambda x: inverse(math.asin, x),
        "acos": lambda x: inverse(math.acos, x),
        "atan": lambda x: inverse(math.atan, x),
        "sqrt": math.sqrt,
        "ln": math.log,
        "log": math.log10,
        "exp": math.exp,
        "abs": abs,
        "floor": math.floor,
        "ceil": math.ceil,
        "factorial": factorial,
    }
    operations = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
                  ast.Div: operator.truediv, ast.Mod: operator.mod, ast.Pow: operator.pow}

    def visit(node, depth=0):
        if depth > 24:
            raise CalculationError("Too many nested operations.")
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            result = float(node.value)
        elif isinstance(node, ast.Name) and node.id in {"pi", "e", "tau"}:
            result = getattr(math, node.id)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            result = visit(node.operand, depth + 1) * (-1 if isinstance(node.op, ast.USub) else 1)
        elif isinstance(node, ast.BinOp) and type(node.op) in operations:
            left, right = visit(node.left, depth + 1), visit(node.right, depth + 1)
            if isinstance(node.op, ast.Pow) and abs(right) > 1000:
                raise CalculationError("Exponent must be between -1000 and 1000.")
            result = operations[type(node.op)](left, right)
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
              and node.func.id in functions and len(node.args) == 1 and not node.keywords):
            result = functions[node.func.id](visit(node.args[0], depth + 1))
        else:
            raise CalculationError("Use numbers, arithmetic, constants, and supported functions only.")
        if isinstance(result, complex) or not math.isfinite(result):
            raise CalculationError("Result must be a finite real number.")
        return float(result)

    try:
        return visit(tree.body)
    except CalculationError:
        raise
    except (ValueError, OverflowError, ZeroDivisionError, TypeError) as exc:
        raise CalculationError("Undefined calculation: check the domain or division by zero.") from exc
