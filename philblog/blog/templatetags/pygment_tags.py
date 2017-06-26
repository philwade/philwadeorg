from django import template
from django.template.defaultfilters import stringfilter
from bs4 import BeautifulSoup
import pygments
import pygments.lexers as lexers
import pygments.formatters as formatters
import html.parser

register = template.Library()
html_parser = html.parser.HTMLParser()

@register.filter(name='pygmentize')
@stringfilter
def pygmentize(value):
    try:
        my_formatter = formatters.HtmlFormatter(style='trac')
        my_tree = BeautifulSoup(value, "html.parser")
        for code_block in my_tree.findAll('code'):
            if not code_block['class']:
                language = 'text'
            else:
                language = code_block['class'].pop(0)
            my_lexer = lexers.get_lexer_by_name(language)
            new_content = pygments.highlight(code_block.text, my_lexer, my_formatter)
            if str(code_block.text).find("&") > -1:
                raise Exception('ok')
            new_content += u"<style>%s</style>" % my_formatter.get_style_defs('.highlight')
            code_block.replaceWith ( "%s\n" % new_content )
        my_content = html_parser.unescape(str(my_tree))
        return my_content
    except KeyError:
      return value
