
#% https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

from html.parser import HTMLParser
lista = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for x in range(len(attrs)):
            print(f"-> {attrs[x][0]} > {attrs[x][1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self,tag, attrs):
        print("Empty :", tag)
        for x in range(len(attrs)):
            print(f"-> {attrs[x][0]} > {attrs[x][1]}")

parser = MyHTMLParser()

for x in range(int(input())):
    text = input()
    parser.feed(text)
            
