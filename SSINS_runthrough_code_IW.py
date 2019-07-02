# This is a run through of RFI analysis using SSINS Tutorial and uvfits files
# Written in python3 by Imani Ware, from SSINS created by Michael J. Wilensky

#To nuse another file from shrivelfig, use this command to download the file: rsync -alPvz imaniware@b027-ws01.phys.washington.edu:/Volumes/Faramir/uvfits/1061313128.uvfits .

# import SSINS objects, matplotlib, numpy, and necessary inputs
from SSINS import SS
# from pyuvdata import version
# print(version.version)
from SSINS import INS
import numpy as np 
import matplotlib as plt
import os

# Create an SS object and read in uvfits file
ss = SS()

uvfits_filename = str(input("Enter the .uvfits file you would like to use: "))
uvfits_file = '/Users/imaniware/Desktop/CHAMP/hera_uvfits/' + uvfits_filename

ss.read(uvfits_file, ant_str = 'cross')

#apply flags to SS data
ss.apply_flags(flag_choice = 'INS')

# Make a VDH plot
# import Catalog_Plot from SSINS
from SSINS import Catalog_Plot as cp 


# set a file prefix for plot
prefix = 'tutorial_outputs/IW_plot_1.1_' + uvfits_filename

# Pre-flagged and Post-flagged
cp.VDH_plot(ss, prefix, file_ext = 'pdf', xlabel='Visibility Differences', xscale='log', yscale='log', legend=True, ylim=None, density=False, pre_flag=True, post_flag=True, pre_model=True, post_model=True, pre_label='Pre flagging', post_label='Post flagging', pre_model_label= 'Pre Model', post_model_label='Post Model', pre_model_color='green', post_model_color='yellow', pre_color='red', post_color='blue', font_size='medium')


# Create an INS object and use uvfits file
ins =INS(ss)

# Make a INS plot
# Pre-flagged and Post-flagged
cp.INS_plot(ins, prefix, file_ext='.pdf')


