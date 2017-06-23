from django import template
from bs4 import BeautifulSoup
import pygments
import pygments.lexers as lexers
import pygments.formatters as formatters
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='pygmentize')
def pygmentize(value):
    try:
        my_formatter = formatters.HtmlFormatter(style='trac')
        my_tree = BeautifulSoup(value)
        for code_block in my_tree.findAll('code'):
            if not code_block['class']:
                language = 'text'
            else:
                language = code_block['class'].pop(0)
            my_lexer = lexers.get_lexer_by_name(language)
            new_content = pygments.highlight(code_block.text, my_lexer, my_formatter)
            new_content += u"<style>%s</style>" % my_formatter.get_style_defs('.highlight')
            code_block.replaceWith ( "%s\n" % new_content )
        my_content = str(my_tree)
        return mark_safe(my_content)
    except KeyError:
      return value
