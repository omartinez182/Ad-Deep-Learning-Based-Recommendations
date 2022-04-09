import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import hashlib
from pathlib import Path
from urllib.request import urlretrieve as download
from gazpacho import Soup
import click

# Pass the headers you want to retrieve from the xml such as ["loc", "lastmod"]
def parse_sitemap(url, headers):

    resp = requests.get(url)
    # we didn't get a valid response, bail
    if 200 != resp.status_code:
        return False

    # BeautifulSoup to parse the document
    soup = bs(resp.content, "xml")

    # find all the <url> tags in the document
    urls = soup.findAll('url')
    sitemaps = soup.findAll('sitemap')
    new_list = ["Source"] + headers
    panda_out_total = pd.DataFrame([], columns=new_list)

    if not urls and not sitemaps:
        return False

    # Recursive call to the the function if sitemap contains sitemaps
    if sitemaps:
        for u in sitemaps:
            sitemap_url = u.find('loc').string
            panda_recursive = parse_sitemap(sitemap_url, headers)
            panda_out_total = pd.concat([panda_out_total, panda_recursive], ignore_index=True)

    # storage for later...
    out = []

    # Creates a hash of the parent sitemap
    hash_sitemap = hashlib.md5(str(url).encode('utf-8')).hexdigest()

    # Extract the keys we want
    for u in urls:
        values = [hash_sitemap]
        for head in headers:
            loc = None
            loc = u.find(head)
            if not loc:
                loc = "None"
            else:
                loc = loc.string
            values.append(loc)
        out.append(values)

    # Creates a dataframe
    panda_out = pd.DataFrame(out, columns= new_list)

    # If recursive then merge recursive dataframe
    if not panda_out_total.empty:
        panda_out = pd.concat([panda_out, panda_out_total], ignore_index=True)

    #returns the dataframe
    return panda_out

if __name__ == "__main__":

    print("Preparing for Training Of Model")
    parent_url = click.prompt("URL of Homepage (www.<sitename>.com): ", 
                              type=str, default="www.psychobunny.com")
    csv_name_path = click.prompt("CSV of Image URL Reference Name:", 
                                 type=str, default="default_image")

    #format url correct
    while parent_url.split(".")[0] != "www":
        parent_url = click.prompt("Please formate URL correctly -> 'www.<sitename>.com:': ", 
                                  type=str, default="www.psychobunny.com")

    complete_url = f'https://{parent_url}/sitemap.xml'

    site_links_df = parse_sitemap(complete_url, ["loc"])

    column_names = ["Image_Name", "URL"]
    image_url_df = pd.DataFrame()

    for url in site_links_df["loc"]:
        
        soup = Soup.get(url)
        image_containers = soup.find('img', {'class':'Image--lazyLoad Image--fadeIn'})

        try:
            for image in image_containers:
                for t in image.attrs:
                    if t == "src":

                        image_url = "https:" + image.attrs[t]
                        image_name = url.split("/")[-1]
                        to_concat = pd.DataFrame([[image_name, image_url]], 
                                                 columns = column_names)

                        if image_url_df.empty:
                            image_url_df = to_concat                    
                        else:
                            image_url_df = pd.concat([image_url_df, to_concat])

                    elif t == "data-original-src":

                        image_url = "https:" + image.attrs[t]
                        image_name = url.split("/")[-1]
                        to_concat = pd.DataFrame([[image_name, image_url]], 
                                                 columns = column_names)

                        if image_url_df.empty:
                            image_url_df = to_concat                    
                        else:
                            image_url_df = pd.concat([image_url_df, to_concat])

        except Exception as e:
            print(e)
            pass

        
    print(f'Saving URL csv to "data/output/images_to_rec.csv"')
    image_url_df.to_csv(f'data/output/images_to_rec.csv')