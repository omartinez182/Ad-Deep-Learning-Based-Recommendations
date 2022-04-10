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

### Data Sourcing & Processing
To prototype our idea, we scraped images from a retailer's website, and manually collected a sample of their ads that were targeted to us on Facebook. 

We then used a pre-trained model (ResNet-18) `scripts/make_embeddings.py` to generate embeddings for the images that we used as our features. More details on the RecSys model can be found below under the modeling section.

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

Finally, we've also produced a UI (prototype) in which you just have to provide a sitemap and a folder (zipped) with images from which you'd like to get recommendations, and then you'll be able to preview the recommendations for each "query image" and will also get access to a CSV file the all of the URLs for the commended images. You can run the demo app with:

```
$ streamlit run app.py
```
Here's a demo of how the app works/looks like.

https://user-images.githubusercontent.com/63601717/162553930-690a71c7-346f-4433-8e1a-cfbc4b7c83ca.mp4

Notice that this web app is for demonstrations purposes only, so it won't download any new data and it is currently only getting data from the test website we used. However, if you'd like to get recommendations for your specific images, you can just replace the images under ```data ``` -> ```raw``` -> ```images``` and run all of the previous scripts again to produce the personalized recommendations with your data.


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
