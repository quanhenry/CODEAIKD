import subprocess
import os

# Danh sách các file cần chạy
files_to_run = [
    "b1.py",
    "b2.py",
    "b3.py",
    "b4.py"
    # "b5.py",
    # "b6.py",
    # "alayanh.py",
    # "laylinkvatenfile.py",
    # "b7.py"
    # # "b8.py",
    # # "b9.py"
]

def run_python_file(file_name):
    try:
        print(f"Đang chạy {file_name}...")
        result = subprocess.run(["python", file_name], check=True, capture_output=True, text=True)
        print(f"{file_name} đã chạy thành công.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy {file_name}:")
        print(e.stderr)

def main():
    for file in files_to_run:
        if os.path.exists(file):
            run_python_file(file)
        else:
            print(f"Không tìm thấy file {file}")
    
    print("Đã chạy xong tất cả các file.")

if __name__ == "__main__":
    main()