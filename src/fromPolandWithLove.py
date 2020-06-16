from sys import argv
from ConsoleIOI import ConsoleIOI
from WindowIOI import WindowIOI

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
