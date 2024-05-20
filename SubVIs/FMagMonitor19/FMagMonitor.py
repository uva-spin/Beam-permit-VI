import xmlrpc.client
import time

def getFMagCurrent(maxFailCount = 5):
  url = 'https://www-bd.fnal.gov/xmlrpc/Accelerator'
  nFailed = 0

  while True:
    if nFailed >= maxFailCount:
      return 9999
    
    try:
      server = xmlrpc.client.Server(url)
      res = server.getReading('F:NM3S')
    except:
      time.sleep(15)
      nFailed = nFailed + 1
      continue

    try:
      if not ('name' in res and 'scaled' in res):
        time.sleep(15)
        nFailed = nFailed + 1
        continue

      if res['name'] != 'F:NM3S':
        time.sleep(15)
        nFailed = nFailed + 1
        continue

      if not isinstance(res['scaled'], float):
        time.sleep(15)
        nFailed = nFailed + 1
        continue

    except:
      time.sleep(15)
      nFailed = nFailed + 1
      continue

    return res['scaled']

print(getFMagCurrent())