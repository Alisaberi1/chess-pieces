queen, king, rooks, bishops, knights, pawns =map(int,input().split(" "))
# make function with (queen , king),(pawns),(bishops,knights,rooks)
#rooks_knights_bishops==r_k_b
#king_queen==K_Q
def pawn(pawns):
  if pawns==8:return(0)
  else:return(8-pawns)
def K_Q(king):
  if king==1:return(0)
  else:return(king-1)
def r_k_b(rooks):
  if rooks==2:return(0)
  else:return(2-rooks)
print(K_Q(king),K_Q(queen),r_k_b(rooks),r_k_b(bishops),r_k_b(knights),pawn(pawns))
