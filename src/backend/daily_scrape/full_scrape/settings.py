# Scrapy settings for OSRS_Extract project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'full_scrape'

SPIDER_MODULES = ['full_scrape.spiders']
NEWSPIDER_MODULE = 'full_scrape.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'OSRS_Extract (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 10
#CONCURRENT_REQUESTS_PER_IP = 2

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'OSRS_Extract.middlewares.OsrsExtractSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'OSRS_Extract.middlewares.OsrsExtractDownloaderMiddleware': None,
'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
# RANDOM_UA_PER_PROXY = True
#
# ROTATING_PROXY_LIST = ['47.242.202.128:54466', '47.91.42.219:30001',
# '212.71.255.43:38613', '8.209.127.181:1080', '47.88.6.66:46726',
# '198.59.191.234:8080', '8.219.97.248:80', '47.254.153.200:80',
# '47.243.189.250:8000', '154.236.177.100:1981', '210.245.30.148:8080',
# '20.54.56.26:8080', '67.206.232.113:999', '154.236.189.29:8080',
# '47.242.254.88:8888', '167.114.96.27:9300', '20.213.232.137:8000',
# '20.43.60.43:8000', '45.79.208.64:44554', '110.34.3.229:3128',
# '178.79.191.47:54417', '54.66.104.168:80', '200.105.215.18:33630',
# '68.183.230.116:39517', '130.41.55.190:8080', '8.211.22.40:1080',
# '103.145.72.239:24002', '190.145.154.214:80', '139.162.182.54:49165',
# '196.179.204.9:8080', '67.200.146.75:3128']

#ROTATING_PROXY_LIST_PATH = '/my/path/proxies.txt'



# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'OSRS_Extract.pipelines.OsrsExtractPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
