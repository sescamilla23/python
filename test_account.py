from account import *
import pytest


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == pytest.approx(0)

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.deposit(20.5) is True
        assert self.a1.get_balance() == pytest.approx(20.5)

    def test_withdraw(self):
        assert self.a1.withdraw(-2) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.withdraw(10) is False
        assert self.a1.get_balance() == pytest.approx(0)
        self.a1.deposit(10)
        assert self.a1.withdraw(5.5) is True
        assert self.a1.get_balance() == pytest.approx(4.5)

