
# Try to import all dependencies, catch and handle the error gracefully if it fails.

import import_lldb

try:
  import lldb
  import vim
except ImportError:
  pass
else:
  # Everthing went well, so use import to start the plugin controller 
  from lldb_controller import *
  vim.command("let l:python_plugin_initialized = 1")
