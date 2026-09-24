import sys
from checkmate import checkmate

def main():
    # ตรวจสอบว่ามีการส่งไฟล์แนบมาทาง Arguments หรือไม่
    if len(sys.argv) < 2:
        print("Error")
        return
        
    # วนลูปอ่านทุกๆ ไฟล์ที่ส่งเข้ามา
    for file_path in sys.argv[1:]:
        try:
            with open(file_path, 'r') as f:
                board = f.read()
                checkmate(board)
        except Exception:
            # หากไฟล์พัง หรืออ่านไม่ได้
            print("Error")

if __name__ == "__main__":
    main()