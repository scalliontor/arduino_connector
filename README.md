### Bước 1: Cài Đặt Môi Trường

**1. Cài đặt thư viện `pyserial` của Python:**

Tạo tệp `requirements.txt` với nội dung `pyserial` và chạy lệnh sau:

```bash
pip install -r requirements.txt
```

**2. Cài đặt Arduino CLI:**


```bash
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh


sudo mv bin/arduino-cli /usr/local/bin/

arduino-cli config init

arduino-cli core update-index

# Cài đặt gói lõi cho các bo mạch Arduino AVR (như Uno, Nano, Mega)
arduino-cli core install arduino:avr
```

Để kiểm tra cài đặt thành công, chạy:
```bash
arduino-cli version
```
Bạn sẽ thấy phiên bản của Arduino CLI được hiển thị.

2.  **Biên dịch và Nạp mã bằng Arduino CLI:**
    
    Đầu tiên, bạn cần cấp quyền truy cập vào cổng serial:
    ```bash
    # Thêm người dùng hiện tại vào nhóm 'dialout'
    sudo usermod -a -G dialout $USER
    ```
    **LƯU Ý:** Bạn cần **đăng xuất và đăng nhập lại** hoặc **khởi động lại máy tính** để thay đổi này có hiệu lực.
    
    Sau đó, chạy các lệnh sau từ thư mục chứa thư mục `receiver`:

    ```bash
    # Biên dịch mã nguồn cho bo Arduino Uno
    arduino-cli compile --fqbn arduino:avr:uno receiver/

    # Nạp mã vào Arduino (thay thế /dev/ttyACM0 nếu cổng của bạn khác)
    arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno receiver/
    ```

### Bước 2: Chạy Chương Trình Python

1.  **Tìm Cổng Nối Tiếp:** Chạy kịch bản `find_serial_port.py` để xác định chính xác cổng mà Arduino đang kết nối.

    ```bash
    python3 find_serial_port.py
    ```
    Ghi lại tên cổng (ví dụ: `/dev/ttyACM0`).

2.  **Cấu hình Kịch bản Gửi Lệnh:**
    Mở tệp `sender.py` và đảm bảo giá trị của biến `arduino_port` là chính xác.

    ```python
    # Thay thế bằng cổng nối tiếp của Arduino của bạn.
    arduino_port = '/dev/ttyACM0' 
    ```

3.  **Chạy Kịch bản Điều Khiển:**
    Bây giờ, hãy chạy tệp `sender.py`:

    ```bash
    python3 sender.py
    ```

4.  **Điều khiển đèn LED:**
    Chương trình sẽ yêu cầu bạn nhập lệnh. Nhập `1` và nhấn Enter để bật đèn LED, hoặc nhập `0` và nhấn Enter để tắt đèn. Đèn LED trên bo mạch sẽ phản hồi theo lệnh của bạn. Nhấn `Ctrl+C` để thoát chương trình.
