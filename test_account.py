from Account import Account
import unittest


class TestAccount(unittest.TestCase):

    def test_init(self):
        account1 = Account("John")
        self.assertEqual(account1.get_name(), "John")
        self.assertEqual(account1.get_balance(), 0)

    def test_deposit(self):
        account1 = Account("John")
        assert account1.deposit(-1) is False
        assert account1.deposit(0) is False
        account1.deposit(50)
        self.assertEqual(account1.get_balance(), 50)

    def test_withdraw(self):
        account1 = Account("John")
        assert account1.withdraw(-1) is False
        assert account1.withdraw(0) is False
        assert account1.withdraw(200) is False
        account1.deposit(200)
        account1.withdraw(100)
        self.assertEqual(account1.get_balance(), 100)


if __name__ == '__main__':
    unittest.main()
