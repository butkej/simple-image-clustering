#!/usr/bin/env python3
import argparse
import numpy as np
import cv2

def parse_args():
    parser = argparse.ArgumentParser(prog='sic', description='simple image clustering based on k-means clustering')

    parser.add_argument('-i', '--infile', type=str, required=True, help='you must provide an input image to cluster it')
    parser.add_argument('-c','--clusters', type=int, default=5, dest='num_clusters', help='choose the number of clusters to produce (default is 5) [integer]')
    parser.add_argument('-r', '--runs', type=int, default=10, dest='num_runs', help='choose the number of clustering runs to attempt (default is 10) [integer]')
    parser.add_argument('-e', '--extension', type=str, default='png', dest='extension', help='choose the filename extension of the saved clustered image (default is png) [string]')
    parser.add_argument('--version', action='version', version='%(prog)s 0.2')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    print('Called with arguments:')
    print(args)

    # load image
    print('Loading input image...')
    print(args.infile)
    img = cv2.imread(str(args.infile))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # preprocessing
    img_shape = img.shape
    img = img.reshape((-1,3))
    img = np.float32(img)

    # k-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_PP_CENTERS

    print('Starting clustering...')
    compactness, labels, centers = cv2.kmeans(img, K=args.num_clusters, bestLabels=None, attempts=args.num_runs, criteria=criteria, flags=flags)
    
    centers = np.uint8(centers)
    result = centers[labels.flatten()]
    result_img = result.reshape((img_shape))

    # save clustered image
    print('Saving clustered image to ...')
    savepath = str(args.infile).split('.')
    savepath = savepath[0] + '_' + str(args.num_clusters) + '_CLUSTERS.' + str(args.extension)
    print(savepath)
    result_img = cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(savepath, result_img)
    print('Done!')

