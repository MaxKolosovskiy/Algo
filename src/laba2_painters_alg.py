def main_paint_time(K, T, L):

  painters = [0] * K

  if K < len(L):
    board_for_one_painter = len(L) // K
    remaining = len(L) % K
    start = 0
    for item in range(K):
      end = start + board_for_one_painter
      if remaining > 0:
        end += 1
        remaining -= 1

      painters[item] = sum(L[start:end]) * T
      start = end
  else:
    for i in range(len(L)):
       painters[i] = L[i] * T

  result = max(painters)

  return result