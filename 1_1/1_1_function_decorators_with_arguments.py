#!/usr/bin/python
# Nicolae Erast, 20.04.2017

def tag(tag):
    def add2func(func):
        def new_func(text):
            o = ''
            if tag in ['h3','p']: # new line identing two spaces
                o += '\n  '
            o += '<' + tag + '>'
            if tag in ['html','body']: # new line
                o += '\n'
            o += func(text).lstrip()
            if tag in ['html','body']: # new line
                o += '\n'
            o += '</' + tag + '>'
            return o
        return new_func
    return add2func

def main():
    print 'Demo using function decorators with arguments'
    print 'To print raw text comment the decorator function\n'

    # date de intrare
    page_title = 'My web pag'
    body_title = 'My first web script'
    body_text1 = 'start: yesterday'
    body_text2 = 'end: today'
    # output
    html = ''

    # decorating page title
    @tag('title')
    def add(text):
        return '\n' + text # add '\n' if decorator is missing
    html += add(page_title)

    # add head
    @tag('head')
    def add(text):
        return text
    html = add(html)

    # decorating body title
    @tag('h3')
    def add(text):
        return '\n' + text
    html += add(body_title)

    # decorating body text
    @tag('p')
    def add(text):
        return '\n' + text
    html += add(body_text1)
    html += add(body_text2)

    # add body
    @tag('body')
    def add(text):
        return text
    html = add(html)

    # add html
    @tag('html')
    def add(text):
        return text
    html = add(html)

    print html

    raw_input("\nPress any key to exit!")

if __name__ == "__main__":
    main()