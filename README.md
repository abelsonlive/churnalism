Churnalism API
===============
This python function will submit urls or text to [churnalism.sunlightfoundation.com](http://churnalism.sunlightfoundation.com/), determine whether they have been "churned", and return the url(s) of the original content, the number of characters the documents share, and a link to compare the documents side-by-side on sunlight foundation's website

### Requirements
This function is built on top of three python libraries: `selenium`,`pyvirtualdisplay`, and `BeatifulSoup`.  If you have `pip` installed on your computer, you can install all three by typing the following into your terminal:
```
pip install selenium pyvirtualdisplay BeautifulSoup
```
Then download this folder somewhere that your PYTHONPATH will recognize it.
### Usage:

# with a url:
```
from churnalism import churnalism
churnalism(url="http://www.cbsnews.com/8301-204_162-57526084/moms-bpa-levels-linked-to-sons-thyroid-problems/")
```

# with a text blob:
```
from churnalism import churnalism
article_text = "Researchers found that every doubling of BPA levels in pregnant moms was tied to a decrease of 0.13 micrograms per deciliter of total thyroxine (T4), meaning their thyroids were less active. Boys whose mother's had doubled their BPA had a 9.9 percent decrease in thyroid stimulating hormone (TSH), meaning their thyroid was overactive."
churnalism(text=article_text)
```

# in the command line (just with urls):
```
python churnalism.py "http://www.cbsnews.com/8301-204_162-57526084/moms-bpa-levels-linked-to-sons-thyroid-problems/" > output.json
```

### Returns:
```
compare_url: A unique url on sunlight's page to assess this churn request
input_url: the inputted url (only returned if a url is submitted)
input_text: the inputted text (only returned if text is submitted)
matched: True or False - Whether or not churnalism found a match
matched_chars: Number of matched characters (only returned if "matched" is True)
matched_urls: A list of matched urls (only returned when "matched" is True)
```
