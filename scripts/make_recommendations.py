from helpers import getSimilarityMatrix
import pandas as pd
import pickle
from tqdm import tqdm
import argparse

def main(args):
    """
    Generates recommendation models.
    """  
    # Load embeddings
    with open('models/PyschobunnyAllVectors.pkl', 'rb') as handle:
        allVectors = pickle.load(handle)

    similarityMatrix = getSimilarityMatrix(allVectors)

    # Number of similary images to retreive
    k = args.k 

    similarNames = pd.DataFrame(index = similarityMatrix.index, columns = range(k))
    similarValues = pd.DataFrame(index = similarityMatrix.index, columns = range(k))

    for j in tqdm(range(similarityMatrix.shape[0])):
        kSimilar = similarityMatrix.iloc[j, :].sort_values(ascending = False).head(k)
        similarNames.iloc[j, :] = list(kSimilar.index)
        similarValues.iloc[j, :] = kSimilar.values

    # Save the model 
    similarNames.to_pickle("models/similarNames.pkl")
    similarValues.to_pickle("models/similarValues.pkl")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--k',
                        type=int,
                        default=10)
    args = parser.parse_args()
    main(args)