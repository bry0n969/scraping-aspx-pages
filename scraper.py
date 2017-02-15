import scraperwiki
import mechanize
import re

# ASPX pages are some of the hardest challenges because they use javascript and forms to navigate
# Almost always the links go through the function function __doPostBack(eventTarget, eventArgument)
# which you have to simulate in the mechanize form handling library

# This example shows how to follow the Next page link

url = 'http://www.ddglobal.com/default.aspx?page=category%20search%20results&catlist=129&tree=25*Classical%2fFractional+V-belts+(3L%2c+A%2f4L%2c+B%2f5L%2c+C%2c+D%2c+E)*0%40%4030*3L+Belts*129%40%40&Parent=30&SearchSource=Pagination&SearchType=AND&forcePrice=False&forceAvailability=False&OrderByColumn=&OrderByDirection=&SearchKey=SK45521PM&CurrentPage=&DropDownPageSize=100
'
br = mechanize.Browser()

    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(url)

for pagenum in range(10):
    html = response.read()
    print "Page %d  page length %d" % (pagenum, len(html))
    print "Clinicians found:", re.findall(default.aspx?page.*%20%)(.*%20%)</a>", html)

    mnextlink = re.search("javascript:__doPostBack\('ItemSearchResults_Table\$ItemSearchResults_PrevNextLinksTD',''\).>Next Page", html) 
    if not mnextlink:
        break

    br.select_form(name='ctl00')
    br.form.set_all_readonly(False)
    br['__EVENTTARGET'] = 'ProviderSearchResultsTable1$NextLinkButton'
    br['__EVENTARGUMENT'] = ''
    response = br.submit()

