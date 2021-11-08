import json
import csv
import pandas as pd

print("starting")
data = pd.read_csv("https://raw.githubusercontent.com/Yleisradio/yle-uutiset/master/names/data.csv", encoding="latin-1", header=0) #Etunimet_1900-2016
print("kakka")
aloitusvuosi=1900
lopetusvuosi=2016
#data= file.loc[(file["Syntymävuosi"] >= aloitusvuosi) & (file["Syntymävuosi"] <= lopetusvuosi) & ((file["Etunimi"].astype(str).str.len()>1))]
data["Määrä"]=data["Määrä"].replace("Alle 10", "10")
data = data.astype({"Syntymävuosi":int, "Määrä":int})
#joined_data=data.groupby(["Etunimi", "Sukupuoli"])["Määrä"].sum().rename("Määrä").reset_index().sort_values(by="Määrä", ascending=False)
#joined_data= joined_data.set_index("Etunimi")
#joined_data.columns = ["Etunimi", "Sukupuoli", "Määrä"]
#joined_data=joined_data.sort_values(by=["Määrä"])
#print(joined_data.head(10))
#joined_data=joined_data[:1001]
data.to_csv(f"vrk_names/Names_{aloitusvuosi}_{lopetusvuosi}.tsv", sep="\t",index=True)

    