import pickle
import cornac
from cornac.eval_methods import RatioSplit
from cornac.models import ItemKNN, AMR
from cornac.data import ImageModality
import tensorflow as tf

def main():
    """
    Evaluates the performance of Cosine & AMR models.
    """
    SEED = 42
    VERBOSE = True

    # Item-IDs
    with open("data/interaction_data/img_ids", "rb") as fp:
        img_ids = pickle.load(fp)

    # Image Features
    with open("data/interaction_data/img_features", "rb") as fp:
        img_features = pickle.load(fp)

    # Interaction/Feedback matrix
    with open("data/interaction_data/interaction_data", "rb") as fp:
        interaction_data = pickle.load(fp)


    # Cosine similarity (Neighborhood-Based)
    cosine = ItemKNN(k=15, similarity="cosine", name="Cosine", verbose=VERBOSE, seed=SEED)

    # Deep Learning model (Adversarial)
    amr = AMR(k=15, k2=15, n_epochs=1, batch_size=10, learning_rate=0.1, lambda_w=0.1, lambda_b=0.1, lambda_e=0.0, seed=SEED)

    item_image_modality = ImageModality(features=img_features, ids=img_ids, normalized=True)

    ratio_split = RatioSplit(
        data=interaction_data,
        test_size=0.35,
        item_image=item_image_modality,
        verbose=VERBOSE,
        seed=SEED,
    )

    auc = cornac.metrics.AUC()

    cornac.Experiment(eval_method=ratio_split, models=[cosine, amr], metrics=[auc], save_dir='data/output/model_eval').run()


if __name__ == "__main__":
    main()