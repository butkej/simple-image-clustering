#!/usr/bin/env python3
import argparse
import sklearn
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(prog='sic', description='simple image clustering based on k-means clustering')

    parser.add_argument('-i', '--input', type=argparse.FileType('r'), required=True, help='you must provide an input image to cluster it')
    parser.add_argument('-c','--clusters', type=int, default=5, dest='num_clusters', help='choose the number of clusters to produce [integer]')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    args = parser.parse_args()
    return args

#def load_image(path):


#def cluster_image():


#def save_result():
        

if __name__ == "__main__":
    #TODO
    args = parse_args()
    print('Called with arguments:')
    print(args)

    load_image()
    cluster_image()
    save_result()
