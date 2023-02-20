from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple

import pytest


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int

    def __add__(self, other):
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency, self.value + other.value)

    def __sub__(self, other):
        if other.currency != self.currency:
            raise ValueError(f"Cannot substract {other.currency} from {self.currency}")
        return Money(self.currency, self.value - other.value)

    def __mul__(self, integer):
        if not isinstance(integer, int):
            raise ValueError(f"Cannot multiply {self.currency} by {integer}")
        return Money(self.currency, self.value * integer)


Line = namedtuple("Line", ["sku", "qty"])


fiver = Money("gbp", 5)
tenner = Money("gbp", 10)


def test_equality():
    assert Money("gbp", 10) == Money("gbp", 10)
    assert Name("Harry", "Percival") != Name("Bob", "Gregory")
    assert Line("RED-CHAIR", 5) == Line("RED-CHAIR", 5)


def tes_can_add_money_values_for_the_same_currency():
    assert fiver + fiver == tenner


def test_can_subtract_money_values():
    assert tenner - fiver == fiver


def test_adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money("usd", 10) + Money("gbp", 10)


def test_can_multiply_money_by_a_number():
    assert fiver * 5 == Money("gbp", 25)


def test_multiplying_two_money_values_is_an_error():
    with pytest.raises(ValueError):
        tenner * fiver
