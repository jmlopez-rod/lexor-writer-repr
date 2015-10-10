"""LEXOR: REPR Writer Style

This writing style reproduces the lexor builtin `Node` method
`__repr__`. Its goal is to provide you with the all the information
contained in a document.

"""
from lexor import init
from lexor.core.writer import NodeWriter
import lexor.core.elements as core

INFO = init(
    version=(0, 1, 0, 'final', 0),
    lang='lexor',
    type='writer',
    description='Reproduces the lexor builtin method `__repr__`.',
    git={
        'host': 'github',
        'user': 'jmlopez-rod',
        'repo': 'lexor-writer-repr'
    },
    author={
        'name': 'Manuel Lopez',
        'email': 'jmlopez.rod@gmail.com'
    },
    docs='http://jmlopez-rod.github.io/'
         'lexor-lang/lexor-writer-repr',
    license='BSD License',
    path=__file__
)
DEFAULTS = {
    'tab_form': '  ',
    'print_id': 'false',
    'print_pos': 'false',
}
TRUE = ['true', 'on', '1']


class DefaultNW(NodeWriter):
    """Writes the node name and its attributes. """

    def start(self, node):
        opt = self.writer.defaults
        tab = opt['tab_form']
        pid = opt['print_id'].lower() in TRUE
        pos = opt['print_pos'].lower() in TRUE
        indent = tab*node.level
        if node.name == '#document':
            indent = tab*(node.level+1)
        self.write('%s%s' % (indent, node.name))
        if pos:
            self.write('[%s:%s]' % node.node_position)
        if not isinstance(node, core.Element):
            if pid:
                self.write('[0x%x]' % id(node))
            self.write(':')
            return
        att = ' '.join(['%s="%s"' % (k, v) for k, v in node.items()])
        if pid:
            self.write('[0x%x' % id(node))
            if att != '':
                self.write(' %s]' % att)
            else:
                self.write(']')
        elif att != '':
            self.write('[%s]' % att)
        if node.name == '#document':
            msg = ': (%s:%s:%s)'
            self.write(msg % (node.uri, node.lang, node.style))
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
