# Simple Image Clustering
Simple (or more fittingly: stupid) image clustering [*sic*] is a very barebones command line tool written in Python 3.  

### Dependencies
*sic* requires opencv2 (and also numpy) to perform clustering and manipulate files. Matplotlib is needed for additional plotting.

### Installation
To use this command line tool simply clone it into any directory you want:  
```
$ git clone https://github.com/butkej/simple-image-clustering.git
```

Afterwards, simply change into the downloaded directory, make the script executable and run it:  
```
$ cd simple-image-clustering/
$ chmod +x install.sh
$ ./install.sh
```
This will pip install the package into the currently activated environment and makes the script executable by calling only `sic` itself with its respective arguments.

### Usage

`$ (python) sic(.py) [-h] -i INFILE [-s SPECTRAL_SWITCH] [-c NUM_CLUSTERS] [-r NUM_RUNS] [-e EXTENSION] [--version]`
  
simple image clustering based on k-means clustering  
  
optional arguments:  
  -h, --help        show this help message and exit  
  -i INFILE, --infile INFILE        you must provide an input image to cluster it  
  -s SPECTRAL_SWITCH, --spectral SPECTRAL_SWITCH   switch to spectral clustering mode (see documentation for details) (FOUND BELOW IN THE README)
  -c NUM_CLUSTERS, --clusters NUM_CLUSTERS      choose the number of clusters to produce (default is 5) [integer]  
  -r NUM_RUNS, --runs NUM_RUNS      choose the number of clustering runs to attempt (default is 10) [integer]  
  -e EXTENSION, --extension EXTENSION       choose the filename extension of the saved clustered image (default is png) [string]  

---
#### Spectral Option
The spectral option takes an input folder (containing single wavenumber images) instead of a single input image!  
All .tif images in this folder will be loaded sequentially, converted into grayscale images and concatenated.  
This new array is then clustered to achieve a clustering across all spectral wavelenghts in the folder.
The clustered image is saved by converting cluster labels to a distinct color palette. This leads to a maximum of 22 clusters.  

By examining the saved clustering image the user can then choose a suitable cluster (prompted during script execution). The spectra from this cluster are then extracted, plotted and saved as well.  
Additionally all cluster spectra are saved to an extra folder individually.

![Color Palette](color_palette.png)
