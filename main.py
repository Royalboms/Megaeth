from web3 import Web3
from utils.utils import check_connection
from utils.utils import is_valid_address
from display import loging
from utils.utils import show_balance
from eth_account import Account
from config import config
from utils.utils import swap
from utils.utils import check_token_balance
from utils.utils import wait_until_next_day
from dotenv import load_dotenv
from display import appearance
import os

load_dotenv()

def main(PRIVATE_KEY, swap_type, swap_count, swap_percent):
    print(appearance.ASCII_ART)
    print(appearance.CREDIT)
    
    account = Account.from_key('0x' + PRIVATE_KEY)
    address = account.address
    web3 = Web3(Web3.HTTPProvider(config.RPC_URL))
    router = web3.eth.contract(address=config.ROUTER_ADDRESS, abi=config.ROUTER_ABI)
    
    loging.log_info(f"Địa chỉ ví: {address}")  

    if not check_connection(web3):
        return

    print("\n=== KIỂM TRA SỐ DƯ ===")
    print("-" * 50)
    for token in config.GTE_TOKENS.keys():
        show_balance(address, web3, token=token)
    print("-" * 50)
    
    # Chỉ chạy swap_count lần, không chờ ngày hôm sau
    for i in range(swap_count):
        for item in config.GTE_TOKENS.keys():
            if item == "ETH":
                continue
            else:
                amt = check_token_balance(address, web3)
                swap(web3, account, router, config.BASE_TOKEN, item, amt * swap_percent)
                
        loging.log_info("Swap lại về eth")
        
        for item in config.GTE_TOKENS.keys():
            if item == "ETH":
                continue
            else:
                amt = check_token_balance(address, web3, item)
                swap(web3, account, router, item, config.BASE_TOKEN, amt )
                
        loging.log_success(f"Swap {i+1} hoàn tất.")
                
        loging.log_info("\n=== KIỂM TRA SỐ DƯ ===")
        print("-" * 50)
        for token in config.GTE_TOKENS.keys():
            show_balance(address, web3, token=token)
        print("-" * 50)
        loging.log_info("Đang chờ swap tiếp theo...")
    
    loging.log_info("Swap hoàn tất cho ví này.")
        

if __name__ == "__main__":
    try:
        # Đọc danh sách private key từ file wallets.txt
        if not os.path.exists("wallets.txt"):
            print("Không tìm thấy file wallets.txt! Hãy tạo file này và điền mỗi private key trên 1 dòng.")
            exit(1)
        with open("wallets.txt") as f:
            private_keys = [line.strip() for line in f if line.strip()]

        # Hỏi thông tin 1 lần duy nhất
        while True:
            swap_method = input("Bạn muốn chạy swap tự động hoặc một lần? (auto/once): ").strip().lower()
            if swap_method in ["auto", "once"]:
                swap_type = swap_method == "auto"
                break
            else:
                print("❌ Lỗi. Vui lòng nhập 'auto' hoặc 'once'.")
        while True:
            try:
                swap_count = int(input("Bạn muốn swap bao nhiêu lần? : "))
                break
            except ValueError:
                print("Lỗi. Vui lòng nhập số.")
        while True:
            try:
                swap_percent = float(input("Bạn muốn swap bao nhiêu phần trăm? (1-100): "))
                swap_percent = swap_percent / 100
                break
            except ValueError:
                print("Lỗi. Vui lòng nhập số.")

        # Vòng lặp chính cho auto mode
        while True:
            # Chạy lần lượt cho từng ví
            for idx, PRIVATE_KEY in enumerate(private_keys):
                print(f"\n=============================")
                print(f"=== ĐANG CHẠY VÍ SỐ {idx+1}: ...{PRIVATE_KEY[-6:]} ===")
                print(f"=============================")
                try:
                    main(PRIVATE_KEY, swap_type, swap_count, swap_percent)
                except Exception as e:
                    loging.log_warning(f"Lỗi với ví ...{PRIVATE_KEY[-6:]}: {e}")
            
            # Nếu chọn auto, chờ đến ngày hôm sau rồi lặp lại
            if swap_type:
                loging.log_info("Đã hoàn thành tất cả các ví. Đang chờ đến ngày hôm sau...")
                wait_until_next_day()
                continue
            else:
                loging.log_info("Đã hoàn thành tất cả các ví.")
                break
                
    except KeyboardInterrupt:
        loging.log_warning("Chương trình kết thúc.")


