
#% https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(data.lstrip())
        else: 
            print(">>> Single-line Comment")
            print(data.lstrip())
            
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)

  
  
  
  
html = ""
parser = MyHTMLParser()

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser.feed(html)
parser.close()
    