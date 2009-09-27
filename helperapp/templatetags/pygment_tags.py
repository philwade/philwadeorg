from django import template
from BeautifulSoup import BeautifulSoup
import re
import pygments
import pygments.lexers as lexers
import pygments.formatters as formatters
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter(name='pygmentize')
def pygmentize(value):
    try:
        formatter = HtmlFormatter(style='trac')
        tree = BeautifulSoup(value)
        for code in tree.findAll('code'): 
            if not code['class']: code['class'] = 'text'
            lexer = lexers.get_lexer_by_name(code['class'])
            new_content = pygments.highlight(code.contents[0], lexer, formatter)
            new_content += u"<style>%s</style>" % formatter.get_style_defs('.highlight')
            code.replaceWith ( "%s\n" % new_content )
        content = str(tree)
        return content
    except KeyError:
      return value
