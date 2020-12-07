# getclippingpic
Tiny helper tool to get picture of a clipping by url or file

There are two parameters

* Parameter -u , give an url of a clipping 

```python clippic.py -u https://digi.kansalliskirjasto.fi/aikakausi/binding/941412/articles/78729857```
 
 downloads that particular region images of particular clipping.

* Parameter -i , input file in [digi clipping export](https://digi.kansalliskirjasto.fi/search/download/user-articles/articles.xlsx?criteria=%7B%22categoryIds%22%3A%5B%5D%2C%22endDate%22%3Anull%2C%22fuzzy%22%3Afalse%2C%22generalTypes%22%3A%5B%5D%2C%22includeCollected%22%3Afalse%2C%22keywords%22%3A%5B%22kissa%22%5D%2C%22onlyCollected%22%3Afalse%2C%22orderBy%22%3A%22CREATED_DESC%22%2C%22query%22%3A%22%22%2C%22queryTargetsMetadata%22%3Atrue%2C%22queryTargetsOcrText%22%3Atrue%2C%22requireAllKeywords%22%3Atrue%2C%22startDate%22%3Anull%2C%22subjectIds%22%3A%5B%5D%2C%22titles%22%3A%5B%5D%7D) format (saved as csv)

```python clippic.py -i cat_articles.csv```



Writes region images to the MYDIR="./clippings" directory.
Names region images as ARTICLEID_NUMBER.

