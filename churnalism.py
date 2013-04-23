from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display
import re

def churnalism(url=None, text=None):
    """
    This function will submit urls or text to churnalism.sunlightfoundation.com,
    determine whether they have been "churned", return the url(s) of the original content,
    the number of shared characters, and a link to compare the documents side-by-side on
    sunlight foundation's website

    Use as follows:

    # with a url:
    churnalism(url="http://www.cbsnews.com/8301-204_162-57526084/moms-bpa-levels-linked-to-sons-thyroid-problems/")

    # with a text blob

    article_text = "Researchers found that every doubling of BPA levels in pregnant moms was tied to a decrease of 0.13 micrograms per deciliter of total thyroxine (T4), meaning their thyroids were less active. Boys whose mother's had doubled their BPA had a 9.9 percent decrease in thyroid stimulating hormone (TSH), meaning their thyroid was overactive."
    churnalism(text=article_text)

    Returns:

    compare_url: A unique url on sunlight's page to assess this churn request
    input_url: the inputted url (only returned if a url is submitted)
    input_text: the inputted text (only returned if text is submitted)
    matched: True or False - Whether or not churnalism found a match
    matched_chars: Number of matched characters (only returned if "matched" is True)
    matched_urls: A list of matched urls (only returned when "matched" is True)

    """
    # sunlight foundation url
    CHURNALISM = "http://churnalism.sunlightfoundation.com/"

    # initalize output dictionary
    df = {}

    # create virtual display
    display = Display(visible=0, size=(800, 600))
    display.start()

    # open firefox
    browser = webdriver.Firefox()

    # get the url
    browser.get(CHURNALISM)

    # depending on arguments, input url or text form
    if url is not None:
        input_url = browser.find_element_by_id("url")
        input_url.send_keys(url)
        df['input_url'] = url
    elif text is not None:
        input_text = browser.find_element_by_id("text")
        input_text.send_keys(text)
        df['input_text'] = text
    else:
        print "must submit a 'url' or 'text'"

    # press the submit button! so cool!
    submit = browser.find_element_by_id("submitBtn")
    submit.click()

    # okay now were on the page, let's BeautifulSoup this madness
    content = browser.page_source
    soup = BeautifulSoup(content)

    # now that we saved the page source, let's close our browser and display
    browser.quit()
    display.stop()

    # first let's get the "share url" for this story
    df['compare_url'] = soup.find("input", {"id":"share-page-url"}).attrMap["value"]


    # now let's determine whether any matches were returned.
    matches = soup.findAll("h3", {"id":"match-title"})

    if matches[0].text!="No Matches":

        # set match to true and save matched urls
        df['matched'] = True
        df['matched_urls'] = [m.a['href'] for m in matches]

        # get the number of matched characters
        char_raw = soup.find("a", {"class":"characters"}).text
        df['matched_chars'] = int(re.sub(" Characters", "", char_raw))

    else:

        df['matched'] = False

    return(df)

if __name__ == "__main__":
    import sys
    print churnalism(url=sys.argv[1])
