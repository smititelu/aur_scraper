from fractions import Fraction
import scrapy
from scrapy_playwright.page import PageMethod

config = {
    'stoc': True,
    'weight': 100,

    'ounce': 31.1,
    'kilo': 1000,

    'dollar_to_ron': 4.32,
    'euro_to_ron': 5.1,
}

class AurSpider(scrapy.Spider):
    name = "aur"
    allowed_domains = [
        "tavex.ro",
        "avangardgold.ro",
        "neogold.ro",
        "goldbars.ro",
        "magnorshop.ro",
        "smartgold.ro",
        "aurlingou.ro",
        "auracasa.ro",
        "stonexbullion.com",
        "goldavenue.com",
        "goldsilvershop24.com",
        "citygold.ro",
    ]
    start_urls = [
        "https://smartgold.ro/index.php/categorie-produs/lingouri",
        "https://smartgold.ro/index.php/categorie-produs/monede/",
        "https://magnorshop.ro/lingouri",
        "https://tavex.ro/aur/page/1",
        "https://tavex.ro/aur/page/2",
        "https://avangardgold.ro/collections/vanzare-aur",
        "https://www.neogold.ro/lingouri-de-aur/",
        "https://www.neogold.ro/monede-de-aur/",
        "https://goldbars.ro/catalog/lingouri-de-aur",
        "https://goldbars.ro/catalog/monede-de-aur",
        "https://www.aurlingou.ro/lingouri",
        "https://www.aurlingou.ro/monede",
        "https://auracasa.ro/gb/3-gold-bars?page=1",
        "https://auracasa.ro/gb/3-gold-bars?page=2",
        "https://auracasa.ro/gb/3-gold-bars?page=3",
        "https://auracasa.ro/gb/3-gold-bars?page=4",
        "https://auracasa.ro/gb/6-gold-coins?page=1",
        "https://auracasa.ro/gb/6-gold-coins?page=2",
        "https://stonexbullion.com/en/gold-bars/?page=1",
        "https://stonexbullion.com/en/gold-bars/?page=2",
        "https://stonexbullion.com/en/gold-bars/?page=3",
        "https://stonexbullion.com/en/gold-bars/?page=4",
        "https://stonexbullion.com/en/gold-bars/?page=5",
        "https://www.citygold.ro/cat/lingouri-de-aur-investitie-colectie",
        "https://www.goldavenue.com/en/buy/gold?premium_per_oz_sort=asci&page=1",
        "https://www.goldavenue.com/en/buy/gold?premium_per_oz_sort=asci&page=2",
        "https://www.goldavenue.com/en/buy/gold?premium_per_oz_sort=asci&page=3",
        "https://www.goldavenue.com/en/buy/gold?premium_per_oz_sort=asci&page=4",
        "https://www.goldavenue.com/en/buy/gold?premium_per_oz_sort=asci&page=5",
        "https://www.goldavenue.com/en/buy/gold?premium_per_oz_sort=asci&page=6",
        "https://goldsilvershop24.com/buy/gold-bars.html",
        "https://goldsilvershop24.com/buy/gold-coins.html",
    ]
    custom_settings = {
        'COOKIES_ENABLED': True,
        'REDIRECT_ENABLED': True,
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'ro,en-US;q=0.9,en;q=0.8',
            'Referer': 'https://www.google.com',
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            scroll = False 
            wait_selector_button1 = False
            wait_selector_button2 = False
            wait_initial_network = False
            custom_page_methods = []
            wait_selector = False

            playwright_page_methods = []

            if "smartgold" in url:
                callback = self.parse_smartgold
                #wait_selector_button1 = "button[aria-label=\"Accept Cookies\"]"
                playwright_page_methods.append(PageMethod("wait_for_timeout", 15000))

                button = "button[class=\"load-next-button load-more-button shop-load-more-button\"]"

                page = 0
                if "monede" in url:
                    pages = 3
                elif "lingo" in url:
                    pages = 4
                else:
                    pages = 0
                while page < pages:
                    custom_page_methods.append(PageMethod("wait_for_timeout", 2000))
                    custom_page_methods.append(PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"))
                    custom_page_methods.append(PageMethod("wait_for_timeout", 2000))
                    custom_page_methods.append(PageMethod("click", button))
                    page = page + 1
            elif "goldsilvershop24" in url:
                callback = self.parse_goldsilvershop24

                playwright_page_methods.append(PageMethod("wait_for_timeout", 2000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 4)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 4000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 4)"))
            elif "avenue" in url:
                callback = self.parse_avenue

                # Wait for a real element to confirm the challenge is solved
                playwright_page_methods.append(PageMethod("wait_for_selector", "body"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 10000))
            elif "stonex" in url:
                callback = self.parse_stonex
                #wait_selector_button1 = "a[class=\"cc-btn cc-allow cc-btn-format\"]"
                wait_selector = "div[class=\"pics-view row\"]"
            elif "magnorshop" in url:
                wait_selector = "div[class=\"products wrapper grid products-grid\"]"
                #wait_selector_button1 = "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"                
                callback = self.parse_magnor
                scroll = True
                wait_initial_network = True
            elif "neogold" in url:
                #wait_selector_button1 = "button[class=\"cky-btn cky-btn-accept\"]"
                #wait_selector_button2 = "button[class=\"cmplz-btn cmplz-accept\"]"
                wait_selector = "div[class=\"main-content\"]"
                callback = self.parse_neogold
                scroll = True
            elif "avangard" in url:
                wait_selector = "div[class=\"collection__window\"]"
                wait_selector_button1 = "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
                callback = self.parse_avangard
                scroll = True
                custom_page_methods.append(PageMethod("wait_for_timeout", 2000))
                custom_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                custom_page_methods.append(PageMethod("wait_for_timeout", 4000))
                custom_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 4)"))
                custom_page_methods.append(PageMethod("wait_for_timeout", 4000))
                custom_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 6)"))
                custom_page_methods.append(PageMethod("wait_for_timeout", 4000))
                custom_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 8)"))
            elif "tavex" in url:
                callback = self.parse_tavex
                scroll = True
            elif "goldbars" in url:
                callback = self.parse_goldbars
                scroll = True
            elif "auracasa" in url:
                callback = self.parse_auracasa
                custom_page_methods.append(PageMethod("wait_for_timeout", 4000))
                custom_page_methods.append(PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"))
            elif "aurlingou" in url:
                callback = self.parse_aurlingou
                wait_selector = "div[class=\"section--content category_page\"]"
                #wait_selector_button1 = "button[class=\"allow-btn btn js-accept-all-cookies\"]"
            elif "citygold" in url:
                wait_selector = "div[class=\"ais-Hits\"]"
                #wait_selector_button1 = "button[class=\"CybotCookiebotDialogBodyButton\"]"
                callback = self.parse_citygold
                scroll = True
            else:
                print(f"Gold site not found in url: {url}")
                continue

            if wait_initial_network:
                playwright_page_methods.append(PageMethod("wait_for_load_state", "networkidle"))

            if wait_selector_button1:
                playwright_page_methods.append(PageMethod("wait_for_selector", wait_selector_button1))
                playwright_page_methods.append(PageMethod("click", wait_selector_button1))

            if wait_selector_button2:
                playwright_page_methods.append(PageMethod("wait_for_selector", wait_selector_button2))
                playwright_page_methods.append(PageMethod("click", wait_selector_button2))

            if custom_page_methods:
                playwright_page_methods.extend(custom_page_methods)

            if wait_selector:
                playwright_page_methods.append(PageMethod("wait_for_selector", wait_selector))

            if scroll is True:
                playwright_page_methods.append(PageMethod("wait_for_timeout", 2000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 2000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"))

            yield scrapy.Request(
                url=url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": playwright_page_methods,
                },
                callback=callback,
            )


    def get_weight_from_title(self, item_title, item_link):
        skip_list = ['argint', 'silver']
        if any(item in item_title for item in skip_list):
            self.logger.info(f"SKIP SILVER {item_link}")
            return 0

        skip_list = ['gulde', 'sovere', 'suvera', 'ducat', 'franc', 'franz', 'coroa', 'kruge', 'ruble', 'george', 'crown', 'marca', 'marci', 'kuru', 'imperiul', 'iling', 'illing', 'lira', 'lire', 'eagle', 'mark', 'kroner', 'coron', 'coroan', 'guilder']
        if any(item in item_title for item in skip_list):
            self.logger.info(f"SKIP COIN {item_link}")
            return 0

        item_title = item_title.replace('gold', '').replace('green', '').replace('roz', '').replace('kang', '').replace('lingo', '').replace('giovan', '').replace('multigram', '').replace('mozart', '').replace('king', '')
        try:
            if 'kilogram' in item_title:
                item_weight = float(item_title.strip().split("kilogram")[0].strip().split()[-1].replace(',', '.').split('x')[0]) * config['kilo']
            elif 'ounce' in item_title:
                item_weight = item_title.strip().split("ounce")[0].strip().split()[-1].replace(',', '.').split('x')[0]
                if "/" in item_weight:
                    item_weight = float(Fraction(item_weight))
                else:
                    item_weight = float(item_weight)
                item_weight = item_weight * config['ounce']
            elif 'uncie' in item_title:
                item_weight = item_title.strip().split("uncie")[0].strip().split()[-1].replace(',', '.').split('x')[0]
                if "/" in item_weight:
                    item_weight = float(Fraction(item_weight))
                else:
                    item_weight = float(item_weight)
                item_weight = item_weight * config['ounce']
            elif 'oz' in item_title:
                item_weight = item_title.strip().split("oz")[0].strip().split()[-1].replace(',', '.').split('x')[0]
                if "/" in item_weight:
                    item_weight = float(Fraction(item_weight))
                else:
                    item_weight = float(item_weight)
                item_weight = item_weight * config['ounce']
            elif 'gram' in item_title:
                item_weight = float(item_title.strip().split("gram")[0].strip().split()[-1].replace(',', '.').split('x')[0])
            elif 'kilo' in item_title:
                item_weight = float(item_title.strip().split("kilo")[0].strip().split()[-1].replace(',', '.').split('x')[0]) * config['kilo']
            elif 'kg' in item_title:
                item_weight = float(item_title.strip().split("kg")[0].strip().split()[-1].replace(',', '.').split('x')[0]) * config['kilo']
            elif 'gr' in item_title:
                item_weight = float(item_title.strip().split("gr")[0].strip().split()[-1].replace(',', '.').split('x')[0])
            elif 'g ' in item_title:
                item_weight = float(item_title.strip().split("g ")[0].strip().split()[-1].replace(',', '.').split('x')[0])
            elif 'g,' in item_title:
                item_weight = float(item_title.strip().split("g,")[0].strip().split()[-1].replace(',', '.').split('x')[0])
            elif 'g' in item_title:
                item_weight = float(item_title.strip().split("g")[0].strip().split()[-1].replace(',', '.').split('x')[0])
            elif '/' in item_title:
                item_weight = float(Fraction(item_title.strip().split()[0].strip().split()[-1].strip()))
            else:
                self.logger.error(f"Failed to parse weight: no keyword in this item {item_link} {item_title}")
                return 0
            return item_weight
        except Exception as e:
            self.logger.error(f"Failed to parse weight: no float in this item {item_link} {item_title} {e}")
            return 0


    def parse_goldsilvershop24(self, response):
        items = response.css("li.p-1.col-6.col-md-4.col-lg-4.col-xl-2.item.product.product-item")

        for item in items:
            item_link = item.css("a.product.photo.product-item-photo::attr(href)").get()
            if item_link:
                item_title = str(item.css("a.col-12.product-item-link.productListColumnProductTitle::text").get()).strip().lower().replace("-", "")
                item_price = str(item.css("div.col-6.small.tierPrice.goldFont.h-auto span::text").get())
                #self.logger.info(f"ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEE link {item_link}   {item_price}")
                if "None" in item_price:
                    self.logger.error(f"Cannot parse item price: {item_link}")
                    continue
                item_price = item_price.strip().split()[0].replace(' ', '').replace(",", "")
                item_price = (float(item_price) + 15) * config['euro_to_ron']

                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    async def parse_avenue(self, response):
        items = response.css("div.sc-c9a6ecec-0.bdzbGi")

        for item in items:
            if config['stoc'] is True:
                item_stoc=item.css("div.sc-94cb3c14-0.gSCdFF p::text").get()
                if "out of stock" in item_stoc.lower():
                    continue

            item_link = item.css("a.sc-21016d95-0.jxrwJO::attr(href)").get()
            if item_link:
                item_link = "https://www.goldavenue.com" + item_link
                #self.logger.info(f"ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEE link {item_link}")
                item_title = str(item.css("div.sc-94cb3c14-0.fOTrwV p::text").get()).strip().lower().replace("-", "")
                item_price = item.css("div.sc-94cb3c14-0.gSCdFF p::text").get()
                if "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price, check reduction for: {item_link}")
                    item_price = item.css("span.price.reduction::text").get()
                    if "None" in item_price:
                        self.logger.error(f"Cannot parse item price: {item_link}")
                        continue
                item_price = item_price.strip().split()[0].replace(' ', '').replace(",", "").replace("€", "")
                item_price = (float(item_price) + 120) * config['euro_to_ron']

                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }
        #await page.close()


    def parse_stonex(self, response):
        items = response.css("div.col-12.col-lg-6.col-xl-4.mb-5")

        for item in items:
            if config['stoc'] is True:
                item_stoc=item.css("span.badge.badge-sold-out.position-absolute").get()
                if item_stoc is not None:
                    continue

            item_link = item.css("div.product-item-in-small a::attr(href)").get()
            if item_link:
                item_link = "https://stonexbullion.com" + item_link
                item_title = str(item.css("span.card-title.clamp-2.mb-2.fw-bold.text-uppercase::text").get()).strip().lower().replace("-", "")
                item_price = item.css("span.text-nowrap.font-size-14.me-2::text").get()
                if "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price, check reduction for: {item_link}")
                    item_price = item.css("span.price.reduction::text").get()
                    if "None" in item_price:
                        self.logger.error(f"Cannot parse item price: {item_link}")
                        continue
                item_price = item_price.strip().split()[0].replace(' ', '').replace(",", "").replace("€", "")
                item_price = (float(item_price) + 15) * config['euro_to_ron']

                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_auracasa(self, response):
        items = response.css("article.js-product.product-miniature.js-product-miniature.prod-box-grid.col-sm-6.col-lg-4.col-xs-12")
        #self.logger.info(f"{items}")

        for item in items:
            item_link = item.css("h2.h3.product-title a::attr(href)").get()

            if item_link:
                item_title = str(item.css("h2.h3.product-title a::text").get()).strip().lower().replace("-", "")
                item_price = item.css("span.price::text").get()
                if "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price, check reduction for: {item_link}")
                    item_price = item.css("span.price.reduction::text").get()
                    if "None" in item_price:
                        self.logger.error(f"Cannot parse item price: {item_link}")
                        continue
                item_price = item_price.strip().split()[0].replace(' ', '').replace(",", "").replace("€", "")
                item_price = (float(item_price) + 15) * config['euro_to_ron']

                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_aurlingou(self, response):
        items = response.css("div.product.js-custom-difference")

        for item in items:
            item_link = item.css("a::attr(href)").get()
            if item_link:
                item_title = str(item.css("div.product_title a::text").get()).strip().lower()
                item_price = float(str(item.css("div.price::text").get()).strip().split()[0].replace(' ', '').replace(".", "").replace(',', '.'))
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_smartgold(self, response):
        items = response.css("li")

        for item in items:
            item_link = item.css("h2.woocommerce-loop-product__title a::attr(href)").get()
            if item_link:
                if config['stoc'] is True:
                    item_stoc = item.css(".outofstock").get()
                    if item_stoc is not None:
                        self.logger.info(f"OUT OF STOCK: {item_link}")
                        continue

                item_title = str(item.css("h2.woocommerce-loop-product__title a::text").get()).strip().lower()
                item_price = float(str(item.css("span.woocommerce-Price-amount.amount bdi::text").get()).strip().split('&')[0].replace(' ', '').replace(".", "").replace(',', '.'))
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_citygold(self, response):
        items = response.css("li.ais-Hits-item.col-12.col-md-8.col-lg-12.col-xl-8")
        for item in items:
            '''
            if config['stoc'] is True:
                item_stoc= item.css("button.action.tocart.primary span::text").get()
                #print(f"{item_stoc}")
                if "daug" not in item_stoc:
                    continue
            '''

            item_link = item.css("div.product-title a::attr(href)").get()
            item_title = str(item.css("div.product-title a::text").get()).strip()
            item_price = float(str(item.css("div.product-price::text").get()).split()[0].replace(".", ""))
            item_weight = float(item_title.split("-")[0].split()[-1].replace("g", " "))

            if item_weight > config['weight']:
                return

            item_price_per_gram = item_price / item_weight

            yield {
                'price_per_gram': item_price_per_gram,
                'price': item_price,
                'weight': item_weight,
                'link': item_link,
                'description': item_title
            }


    def parse_magnor(self, response):
        items = response.css("li.item.product.product-item")

        for item in items:
            item_link = item.css("a.product-item-link::attr(href)").get()
            if item_link:
                item_title = str(item.css("a.product-item-link::text").get()).strip().lower().replace("-", "")
                item_price = item.css("span.price-container span.price-wrapper span.price::text").get()

                if item_price is None or "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price for: {item_link}")
                    continue
                item_price = item_price.strip().split('lei')[0].replace(' ', '').replace(".", "").replace(",", ".")
                item_price = float(item_price)
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_goldbars(self, response):
        items = response.css("div.prod-card")

        for item in items:
            #item_link = item.css("img::attr(src)").get()
            item_link = item.css("a[class*=\"image-wrapper-prod\"]::attr(href)").get()

            if item_link:
                item_link = response.url + item_link
                item_title = str(item.css('a.product-name.mt-1.font-sm.line-clamp-2.max-sm\\:line-clamp-2::text').get()).strip().lower().replace("-", "")
                item_price = item.css("div.font-semibold.price-prod::text").get()
                if "None" in item_price:
                    self.logger.error(f"Cannot parse item price: {item_link}")
                    continue
                item_price = item_price.strip().split()[0].replace(' ', '').replace(".", "")
                item_price = float(item_price)
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_neogold(self, response):
        items = response.css("li.product-wrap")

        for item in items:
            if config['stoc'] is True:
                item_stoc= item.css("label.product-label.label-stock").get()
                if item_stoc is not None:
                    continue

            item_link = item.css("a.woocommerce-LoopProduct-link.woocommerce-loop-product__link::attr(href)").get()
            if item_link:
                item_title = str(item.css("h3.woocommerce-loop-product__title a::text").get()).strip().lower().replace("-", "")
                item_price = item.css("span.woocommerce-Price-amount.amount bdi::text").get()

                if item_price is None or "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price for: {item_link}")
                    continue
                item_price = item_price.strip().split('&')[0].replace(' ', '').replace('.', '').replace(",", ".")
                item_price = float(item_price)
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_avangard(self, response):
        items = response.css("div.product-item")

        for item in items:
            item_link = item.css("a.product-item__image-wrapper.db.mb3::attr(href)").get()
            if item_link:
                item_title = str(item.css("div.product-item__details a::text").get()).strip().lower().replace("-", "")
                item_price = item.css("div.buy_price span:not([class])::text").get()

                if item_price is None or "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price for: {item_link}")
                    continue
                item_price = item_price.strip().split('lei')[0].replace(' ', '').replace(",", ".")
                item_price = float(item_price)
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_tavex(self, response):
        items = response.css("div.grid__col--xs-6")

        for item in items:
            if config['stoc'] is True:
                item_stoc= item.css("span.product__stock.product__out-of-stock").get()
                if item_stoc is not None:
                    continue

            item_link = item.css("a.product__overlay-link::attr(href)").get()
            if item_link:
                item_title = str(item.css("span.product__title-inner::text").get()).strip().lower().replace("-", "")
                item_price = item.css("span.product__price-value.h-price-flash.js-product-price-from::text").get()

                if item_price is None or "None" in item_price:
                    self.logger.info(f"Cannot initially parse item price for: {item_link}")
                    continue
                item_price = item_price.strip().split()[0].replace(' ', '').replace(",", ".")
                item_price = float(item_price)
                item_weight = self.get_weight_from_title(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                item_price_per_gram = item_price / item_weight

                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }
