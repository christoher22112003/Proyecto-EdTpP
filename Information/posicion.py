import pyautogui, sys
print("Precione ctrl + c para parar")
try:
  while True:
    x, y = pyautogui.position()
    positionStr = 'x =' + str(x).rjust(4) + ',y =' + str(y).rjust(4)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
  print('\n')