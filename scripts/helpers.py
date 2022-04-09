import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.testing import assert_almost_equal
import os
from PIL import Image


# Helpers
# Cosine Similarity Function
def getSimilarityMatrix(vectors):
    """
    Function to calculate the cosine similarity between vectors.
    
    Parameters
    ----------
    vectors : matrix
        Matrix with all of the embeddings.

    matrix : dataframe
        Dataframe with the cosine similarity between all vectors.
    """
    v = np.array(list(vectors.values())).T
    sim = np.inner(v.T, v.T) / ((np.linalg.norm(v, axis=0).reshape(-1,1)) * ((np.linalg.norm(v, axis=0).reshape(-1,1)).T))
    keys = list(vectors.keys())
    matrix = pd.DataFrame(sim, columns = keys, index = keys)
    
    return matrix

def get_image_names(inputDir):
  """
  Function to get all of the image file names from a folder.
  
  Parameters
  ----------
  inputDir : str
      Input directory (with all of the images)
  
  Output
  ----------
  query_images : list
      List with all of the image file names.
  """
  query_images = []
  for filename in os.listdir(inputDir):
    if filename.endswith("jpg"): 
      query_images.append(filename)
  
  return query_images


def setAxes(ax, image, query = False, **kwargs):
    """
    Produces axes for the plot.
    """
    value = kwargs.get("value", None)
    if query:
        ax.set_xlabel("Query Image\n{0}".format(image), fontsize = 12)
    else:
        ax.set_xlabel("Recommendation\n{0}".format(image), fontsize = 12)
    ax.set_xticks([])
    ax.set_yticks([])


def getSimilarImages(image, simNames, simVals):
    """
    Grabs similar images from the similarity matrix.

    Parameters
    ----------
    image: str
        File name of the query image.

    simNames: matrix
        Matrix of all images.

    simVals: matrix
        Matrix of similarity values.

    Output
    ----------
    imgs: list
        List of similar images.
    
    vals: list
        List of similarity values for the top selected images.
    """
    if image in set(simNames.index):
        imgs = list(simNames.loc[image, :])
        vals = list(simVals.loc[image, :])
        if image in imgs:
            assert_almost_equal(max(vals), 1, decimal = 5)
            imgs.remove(image)
            vals.remove(max(vals))
        return imgs, vals
    else:
        print("'{}' Unknown image".format(image))

     
def plotSimilarImages(image, similarNames, similarValues, inputDir, numRow=1, numCol=10):
    """
    Generates the plot for the query images and their recommendations.

    Parameters
    ----------
    image: str
        File name of the query image.

    simNames: matrix
        Matrix of all images.

    simVals: matrix
        Matrix of similarity values.

    inputDir: str
        Directory in which the images are stored.

    numRow: int
        Number of rows per image to display.

    numCol: int
        Number of columns to display.

    Output
    ----------
    fig:
        Matplotlib figure.
    """
    simImages, simValues = getSimilarImages(image, similarNames, similarValues)
    fig = plt.figure(figsize=(20, 20))
    fig.patch.set_alpha(0)

    # now plot the  most simliar images
    for j in range(0, numCol*numRow):
        ax = []
        if j == 0:
            img = Image.open(os.path.join(inputDir, image))
            ax = fig.add_subplot(numRow, numCol, 1)
            setAxes(ax, image, query = True)
        else:
            img = Image.open(os.path.join(inputDir, simImages[j-1]))
            ax.append(fig.add_subplot(numRow, numCol, j+1))
            setAxes(ax[-1], simImages[j-1], value = simValues[j-1])
        img = img.convert('RGB')
        plt.imshow(img)
        img.close()
    
    plt.show()
    return fig