# Simple Image Clustering
Simple (or more fittingly: stupid) image clustering [*sic*] is a very barebones command line tool written in Python 3.  
### Dependencies
*sic* requires opencv2 to perform clustering and manipulate files.

### Usage

`$(python) sic.py [-h] -i INFILE [-c NUM_CLUSTERS] [-r NUM_RUNS] [-e EXTENSION] [--version]`

simple image clustering based on k-means clustering

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        you must provide an input image to cluster it
  -c NUM_CLUSTERS, --clusters NUM_CLUSTERS
                        choose the number of clusters to produce (default is 5) [integer]
  -r NUM_RUNS, --runs NUM_RUNS
                        choose the number of clustering runs to attempt (default is 10) [integer]
  -e EXTENSION, --extension EXTENSION
                        choose the filename extension of the saved clustered
                        image (default is png) [string]
  --version             show program's version number and exit
