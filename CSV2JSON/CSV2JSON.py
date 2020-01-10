import csv, json
#rootpath='C:/Users/smerchant/OneDrive/KITAB/Working Scripts/'
#inputData = rootpath+"OpenITI_metadata_light.csv"


def generateJson(inputData):

    inputFile = csv.DictReader(open(inputData), delimiter="\t")
    dic = {}
    for r in inputFile:
        print(r)
        dic[r['data']] = r
    with open(inputData.replace(".csv", ".json"), "w") as f9:
        json.dump(dic, f9)


