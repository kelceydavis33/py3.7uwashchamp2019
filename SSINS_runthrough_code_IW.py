# This is a run through of RFI analysis using SSINS Tutorial and uvfits files
# Written in python3 by Imani Ware, from SSINS created by Michael J. Wilensky

# import SSINS objects, matplotlib, numpy, and necessary inputs
from SSINS import SS
from SSINS import INS
import os

# Create an SS object and read in uvfits file
ss = SS()
uvfits_file = '/Volumes/Faramir/uvfits/1061313128.uvfits'
ss.read(uvfits_file, ant_str = 'cross')


#apply flags to SS data
ss.apply_flags(flag_choice = 'original')

# Make a VDH plot
# import Catalog_Plot from SSINS
from SSINS import Catalog_Plot as cp 


# set a file prefix for plot
prefix = 'tutorial_outputs/IW_SSINS_runs_'

# Pre-flagged and Post-flagged
cp.VDH_plot(ss, prefix, file_ext = 'pdf', xlabel='Visibility Differences', xscale='log', yscale='log', legend=True, ylim=None, density=False, pre_flag=True, post_flag=True, pre_model=True, post_model=True, pre_label='Pre flagging', post_label='Post flagging', pre_model_label= 'Pre Model', post_model_label='Post Model', pre_model_color='green', post_model_color='yellow', pre_color='red', post_color='blue', font_size='medium')


# Create an INS object and use uvfits file
ins =INS(ss)

# Make a INS plot
# Pre-flagged and Post-flagged
cp.INS_plot(ins, prefix, file_ext='.pdf')


