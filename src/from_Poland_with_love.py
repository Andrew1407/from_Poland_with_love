from sys import argv
from ioInterfaces import *

appModes = dict(
  console = ConsoleIOI,
  window = WindowIOI
)

# [LAUNCHING]
if len(argv) > 1:
  mode = argv[1]
  appModes[mode]().launch()
else:
  appModes["console"]().launch()
