"""YANG Metadata plugin

Verifies YANG metadata statements as defined in
draft-ietf-netmod-yang-metadata-01, with the exception that
it requires a 'type' substatement to 'annotation', and restricts
the name of the annotation to 'identifier'.

Verifies the grammar of the annotation extension statement.
"""

import pyang
from pyang import plugin
from pyang import grammar

md_module_name = 'ietf-yang-metadata'

class MetadataPlugin(plugin.PyangPlugin):
    pass

def pyang_plugin_init():
    """Called by pyang plugin framework at to initialize the plugin."""

    # Register the plugin
    plugin.register_plugin(MetadataPlugin())

    # Register that we handle extensions from the module 'ietf-yang-metadata'
    grammar.register_extension_module(md_module_name)

    # Register the special grammar
    for (stmt, occurance, (arg, rules), add_to_stmts) in md_stmts:
        grammar.add_stmt((md_module_name, stmt), (arg, rules))
        grammar.add_to_stmts_rules(add_to_stmts,
                                   [((md_module_name, stmt), occurance)])

md_stmts = [

    # (<keyword>, <occurance when used>,
    #  (<argument type name | None>, <substmts>),
    #  <list of keywords where <keyword> can occur>)

    ('annotation', '*',
     ('identifier', [('if-feature', '*'),
                     ('type', '1'),
                     ('units', '?'),
                     ('status', '?'),
                     ('description', '?'),
                     ('reference', '?')]),
     ['module', 'submodule']),
]
