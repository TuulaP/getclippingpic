

import json
import requests

base = "https://digi.kansalliskirjasto.fi"
MYDIR = "./clippings/"


def downloadArticlePics(url):

    #url = "https://digi.kansalliskirjasto.fi/rest/article/78628867"

    response = requests.get(url)
    clipping = json.loads(response.text)

    articleid = url.split("/")[-1]

    regions = clipping['regions']

    counter = 1

    for region in regions:
        suffix = MYDIR + articleid + "_" + str(counter) + ".jpg"
        r = requests.get(base+region)
        # print(r)
        counter += 1

        open(suffix, 'wb').write(r.content)
        print("{0} file saved for article {1}.".format(suffix, articleid))


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='Gimme ids based on col id')

    parser.add_argument("-u", "--url", dest="url")
    parser.add_argument("-i", "--input", dest="input")

    args = parser.parse_args()

    url = args.url
    inputfile = args.input

    if url is not None:
        artid = url.split("/")[-1]
        downloadArticlePics(base + "/rest/article/" + artid)

    if inputfile is not None:
        import csv

        with open(inputfile, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass  # print(f'Column names are {", ".join(row)}')
                line_count += 1
                print("Processing: ", row['URL'])  # rest/article/78628867
                artid = row['URL'].split("/")[-1]
                downloadArticlePics(base + "/rest/article/" + artid)

