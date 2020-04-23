from os import listdir
import pandas as pd

def main():
    dir_neg = "txt_sentoken/neg"
    dir_pos = "txt_sentoken/pos"
    print("Loading data..")
    data = load_docs(dir_neg)
    data = data.append(load_docs(dir_pos), ignore_index=True)
    data = data.sample(None, 1.0).reset_index(drop=True)
    print("Data loaded, saving...")
    data.to_csv("data.csv")
    print("Done")
    

def load_docs(dir):
    docs = {"text":[], "class":[]}
    for filename in listdir(dir):
        with open('/'.join([dir, filename])) as f:
            doc = f.read()
        docs["text"].append(doc)
        docs["class"].append(dir[-3:])
    return pd.DataFrame(docs)

if __name__ == "__main__":
    main()
