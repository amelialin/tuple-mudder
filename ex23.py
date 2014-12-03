# https://github.com/lmjohns3/theano-nets/blob/master/scripts/theanets-untie.py

#!/usr/bin/env python

import climate # command line utilities
import cPickle as pickle # serializes an arbitrary Python object (turns it into a series of bytes)
import gzip
import numpy as np # package for scientific computing with Python

logging = climate.get_logger('theanets-untie')

@climate.annotate( # what is this? defines inputs for the subsequent function?
    source='load a saved network from FILE',
    target='save untied network weights to FILE',
)
def main(source, target):
    opener = gzip.open if source.endswith('.gz') else open # an inline if/else statement!
    p = pickle.load(opener(source))

    logging.info('read from %s:', source)
    for w, b in zip(p['weights'], p['biases']):
        logging.info('weights %s bias %s %s', w.shape, b.shape, b.dtype)

    p['weights'].extend(0 + w.T for w in p['weights'][::-1]) # extend appends multiple elements to the end
    p['biases'].extend(-b for b in p['biases'][-2::-1])
    p['biases'].append(np.zeros(
        (len(p['weights'][0]), ), p['biases'][0].dtype))

    logging.info('writing to %s:', target)
    for w, b in zip(p['weights'], p['biases']):
        logging.info('weights %s bias %s %s', w.shape, b.shape, b.dtype)

    opener = gzip.open if target.endswith('.gz') else open
    pickle.dump(p, opener(target, 'wb'), -1)


if __name__ == '__main__': # cool! just like we've seen
    climate.call(main)