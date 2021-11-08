import json
import wget
import pandas as pd

alkuvuosi=1900
loppuvuosi=1929

maara_url = ("https://korp.csc.fi/cgi-bin/korp/korp.cgi?command=count_all&groupby=text_publ_type&cache=true"
    "&start=0&end=24&corpus=KLK_FI_YEAR&context=&incremental=true")
news_name_dict={}
for vuosi in range(alkuvuosi, loppuvuosi+1):
    print("Haetaan", vuosi)
    Y = str(vuosi)
    maara_url_iter = maara_url.replace("YEAR", Y)
    tmp = wget.download(maara_url_iter)
    klk= "KLK_FI_" + str(vuosi)
    with open(tmp, "r", encoding="utf-8") as f:
        data = json.load(f)
        total_number_year = data["total"]["absolute"]["sanomalehti"]
        news_name_dict[vuosi] = total_number_year
news_names_df = pd.DataFrame.from_dict(news_name_dict, orient="index")
columns = ["Vuosi", "Määrä"]
news_names_df = news_names_df.reset_index().set_axis(columns, axis=1)
news_names_df.to_csv(f"news_names_results/Number_of_tokens_newspapers_{alkuvuosi}_{loppuvuosi}.tsv", sep="\t",index=True)
