# getclippingpic
Tiny helper tool to get picture of a clipping by url or file

There are two parameters

* Parameter -u , give an url of a clipping 

```python clippic.py -u https://digi.kansalliskirjasto.fi/aikakausi/binding/941412/articles/78729857```
 
 downloads that particular region images of particular clipping.

* Parameter -i , input file in digi clipping export format

```python clippic.py -i cat_articles.csv```



Writes region images to the MYDIR="./clippings" directory.
Names region images as ARTICLEID_NUMBER.

