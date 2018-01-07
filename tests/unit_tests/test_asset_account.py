import unittest
from unittest.mock import Mock

from budget.account import AssetAccount
from budget.transaction import Transaction


class TestAssetAccount(unittest.TestCase):
    def setUp(self):
        self.blank_asset_account = AssetAccount()
        self.amazon_account = AssetAccount(name='Amazon')
        self.simple_asset = Mock(spec_set=Transaction())
        self.simple_asset.total_value = 150.0

    def test_asset_accounts_should_have_default_name_uncategorized(self):
        self.assertEqual('UncategorizedAssetAccount', self.blank_asset_account.name)

    def test_asset_account_can_initialize_name_in_constructor(self):
        expected_name = 'Savings'
        account = AssetAccount(name=expected_name)
        self.assertEqual(expected_name, account.name)

    def test_asset_account_can_return_total_assets(self):
        self.amazon_account.add_transaction(self.simple_asset)
        self.amazon_account.add_transaction(self.simple_asset)
        self.assertEqual(300.0, self.amazon_account.total_deposits)
