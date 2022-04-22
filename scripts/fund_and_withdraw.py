from brownie import FundMe
from scripts.helpful_scripts import get_account
import time


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee = {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee * 2})
    print("ok, wait for a while...")
    time.sleep(10)


def withdraw():
    print("enter withdraw function")
    fund_me = FundMe[-1]
    account = get_account()
    print(f"contract: {fund_me}, account: {account}")
    contract_balance = fund_me.getContractBalance()
    print(f"Contract Balance = {contract_balance}")
    print("Withdraw...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
