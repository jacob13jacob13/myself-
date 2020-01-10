def almostIncreasingSequence(seq):
  prev = seq[0]
  counter = 0
  for i in range(1, len(seq)):
    if seq[i] <= prev:
      counter += 1
      if counter > 1:
        return False
      if (i < 2) or (seq[i-2] < seq[i]):
        prev = seq[i]
    else:
      prev = seq[i]
  return True
