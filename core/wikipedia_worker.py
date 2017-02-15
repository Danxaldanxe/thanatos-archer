import pywikibot
from pywikibot import pagegenerators
from core import config

def loadpage(page):
	try:
		site = pywikibot.Site()
		site.throttle.setDelays(delay=0, writedelay=5, absolute=False)
		wpage = pywikibot.Page(site, page)

	except pywikibot.exceptions.InvalidTitle:
		return

	return site, wpage

def savepage(wpage, text, comment):
	if config.test == False:
		try:
			wpage.text = text
			wpage.save(comment)

		except pywikibot.exceptions.EditConflict:
			printlog("edit conflict not saved", wpage)
		except pywikibot.exceptions.OtherPageSaveError:
			printlog("other page save error not saved", wpage)