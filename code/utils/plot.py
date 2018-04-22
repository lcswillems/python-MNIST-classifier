import matplotlib.pyplot as plt
import math

import utils

def plot_images(images, cls_true, cls_pred=None):    
    fig, axes = plt.subplots(4, 4)
    fig.subplots_adjust(hspace=0.5, wspace=0)

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i].reshape((utils.IMG_SIZE, utils.IMG_SIZE)), cmap="gray")

        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        ax.set_xlabel(xlabel)
        
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.show()