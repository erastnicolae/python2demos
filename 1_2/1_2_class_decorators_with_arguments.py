#!/usr/bin/python
# Nicolae Erast - 20.04.2017

class tag(object):
    def __init__(self,tag):
        self.tag = tag

    def __call__(self,func):
        def new_func(text):
            o = ''
            # trec la linie noua si indentez 2 spatii
            if self.tag in ['h3','p']: 
                o += '\n  '
            o += '<' + self.tag + '>'
            if self.tag in ['html','body']: # trec la linie noua
                o += '\n'
            # cu lstrip() scap de terminator in cazul se tipareste prin decorator
            o += func(text).lstrip()
            if self.tag in ['html','body']: # trec la linie noua
                o += '\n'
            o += '</' + self.tag + '>'
            return o
        return new_func
        
def main():
    print 'Demo using class decorators with arguments'
    print 'Comment decorators for raw printing'

    # input data
    page_title = 'My web page'
    body_title = 'My first web script'
    body_text1 = 'start: yesterday'
    body_text2 = 'end: today'
    # output
    html = ''

    # decorate page title
    @tag('title')
    def add(text):
        # add '\n' if decorator is commented
        return '\n' + text
    html += add(page_title)

    # decorate head
    @tag('head')
    def add(text):
        return text
    html = add(html)

    # decorate page title
    @tag('h3')
    def add(text):
        return '\n' + text
    html += add(body_title)

    #d decorate body title
    @tag('p')
    def add(text):
        return '\n' + text
    html += add(body_text1)
    html += add(body_text2)

    # decorate body
    @tag('body')
    def add(text):
        return text
    html = add(html)

    # decorate html tag
    @tag('html')
    def add(text):
        return text
    html = add(html)

    print html

    raw_input("\nPress any key to exit!")

if __name__ == "__main__":
    main()