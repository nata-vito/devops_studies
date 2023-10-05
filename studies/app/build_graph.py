from pycfg.pycfg import PyCFG, CFGNode, slurp
import argparse

parser = argparse.ArgumentParser()
  
parser.add_argument('main.py', help ='The python file to be analyzed')
args = parser.parse_args()
arcs = []

cfg = PyCFG()
cfg.gen_cfg(slurp(args.pythonfile).strip())
g = CFGNode.to_graph(arcs)
g.draw(args.pythonfile + '.png', prog ='dot')