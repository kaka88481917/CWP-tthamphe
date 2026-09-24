def checkmate(board: str):
    try:
        if not isinstance(board, str) or not board.strip():
            print("Error")
            return
            
        # แยกแถวและลบช่องว่าง/บรรทัดว่างส่วนเกินออก
        rows = board.strip('\n').split('\n')
        size = len(rows)
        
        # ตรวจสอบว่ากระดานเป็นรูปสี่เหลี่ยมจัตุรัสตามกฎ
        for row in rows:
            if len(row) != size:
                print("Error")
                return
                
        king_pos = None
        # ตัวอักษรที่ไม่ใช่ P, B, R, Q, K จะถือเป็นช่องว่างทั้งหมด
        pieces = {'K', 'Q', 'R', 'B', 'P'}
        
        # ค้นหาตำแหน่งของ King
        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    if king_pos is not None:
                        # มี King มากกว่า 1 ตัว
                        print("Error")
                        return
                    king_pos = (r, c)
                    
        if king_pos is None:
            # ไม่พบ King
            print("Error")
            return
            
        kr, kc = king_pos
        
        # ฟังก์ชันเช็คว่ามีสิ่งกีดขวางในเส้นทางเดินหรือไม่ (ตัวหมากแรกที่ขวางจะรับการโจมตีไป)
        def is_path_clear(r1, c1, r2, c2):
            dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
            dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
            
            curr_r, curr_c = r1 + dr, c1 + dc
            while (curr_r, curr_c) != (r2, c2):
                if rows[curr_r][curr_c] in pieces:
                    return False
                curr_r += dr
                curr_c += dc
            return True

        # ตรวจสอบหมากศัตรูทุกตัวบนกระดานว่าสามารถโจมตี King ได้หรือไม่
        for r in range(size):
            for c in range(size):
                char = rows[r][c]
                if char not in pieces or char == 'K':
                    continue
                    
                # Pawn (P): กินเฉียงไปด้านหน้า 1 ช่อง
                if char == 'P':
                    if kr == r - 1 and abs(kc - c) == 1:
                        print("Success")
                        return
                        
                # Rook (R): เดินตรงแนวตั้งและแนวนอน
                elif char == 'R':
                    if r == kr or c == kc:
                        if is_path_clear(r, c, kr, kc):
                            print("Success")
                            return
                            
                # Bishop (B): เดินแนวทแยง
                elif char == 'B':
                    if abs(r - kr) == abs(c - kc):
                        if is_path_clear(r, c, kr, kc):
                            print("Success")
                            return
                            
                # Queen (Q): เดินได้ทั้งแนวตรงและแนวทแยง (Rook + Bishop)
                elif char == 'Q':
                    if (r == kr or c == kc) or (abs(r - kr) == abs(c - kc)):
                        if is_path_clear(r, c, kr, kc):
                            print("Success")
                            return
                            
        # หากไม่มีหมากตัวไหนกิน King ได้
        print("Fail")
        
    except Exception:
        # ป้องกันโปรแกรมแครชกรณีเจอ Undefined behavior
        print("Error")