import mwparserfromhell
import pywikibot


def parse(title):
    site = pywikibot.Site('it', 'wikipedia')
    page = pywikibot.Page(site, title)
    text = page.get()
    return mwparserfromhell.parse(text)