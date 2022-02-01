nth last pointer = None
tail pointer = linked list head
count = 1

while tail pointer exists
  move tail pointer forward
  increment count

  if count >= n + 1
    if nth last pointer is None
      set nth last pointer to head
    else
      move nth last pointer forward

return nth last pointer