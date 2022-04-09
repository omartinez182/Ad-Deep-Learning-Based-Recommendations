# Ad Recommendations Using Image Embeddings
![image](https://www.wired.com/wp-content/uploads/2015/02/products.jpg)

## Motivation
#### Experimentation is King in Advertising.

 * Marketing campaigns can be expensive, and many clicks are wasted due to irrelevant landing pages.

* Matching relevant landing pages and products with the ad content has huge benefits from an algorithmic and conversion rate perspective.

* It is hard to manually identify which other product images to use in the ad experimentation process.

https://github.com/omartinez182/omartinez182-Ad-Deep-Learning-Based-Recommendations/raw/main/demos/Use_Case_Demo.mov

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