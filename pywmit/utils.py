import mwparserfromhell
import mwklient


def parse(title):
    site = mwklient.Site('it.wikipedia.org')
    page = site.pages[title]
    text = page.text()
    return mwparserfromhell.parse(text)
