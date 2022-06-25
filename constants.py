import sys, os
sys.path.append(os.environ['raco'])
from common import *
r_ovshoot = 0.710
r_shear = 0.641
#r_bcz = rbcz_nond
r_bcz = 0.729
rvals_M = [r_shear, r_ovshoot, r_bcz]
linecolors = ['m', 'g', 'k']
linestyles = ['-.', ':', '--']


# slightly different values for case H
r_bcz_H = 0.726
r_ovshoot_H = 0.71