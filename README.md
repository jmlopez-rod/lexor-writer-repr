Lexor Language: Lexor repr style writer
=======================================

This writing style reproduces the lexor builtin `Node` method
`__repr__`. Its goal is to provide you with the all the information
contained in a document.

## Installation

For a local installation 

    $ lexor install lexor.writer.repr

If there is a problem with the registry you may try a more direct
approach

    $ lexor install git+https://github.com/jmlopez-rod/lexor-writer-repr

You may use the `-u` option to install in the python user-site
directory or `-g` for a global installation (requires sudo rights).

If you have a `lexor.config` file in place you may also want to use
the `--save` option so that the dependency gets saved.

## Command line usage

Without document conversion

    $ lexor filename.ext to lexor~repr~

Converting to another language and writing it with this style

    $ lexor filename.ext to lang[cstyle:lexor.repr]


## Options

We may configure this style by providing any of the following
options:

- `tab_form`: A string specifying what to use to display a tab.
              Defaults to two spaces.
- `print_id`: Whether to display the id assigned to the node.
              Defaults to `'false'`.
- `print_pos`: Whether to display the position (line and column) of
               the node within the document. Defaults to `'false'`.

You may override these options in the command line by appending
`@option=value` after the style name. For instance

    lexor filename.ext to lexor~repr@print_id=true@print_pos=true~

## Example

Suppose we have the html file `example.html` with the following
content

```html
<html>
  <body>
    <p>Hello World</p>
  </body>
</html>
```

We can use this style to make sure that the html parser works
correctly

```console
$ lexor example.html to lexor~repr~
#document: (example.html:html:default)
html:
  #text: '\n  '
  body:
    #text: '\n    '
    p:
      #text: 'Hello World'
    #text: '\n  '
  #text: '\n'
#text: '\n'
```


To make sure that each node is being read properly we can print the
code position

```console
$ lexor example.html to lexor~repr@print_pos=true~
#document[0:0]: (example.html:html:default)
html[1:1]:
  #text[1:7]: '\n  '
  body[2:3]:
    #text[2:9]: '\n    '
    p[3:5]:
      #text[3:8]: 'Hello World'
    #text[3:23]: '\n  '
  #text[4:10]: '\n'
#text[5:8]: '\n'
```
