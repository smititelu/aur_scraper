from fractions import Fraction
import scrapy
from scrapy_playwright.page import PageMethod

config = {
    'stock': True,
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
        "https://avangardgold.ro/collections/vanzare-aur",
        "https://smartgold.ro/index.php/categorie-produs/lingouri",
        "https://smartgold.ro/index.php/categorie-produs/monede/",
        "https://magnorshop.ro/lingouri",
        "https://tavex.ro/aur/page/1",
        "https://tavex.ro/aur/page/2",
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
                    custom_page_methods.append(PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"))
                    custom_page_methods.append(PageMethod("wait_for_timeout", 5000))
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
                playwright_page_methods.append(PageMethod("wait_for_timeout", 5000))
                playwright_page_methods.append(PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight / 2)"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 10000))
            elif "stonex" in url:
                callback = self.parse_stonex
                #wait_selector_button1 = "a[class=\"cc-btn cc-allow cc-btn-format\"]"
                wait_selector = "div[class=\"pics-view row\"]"
            elif "magnorshop" in url:
                #wait_selector = "div[class=\"products wrapper grid products-grid\"]"
                #wait_selector_button1 = "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"                
                playwright_page_methods.append(PageMethod("wait_for_selector", "body"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 5000))
                callback = self.parse_magnor
                scroll = True
                #wait_initial_network = True
            elif "neogold" in url:
                #wait_selector_button1 = "button[class=\"cky-btn cky-btn-accept\"]"
                #wait_selector_button2 = "button[class=\"cmplz-btn cmplz-accept\"]"
                #wait_selector = "div[class=\"main-content\"]"
                playwright_page_methods.append(PageMethod("wait_for_selector", "body"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 10000))
                callback = self.parse_neogold
                scroll = True
            elif "avangard" in url:
                #wait_selector = "div[class=\"collection__window\"]"
                #wait_selector_button1 = "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
                playwright_page_methods.append(PageMethod("wait_for_selector", "body"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 5000))
                callback = self.parse_avangard
                #scroll = True
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
                playwright_page_methods.append(PageMethod("wait_for_selector", "body"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 5000))
                custom_page_methods.append(PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"))
            elif "aurlingou" in url:
                callback = self.parse_aurlingou
                wait_selector = "div[class=\"section--content category_page\"]"
                #wait_selector_button1 = "button[class=\"allow-btn btn js-accept-all-cookies\"]"
            elif "citygold" in url:
                #wait_selector = "div[class=\"ais-Hits\"]"
                #wait_selector_button1 = "button[class=\"CybotCookiebotDialogBodyButton\"]"
                playwright_page_methods.append(PageMethod("wait_for_selector", "body"))
                playwright_page_methods.append(PageMethod("wait_for_timeout", 5000))
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


    def get_weight(self, item_title, item_link):
        skip_list = ['argint', 'silver']
        if any(item in item_title for item in skip_list):
            self.logger.debug(f"Skip silver: {item_link}")
            return 0

        skip_list = ['platin',]
        if any(item in item_title for item in skip_list):
            self.logger.debug(f"Skip platinum: {item_link}")
            return 0

        skip_list = ['gulde', 'sovere', 'suvera', 'ducat', 'franc', 'franz', 'coroa', 'kruge', 'ruble', 'george', 'crown', 'marca', 'marci', 'kuru', 'imperiul', 'iling', 'illing', 'lira', 'lire', 'eagle', 'mark', 'kroner', 'coron', 'coroan', 'guilder']
        if any(item in item_title for item in skip_list):
            self.logger.debug(f"Skip coin: {item_link}")
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
                item_weight = item_title.strip().split("oz")[0].strip()

                if "x" in item_weight:
                    x0 = item_weight.split('x')[0].split()[-1]
                    x1 = item_weight.split('x')[1]

                    if "/" in x0:
                        x0 = float(Fraction(x0))
                    else:
                        x0 = float(x0)
                    if "/" in x1:
                        x1 = float(Fraction(x1))
                    else:
                        x1 = float(x0)
                    item_weight = x0 * x1
                else:
                    item_weight= item_weight.split()[-1]
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
                self.logger.error(f"Failed to parse weight: {item_link} no keyword")
                return 0
            return item_weight
        except Exception as e:
            self.logger.error(f"Failed to parse weight: {item_link} {e}")
            return 0


    def get_price(self, item_price_str, item_price_transport):
        if '€' in item_price_str:
            item_price_str = item_price_str.strip().lower().replace(' ', '').replace(",", "").replace("€", "")
        else:
            item_price_str = item_price_str.strip().lower().replace(' ', '').replace('.', '').replace(',', '.').replace('lei', '')

        try:
            if '€' in item_price_str:
                item_price = (float(item_price_str) + item_price_transport) * config['euro_to_ron']
            else:
                item_price = float(item_price_str) + item_price_transport
            return item_price
        except Exception as e:
            self.logger.error(f"Failed to parse price: {item_link} {e}")
            return 0


    def get_price_per_gram(self, items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
        for item in items:
            # get link
            item_link = item.css(item_link_css).get()
            if item_link:
                if item_link_prefix:
                    item_link = item_link_prefix + item_link

                # get stock
                if config['stock'] is True and item_stoc_css is not None:
                    item_stoc = item.css(item_stoc_css).get()
                    if item_stoc is not None:
                        if "epuizat" in item_stoc.lower() or "out" in item_stoc.lower():
                            self.logger.debug(f"Out of stock: {item_link}")
                            continue
                        else:
                            self.logger.debug(f"item has stoc selector but not out of stock: {item_link}")

                # get title
                item_title = str(item.css(item_title_css).get()).strip().lower().replace("-", "")

                # get price
                item_price = item.css(item_price_css1).get()
                if item_price is None or "None" in item_price:
                    if item_price_css2:
                        item_price = item.css(item_price_css2).get()
                        if item_price is None or "None" in item_price:
                            self.logger.error(f"Cannot parse price css2 for: {item_link}")
                            continue
                    else:
                        self.logger.error(f"Cannot parse price css1 for: {item_link}")
                        continue

                item_price = self.get_price(item_price, item_price_transport)

                if item_price == 0:
                    continue

                # get weight
                item_weight = self.get_weight(item_title, item_link)

                if item_weight == 0:
                    continue

                if item_weight > config['weight']:
                    continue

                # get price per gram
                item_price_per_gram = item_price / item_weight

                # return csv line
                yield {
                    'price_per_gram': item_price_per_gram,
                    'price': item_price,
                    'weight': item_weight,
                    'link': item_link,
                    'description': item_title
                }


    def parse_goldsilvershop24(self, response):
        items = response.css("li.p-1.col-6.col-md-4.col-lg-4.col-xl-2.item.product.product-item")
        item_link_css = "a.product.photo.product-item-photo::attr(href)"
        item_link_prefix = None
        item_title_css = "a.col-12.product-item-link.productListColumnProductTitle::text"
        item_price_css1 = "div.col-6.small.tierPrice.goldFont.h-auto span::text"
        item_price_css2 = None
        item_price_transport = 15
        item_stoc_css = None


    async def parse_avenue(self, response):
        items = response.css("div.sc-c9a6ecec-0.bdzbGi")
        item_link_css = "a.sc-21016d95-0.jxrwJO::attr(href)"
        item_link_prefix = "https://www.goldavenue.com"
        item_title_css = "div.sc-94cb3c14-0.fOTrwV p::text"
        item_price_css1 = "div.sc-94cb3c14-0.gSCdFF p::text"
        item_price_css2 = None
        item_price_transport = 120
        item_stoc_css = "div.sc-94cb3c14-0.gSCdFF p::text"

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_stonex(self, response):
        items = response.css("div.col-12.col-lg-6.col-xl-4.mb-5")
        item_link_css = "div.product-item-in-small a::attr(href)"
        item_link_prefix = "https://stonexbullion.com"
        item_title_css = "span.card-title.clamp-2.mb-2.fw-bold.text-uppercase::text"
        item_price_css1 = "span.text-nowrap.font-size-14.me-2::text"
        item_price_css2 = "span.price.reduction::text"
        item_price_transport = 15
        item_stoc_css = "span.badge.badge-sold-out.position-absolute"

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_auracasa(self, response):
        items = response.css("article.js-product.product-miniature.js-product-miniature.prod-box-grid.col-sm-6.col-lg-4.col-xs-12")
        item_link_css = "h2.h3.product-title a::attr(href)"
        item_link_prefix = None
        item_title_css = "h2.h3.product-title a::text"
        item_price_css1 = "span.price.reduction::text"
        item_price_css2 = "span.price::text"
        item_price_transport = 15
        item_stoc_css = None

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_aurlingou(self, response):
        items = response.css("div.product.js-custom-difference")
        item_link_css = "a::attr(href)"
        item_link_prefix = None
        item_title_css = "div.product_title a::text"
        item_price_css1 = "div.price::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = None

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_smartgold(self, response):
        items = response.css("li")
        item_link_css = "h2.woocommerce-loop-product__title a::attr(href)"
        item_link_prefix = None
        item_title_css = "h2.woocommerce-loop-product__title a::text"
        item_price_css1 = "span.woocommerce-Price-amount.amount bdi::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = ".outofstock"

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_citygold(self, response):
        items = response.css("li.ais-Hits-item.col-12.col-md-8.col-lg-12.col-xl-8")
        item_link_css = "div.product-title a::attr(href)"
        item_link_prefix = None
        item_title_css = "div.product-title a::text"
        item_price_css1 = "div.product-price::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = None

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_magnor(self, response):
        items = response.css("li.item.product.product-item")
        item_link_css = "a.product-item-link::attr(href)"
        item_link_prefix = None
        item_title_css = "a.product-item-link::text"
        item_price_css1 = "span.price-container span.price-wrapper span.price::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = None

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_goldbars(self, response):
        items = response.css("div.prod-card")
        item_link_css = "a[class*=\"image-wrapper-prod\"]::attr(href)"
        item_link_prefix = "https://goldbars.ro"
        item_title_css = "a.product-name.mt-1.font-sm.line-clamp-2.max-sm\\:line-clamp-2::text"
        item_price_css1 = "div.font-semibold.price-prod::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = None

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_neogold(self, response):
        items = response.css("li.product-wrap")
        item_link_css = "a.woocommerce-LoopProduct-link.woocommerce-loop-product__link::attr(href)"
        item_link_prefix = None
        item_title_css = "h3.woocommerce-loop-product__title a::text"
        item_price_css1 = "span.woocommerce-Price-amount.amount bdi::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = "label.product-label.label-stock"

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_avangard(self, response):
        items = response.css("div.product-item")
        item_link_css = "a.product-item__image-wrapper.db.mb3::attr(href)"
        item_link_prefix = "https://avangardgold.ro"
        item_title_css = "div.product-item__details a::text"
        item_price_css1 = "div.buy_price span:not([class])::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = None

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item


    def parse_tavex(self, response):
        items = response.css("div.grid__col--xs-6")
        item_link_css = "a.product__overlay-link::attr(href)"
        item_link_prefix = None
        item_title_css = "span.product__title-inner::text"
        item_price_css1 = "span.product__price-value.h-price-flash.js-product-price-from::text"
        item_price_css2 = None
        item_price_transport = 0
        item_stoc_css = "span.product__stock.product__out-of-stock"

        for item in self.get_price_per_gram(items, item_link_css, item_title_css, item_price_css1, item_price_css2, item_stoc_css, item_link_prefix, item_price_transport):
            yield item
