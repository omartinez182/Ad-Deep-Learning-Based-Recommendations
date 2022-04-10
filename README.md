# Ad Recommendations Using Image Embeddings
![image](https://www.wired.com/wp-content/uploads/2015/02/products.jpg)

## Motivation
#### Experimentation is King in Advertising.

* Marketing campaigns can be expensive, and many clicks are wasted due to irrelevant landing pages.

* Matching relevant landing pages and products with the ad content has huge benefits from an algorithmic and conversion rate perspective.

* Deciding which products/images are good variants for a given ad sometimes requires a lot of manual effort and introduces subjectivity into the experiment.

As an example, consider the following ad for polo shirts, that, when clicked, takes you to a landing page with T-shirts. In this case, the value proposition is to provide recommendations on the specific items in the inventory that match more closely (visually) the product in the ad the user clicked. This recommendations can be used to dinamically generate personalized category/landing pages. The relevance/match can have an impact on the conversion rate and therefore increase both revenue and decrease costs at the same time by having a higher relevance score (i.e. in search engine ads).

https://user-images.githubusercontent.com/63601717/162553790-b745db1a-b933-4dd0-8b73-373cccf29ae1.mov

Our approach consists of first using...


### Data Sourcing & Processing
Data was scraped from [Psycho Bunny](https://www.psychobunny.com/) ...

We then used a (Resnet-18) pre-trained model `scripts/make_embedding.py` to generate embeddings for the images.... 

## Getting Started

First, install the requirements necessary to run the python files.

```
$ pip install -r requirements.txt
```
Then, because

```
$ python3 scripts/make_dataset.py
```

Finally, you can run the demo app with:

```
$ streamlit run app.py
```
Here's a demo of how the app works/looks like.

https://user-images.githubusercontent.com/63601717/162553930-690a71c7-346f-4433-8e1a-cfbc4b7c83ca.mp4


Here's an example of how to execute all of the scripts using Google [Colab](https://colab.research.google.com/).


## Modeling Details

Our recommendation system model operates based on cosine similarity. The key idea is to first create vector embeddings for each image, and perform cosine similarity of each image with all others. We ended up having a large cosine similarity matrix, and we select the top-10 for each image, to generate its recommended images. We link up them back to the csv in the preprocessing step to find the URLs of recommended images.

### Model Evaluation

We did a quick comparison between AMR and Cosine Similarity. The AUC for AMR was 0.8920 and for Cosine Similarity was 0.9397, so we achieved a small bump for our model. What's more interesting is for the execution time: To do a complete training for the train set, cosine similarity takes 0.0612s while AMR takes 7.0172s. That provides some rationale for us to stick with the Cosine Similarity model.



## Citations

```
@misc{
}

```
