import time




def bubble_sort(data, drawData, timeTick):
  for _ in range(len(data)-1):
    for i in range(len(data)-1):
      if data[i] > data [i+1]:
        data[i] , data [i+1] = data [i+1] , data[i]
        drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    
  drawData(data, ['green' for x in range(len(data))])

  return data

