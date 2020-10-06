import katsdpscripts
print "katsdpscripts version: %s"%katsdpscripts.__version__

from katsdpscripts.reduction.analyse_point_source_scans import analyse_point_source_scans
class my_opts:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
##
h5name='/var/kat/archive3/data/MeerKATAR1/telescope_products/2018/02/10/1518247207.h5'
ants=['m007']

##
for baseline in ants :
    print "\n Starting ",baseline,"\n"
    opts = my_opts(outfilebase=None, keepfilename=None, baseline=baseline, mc_iterations=1, freq_centre=1284.0,     freq_chans="200,4000", channel_mask='/var/kat/katsdpscripts/RTS/rfi_mask.pickle',     time_offset=0.0, pointing_model=None, old_loader=None, nd_models=None,     ku_band=False, keep_all=False,remove_spikes=False,batch=True,plot_spectrum=False)
    analyse_point_source_scans(h5name,opts)
    print "\n\n***************Done",baseline,"*************\n"
print "\nDONE ALL"

