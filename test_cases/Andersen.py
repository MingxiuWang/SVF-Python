# Install the pysvf library
# You might need to run this command in your terminal or use a Jupyter magic command
# !pip install pysvf
import sys

# Import necessary libraries
import pysvf
# Load the LLVM bitcode file
bitcode_file = "array-constIdx.c.bc"

# Get the pag(SVFIR) from the bitcode file
pag = pysvf.get_pag(bitcode_file)

# Get the control flow graph (CFG) from the pag
cfg = pag.get_icfg()

ander_base = pysvf.AndersenBase(pag)
ander_base.initialize()
consCG = ander_base.get_constraint_graph()
ander_base.init_worklist()
wpa = pysvf.WPAPass()
wpa.run_on_module(pag)








