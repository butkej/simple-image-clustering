#!/usr/bin/env python3
import argparse
import numpy as np
import cv2

def parse_args():
    parser = argparse.ArgumentParser(prog='sic', description='simple image clustering based on k-means clustering')

    parser.add_argument('-i', '--infile', type=argparse.FileType('r'), required=True, help='you must provide an input image to cluster it')
    parser.add_argument('-c','--clusters', type=int, default=5, dest='num_clusters', help='choose the number of clusters to produce [integer]')
    parser.add_argument('-r', '--runs', type=int, default=10, dest='num_runs', help='choose the number of clustering runs to attempt [integer]')  )
    parser.add_argument('--version', action='version', version='%(prog)s 0.2')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    print('Called with arguments:')
    print(args)

    # load image
    print('Loading input image...')
    img = cv2.imread(args.infile)
    img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)

    # preprocessing
    img_shape = img.shape
    img = img.reshape((-1,3))
    img = np.float32(img)

    # k-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_PP_CENTERS

    print('Starting clustering...')
    compactness, labels, centers = cv2.kmeans(img, args.num_clusters, args.num_runs, criteria, flags) 
    
    center = np.uint8(center)
    result = center[labels.flatten()]
    result_img = result.reshape((img_shape))

    # save clustered image
    print('Saving clustered image to ...')

    print('Done!')

