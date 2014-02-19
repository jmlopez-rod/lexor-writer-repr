"""LEXOR: REPR Writer Style

This writing style reproduces the lexor builtin `Node` method
`__repr__`. Its goal is to provide you with the all the information
contained in a document.

"""

from lexor import init
from lexor.core.writer import NodeWriter
import lexor.core.elements as core

INFO = init(
    version=(0, 0, 1, 'final', 1),
    lang='lexor',
    type='writer',
    description='Reproduces the lexor builtin method `__repr__`.',
    url='http://jmlopez-rod.github.io/lexor-lang/lexor-writer-repr',
    author='Manuel Lopez',
    author_email='jmlopez.rod@gmail.com',
    license='BSD License',
    path=__file__
)
DEFAULTS = {
    'tab_form': '    ',
    'print_id': 'false',
}


class DefaultNW(NodeWriter):
    """Writes the node name and its attributes. """

    def start(self, node):
        tab = self.writer.defaults['tab_form']
        pid = self.writer.defaults['print_id']
        indent = tab*node.level
        if node.name == '#document':
            indent = tab*(node.level+1)
        self.write('%s%s' % (indent, node.name))
        if not isinstance(node, core.Element):
            if pid.lower() == 'true':
                self.write('[0x%x]' % id(node))
            self.write(':')
            return
        att = ' '.join(['%s="%s"' % (k, v) for k, v in node.items()])
        if pid.lower() == 'true':
            self.write('[0x%x' % id(node))
            if att != '':
                self.write(' %s]' % att)
            else:
                self.write(']')
        elif att != '':
            self.write('[%s]' % att)
        if node.name == '#document':
            self.write(': (%s:%s:%s)' % (node.uri, node.lang, node.style))
        else:
            self.write(':')
        if not isinstance(node, core.CharacterData):
            self.write('\n')

    def data(self, node):
        self.write(' %r\n' % node.data)


MAPPING = {
    '__default__': DefaultNW,
    '#document': '__default__',
    '#text': '__default__',
    '#entity': '__default__',
}
