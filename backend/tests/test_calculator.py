import math

import pytest

from app.calculator import CalculationError, calculate


@pytest.mark.parametrize("expression,expected", [
    ("2 + 3 * 4", 14), ("(2 + 3) * 4", 20), ("2^3^2", 512),
    ("-2^2", -4), ("sqrt(144)", 12), ("ln(e)", 1), ("log(1000)", 3),
    ("sin(pi/2)", 1), ("cos(pi)", -1), ("factorial(5)", 120),
    ("abs(-7) + floor(2.9)", 9), ("ceil(2.1)", 3), ("10 % 3", 1),
    ("2 × 3 + 8 ÷ 4", 8), ("π", math.pi), ("tau", math.tau),
    ("exp(0)", 1), ("atan(1)", math.pi/4), ("factorial(170)", float(math.factorial(170))),
])
def test_scientific_operations(expression, expected):
    assert calculate(expression) == pytest.approx(expected)


@pytest.mark.parametrize("expression,expected", [("sin(30)", .5), ("cos(60)", .5),
    ("tan(45)", 1), ("asin(0.5)", 30), ("acos(0.5)", 60), ("atan(1)", 45)])
def test_degrees(expression, expected):
    assert calculate(expression, "deg") == pytest.approx(expected)


@pytest.mark.parametrize("expression", [
    "", "   ", "1/0", "sqrt(-1)", "ln(0)", "(-1)^0.5", "1e309",
    "2^1001", "factorial(171)", "factorial(1.5)", "factorial(-1)",
    "__import__('os')", "(1).__class__", "[1,2]", "True", "sum(1)",
    "sqrt(x=4)", "sin(1, 2)", "lambda: 1", "1;2", "'hello'", "2(3)",
    "1+" * 130, "+" * 40 + "1", "1e308 * 10", "2 ** (2 ** 100)",
])
def test_rejects_unsafe_or_undefined_expressions(expression):
    with pytest.raises(CalculationError):
        calculate(expression)


def test_undefined_tangent_and_angle_mode():
    with pytest.raises(CalculationError):
        calculate("tan(90)", "deg")
    with pytest.raises(CalculationError):
        calculate("1", "grads")
