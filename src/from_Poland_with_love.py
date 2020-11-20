from sys import argv
from ioInterfaces import ConsoleIOI, WindowIOI

appModes = dict(
  console = ConsoleIOI,
  window = WindowIOI
)

# [LUANCHING]
if len(argv) > 1:
  mode = argv[1]
  appModes[mode]().launch()
else:
  appModes["console"]().launch()
