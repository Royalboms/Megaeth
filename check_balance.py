from web3 import Web3
from eth_account import Account
from config import config
from utils.utils import show_balance, check_connection
from dotenv import load_dotenv
import os

load_dotenv()

if not os.path.exists("wallets.txt"):
    print("Không tìm thấy file wallets.txt! Hãy tạo file này và điền mỗi private key trên 1 dòng.")
    exit(1)

with open("wallets.txt") as f:
    private_keys = [line.strip() for line in f if line.strip()]

for idx, PRIVATE_KEY in enumerate(private_keys):
    print(f"\n=============================")
    print(f"=== ĐANG CHECK VÍ SỐ {idx+1}: ...{PRIVATE_KEY[-6:]} ===")
    print(f"=============================")
    account = Account.from_key('0x' + PRIVATE_KEY)
    address = account.address
    web3 = Web3(Web3.HTTPProvider(config.RPC_URL))
    if not check_connection(web3):
        continue
    for token in config.GTE_TOKENS.keys():
        show_balance(address, web3, token=token)