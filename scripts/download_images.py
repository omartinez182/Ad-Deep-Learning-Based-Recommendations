from img2dataset import download
import pandas as pd
import shutil
import os

def main():
    """
    1. Creates CSV file with image names and URLs.
    2. Downloads images from the specified URL List.
    """
    # Get the list of image URLs
    df_img_urls = pd.read_csv('data/output/images_to_rec.csv')
    df_img_urls['URL'].to_csv('data/output/img_url_list.txt', sep="\n", index=False)

    output_dir = "data/raw"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # Get all images
    download(
        processes_count=16,
        thread_count=32,
        url_list="data/output/img_url_list.txt",
        image_size=256,
        output_folder=output_dir,
    )

    # Get all image names in the folder
    image_names = []
    for filename in os.listdir('data/raw/00000'):
        if filename.endswith("jpg"): 
            print(filename)
            image_names.append(filename)

    # Get the URL of each image
    urls = []
    for imagename in image_names:
        url = pd.read_json("data/raw/00000/"+imagename.replace("jpg", "json"), typ='series')[0]
        urls.append(url)

    # Save image name and URL
    fb_images = pd.DataFrame({"Image_Name": image_names, "URL":urls})
    fb_images.to_csv("data/output/images_CO.csv")

    # Remove json files
    dir_name = "data/raw/00000"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".json"):
            os.remove(os.path.join(dir_name, item))

    # Rename folder
    os.rename('data/raw/00000', 'data/raw/images')

    #source = 'data/raw/00000'
    #destination = 'data/raw/images'
    
    #allfiles = os.listdir(source)

    #for f in allfiles:
    #    try:
    #        shutil.move(source + f, destination + f)
    #    except:
    #        pass
            
    # Remove unnecesary folder
    #try:
    #    shutil.rmtree(source)
    #except OSError as e:
    #    print ("Error: %s - %s." % (e.filename, e.strerror))

    # Remove unnecessary files
    file1= "data/raw/00000.parquet"
    file2= "data/raw/00000_stats.json"
    files_del = [file1, file2]

    for file in files_del:
        try:
            os.remove(file)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))


if __name__ == "__main__":
    main()