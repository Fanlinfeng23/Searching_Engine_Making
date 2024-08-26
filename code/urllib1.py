import urllib.request

#send a basic request to Baidu

def load_baidu_data():
  url='https://www.baidu.com'
  response = urllib.request.urlopen(url)
  print(response.code)
  #If is code returned is 200, it means you requested successfully.
  
  #read the data and decode the data
  data=response.read()
  str_data=data.decode('utf-8')
  print(str_data)
  
  #write the data you got into a file.
  with open("baidu.html","w", encoding='utf-8') as f:
    f.write(str_data)
load_baidu_data()



