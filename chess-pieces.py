normal_king=normal_queen=1
normal_knight=normal_bishop=normal_rook=2
normal_pawn=8
king,queen,knight,bishop,rook,pawn=map(int,input().split())
print(normal_king - king, normal_queen - queen,normal_knight - knight,
      normal_bishop - bishop,normal_rook - rook , normal_pawn - pawn)