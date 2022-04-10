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

Consine details

### Model Evaluation

Comparison between AMR and Cosine



## Citations

```
@misc{
}

```
