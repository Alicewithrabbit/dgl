"""Module for base types and utilities."""
from __future__ import absolute_import

import warnings

from ._ffi.base import DGLError  # pylint: disable=unused-import
from ._ffi.function import _init_internal_api

# A special symbol for selecting all nodes or edges.
ALL = "__ALL__"
# An alias for [:]
SLICE_FULL = slice(None, None, None)
# Reserved column names for storing parent node/edge types and IDs in flattened heterographs
NTYPE = '_TYPE'
NID = '_ID'
ETYPE = '_TYPE'
EID = '_ID'

def is_all(arg):
    """Return true if the argument is a special symbol for all nodes or edges."""
    return isinstance(arg, str) and arg == ALL

# pylint: disable=unused-argument
def dgl_warning_format(message, category, filename, lineno, file=None, line=None):
    """Format DGL warnings."""
    return "DGL Warning: {}\n".format(message)

warnings.formatwarning = dgl_warning_format
dgl_warning = warnings.warn  # pylint: disable=invalid-name

_init_internal_api()
