from img2vec_pytorch import Img2Vec
from torchvision import transforms
from PIL import Image
from tqdm import tqdm
import pickle
import os


def main():
    """
    Generates embeddings for all images.
    """
    inputDim = (224,224)
    inputDir = "data/raw/images"
    inputDirCNN = "data/raw/imagesCNN"

    os.makedirs(inputDirCNN, exist_ok = True)

    transformationForCNNInput = transforms.Compose([transforms.Resize(inputDim)])

    for imageName in os.listdir(inputDir):
        try:
            I = Image.open(os.path.join(inputDir, imageName))
            newI = transformationForCNNInput(I)

            newI.save(os.path.join(inputDirCNN, imageName))
            
            newI.close()
            I.close()
        except Exception as e:
            pass
            print(e)
            logging.error(traceback.format_exc())

    # Generate Embeddings
    img2vec = Img2Vec(cuda=True, model='resnet-18')

    allVectors = {}
    print("Converting images to feature vectors:")
    for image in tqdm(os.listdir(inputDirCNN)):
        try:
            I = Image.open(os.path.join(inputDirCNN, image))
            vec = img2vec.get_vec(I)
            allVectors[image] = vec
            I.close() 
        except:
            pass

    # Save embedding vectors
    with open('models/PyschobunnyAllVectors.pkl', 'wb') as handle:
        pickle.dump(allVectors, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()