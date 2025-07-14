# MegaEth GTE Automation

---

## Tính năng
- **Auto Swap**: Tự động swap qua lại nhiều token 
- **Balance Tracking**: Kiểm tra số dư
- **Chạy 1 lần hoặc chạy mãi mãi**: Nếu chạy 24/24 không muốn treo pc thì deploy lên VPS qua SSH
- **Multi Wallet**: Chạy được nhiều ví

---

## Yêu cầu

- **Python 3.8+**: Cần thiết để chạy bot.
- **pip**: Trình quản lý gói Python để cài đặt các phụ thuộc.
- **Ví Ethereum**: Một ví với:
  - MegaEth testnet ETH cho phí gas.
---

## Cài đặt

### 1. Download Repository
Tải Repo này về rồi giải nén mở lên bằng VSC hoặc Cursor

```

### 2. Cài đặt Phụ thuộc
Cài đặt các gói Python cần thiết được liệt kê trong `requirements.txt`:

Có thể chạy lệnh dưới đây:

```bash
pip install -r requirements.txt
```



### 4. Thêm file .env để chứa ví

Set up key trong file wallet.txt nhé

- **PRIVATE_KEY**: Private key của ví Ethereum cho testnet MegaEth (không có đầu `0x`) nhớ kỹ
  ```wallet.txt
  Mỗi dòng 1 key nhé
  ```

---


### 1. Start
Đảm bảo ví có:
- Đủ MegaEth testnet ETH cho phí gas.

### 2. Khởi động Bot
Chạy bot với lệnh:

```bash
python main.py
```

### 3. Chọn option (khuyên dùng auto cho khỏe)
- **Chọn Chế độ Thực hiện**:
  - `once`: Chạy hoán đổi một lần và thoát.
  - `auto`: Chạy hoán đổi hàng ngày (yêu cầu VPS để hoạt động liên tục).
- **Số lượng chu kỳ swap**: Nhập số chu kỳ hoán đổi để thực hiện.
- **Số lượng muốn swap**: Chỉ định phần trăm số dư token để hoán đổi (1–100).

## 🎓 **Nhóm của mình các bạn có thể follow để cập nhật các script mới nhất**

Link: [Velhust House](https://t.me/velhustdev)

---

## ☕ ỦNG HỘ MÌNH CỐC CF NẾU BẠN THÍCH SCRIPT NÀY

- **EVM:** 0x70A5a4ede89ED613307d255659a1dD837D9418a1
- **SOL:** AwXQn61FFabdV4iDjzCNTHtx2yanGDiEEh7KY4MKVZS2
- **SUI:** 0xc99395ead375fe240f0edd28acb12e3360ffe1e83bbd1d782b3208fc57fe338c

— **</velhust/>**
