import os
import pandas as pd


def filter_and_save(response):
    if response.status_code == 200:

        data = response.json()
        articles = data.get("articles", [])
        
        # convert to DataFrame
        df = pd.DataFrame(articles)
        
        # Keep only the most useful columns
        df = df[["source", "author", "title", "description", "url", "publishedAt"]]

        # Flatten the "source" column (it’s a dict like {"id":.., "name":..})
        df["source"] = df["source"].apply(lambda x: x.get("name") if isinstance(x, dict) else x)
        
        return df
    else:
        print("Error:", response.status_code, response.text)
        return pd.DataFrame()  




    