# Ad Recommendations Using Image Embeddings
![image](https://www.wired.com/wp-content/uploads/2015/02/products.jpg)

## Motivation
#### Experimentation is King in Advertising.

* Marketing campaigns can be expensive, and many clicks are wasted due to irrelevant landing pages.

* Matching relevant landing pages and products with the ad content has huge benefits from an algorithmic and conversion rate perspective.

* Deciding which products/images are good variants for a given ad sometimes requires a lot of manual effort and introduces subjectivity into the experiment.

As an example, consider the following ad for polo shirts, that, when clicked, takes you to a landing page with T-shirts.

https://user-images.githubusercontent.com/63601717/162553790-b745db1a-b933-4dd0-8b73-373cccf29ae1.mov

In this case, the value proposition is to provide recommendations on the specific items in the inventory that match more closely (visually) the product in the ad the user clicked. These recommendations can be used to dynamically generate personalized category/landing pages. The relevance/match can have an impact on the conversion rate and therefore increase both revenues and decrease costs at the same time by having a higher relevance score (i.e. in search engine ads.)

<img width="1302" alt="Product End State" src="https://user-images.githubusercontent.com/63601717/162641293-19423c93-8fc7-4f00-b1f4-d3f53ffb0e4a.png">


## Getting Started

First, install the requirements necessary to run the python files.

```
$ pip install -r requirements.txt
```

Then, you can generate the image embeddings.

```
$ python3 scripts/make_embeddings.py
```

Once the embeddings have been generated, you can now produce the similarity matrix (model) from which the recommendations are derived.

```
$ python3 scripts/make_recommendations.py
```

Finally, we've also produced a UI (prototype) in which you just have to provide a sitemap and a folder (zipped) with images from which you'd like to get recommendations, and then you'll be able to preview the recommendations for each "query image" and will also get access to a CSV file with all of the URLs for the recommended images. You can run the demo app with:

```
$ streamlit run app.py
```
Here's a demo of how the app works/looks like.

https://user-images.githubusercontent.com/63601717/162553930-690a71c7-346f-4433-8e1a-cfbc4b7c83ca.mp4

Notice that this web app is for demonstrations purposes only, so it won't download any new data and it is currently only getting data from the test website we used. However, if you'd like to get recommendations for your specific images, you can just replace the images under ```data ``` -> ```raw``` -> ```images``` and run all of the previous scripts again to produce the personalized recommendations with your data.


## Data Sourcing & Processing
To prototype our idea, we scraped images from a retailer's website, and manually collected a sample of their ads that were targeted to us on Facebook. 

We then used a pre-trained model (ResNet-18) `scripts/make_embeddings.py` to generate embeddings for the images that we used as our features.


## Modeling Details

Our recommendation system model operates based on cosine similarity. The key idea is to first create vector embeddings for each image, and perform cosine similarity of each image with all others. We end up having a similarity matrix, and then we select the top-10 for each image, to generate its recommended images. We then link the recommended images back to the CSV in the preprocessing step to find the URLs of recommended images.

### Model Evaluation

In order to gauge how well our model was performing, we manually simulated interaction data (i.e. clicking relevant images according to our preferences) and then leveraged that interaction data in conjunction with the visual features to produce visually-aware recommendations.

We did a quick experiment comparing [AMR](https://ieeexplore.ieee.org/document/8618394) with the cosine similarity approach. The AUC for AMR was 0.8920 and for cosine similarity was 0.9397. However, what we found more interesting was the execution time: For the train set, cosine similarity took approximately 0.0612s while AMR took ~7.0172s. That provides some rationale for us to stick with the cosine similarity model at this point. 

However, it's important to clarify a few of the pros and cons of this method of evaluation which we outline below:

**Pros:**

* Allows us to demo how the approach would work with real interaction data coming from a retailer's website, and validate the pipeline.​

**Cons:**
* Extremely small sample size.​
* Reflects the real preferences of only a few users (our team) and it's unlikely to follow the distribution of the data in the real world.


To do this experiment we used the Cornac framework (citation below). If you'd like to reproduce this you can run the file

```
$ python3 scripts/model_eval.py
```
The results of the experiment are saved as a log file under:

```data``` -> ```output``` -> ```model_eval```.

Here's an example of how to execute the script using Google [Colab](https://colab.research.google.com/drive/1cv_4sS1to6i7bFC6Xg14DCKSMjJbrrA3?usp=sharing).


## Further improvements

* Leverage interaction data and auxiliary information about product attributes. (i.e. create embeddings for the product descriptions).

* Test debiasing the visually-aware recommendations using causal inference, as proposed in the [CausalRec paper](https://arxiv.org/abs/2107.02390).

## Citations
```
@article{salah2020cornac,
  title={Cornac: A Comparative Framework for Multimodal Recommender Systems},
  author={Salah, Aghiles and Truong, Quoc-Tuan and Lauw, Hady W},
  journal={Journal of Machine Learning Research},
  volume={21},
  number={95},
  pages={1--5},
  year={2020}
}

```
