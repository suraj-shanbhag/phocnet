'''
Created on Jul 10, 2016

@author: ssudholt
'''
import numpy as np

def calc_map_from_cnn_features(solver, test_iterations, metric='braycurtis'):
    self.logger.info('Evaluating CNN after %d steps:', epoch*solver.param.test_interval)
    net_output = []
    labels = []
    for test_iter in xrange(solver.param.test_iter[0]):
            # calculate the net output
            solver.test_nets[0].forward()
            
            net_output.append(solver.test_nets[0].blobs['sigmoid'].data.flatten())
            labels.append(solver.test_nets[0].blobs['label'].data.flatten())
    net_output = np.vstack(net_output)
    
    # calculate mAP
    _, ave_precs = map_from_feature_matrix(features=net_output, labels=labels, 
                                           metric=metric, drop_first=True)
    mean_ap = np.mean(ave_precs[ave_precs > 0])
    return mean_ap, ave_precs