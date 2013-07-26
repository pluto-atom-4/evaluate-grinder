from net.grinder.plugin.http import HTTPPluginControl
from HTTPClient import NVPair

connectionDefaults = HTTPPluginControl.getConnectionDefaults()

""" Follow redirects (1 = true, 0 = false) """
connectionDefaults.setFollowRedirects(1)

""" Default header definition """
connectionDefaults.defaultHeaders = \
      [ NVPair('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:16.0) Gecko/20100101 Firefox/16.0'),
        NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Accept-Language', 'en-US,en;q=0.5'),
        NVPair('Accept-Encoding', 'gzip, deflate'), ]

headers = \
      [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml,application/json, */*'),
        NVPair('Accept-Language', 'en-us;q=0.5'),
        NVPair('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:16.0) Gecko/20100101 Firefox/16.0'), ]
