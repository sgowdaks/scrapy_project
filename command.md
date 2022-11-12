* `pip install scrapy`
* `scrapy startproject receipes`
* `scrapy shell`
* `fetch <url>`
* Using CSS elements
  * `response.css('<html element>.<class name>')` 
  * `response.css('<html element>.<class name>').get()` -> will return string
  * `product.css('span.card__title-text::text').getall()` -> getting text from span
  * `product.css('a::attr(href)').getall()` -> get href links
* Using X-Path
  * `response.xpath("//li[@class='structured-ingredients__list-item']/p/span/text()").extract()`  -> get response then at the end add text() to get text
  * `i.xpath(".//p/span/text()").extract())` -> using relative path, it start from p that is near by
  * `i.xpath(".//text()").extract())` -> if you want to ignore elements
  * `response.xpath("//img[contains(@class, 'primary-image')]/@src")` -> extract image link (select and image element, that contains class primary-image and src for image, returns Xpath)
  * `response.xpath("//img[contains(@class, 'primary-image')]/@src").extract()` -> gives link
  * ` response.xpath("//div[@class='arrowgreen']/ul/li[1]/a/@href").extract()` -> for href link
* `scrapy crawl <crawler name> -o <file_to_be_saved>.csv`
  
