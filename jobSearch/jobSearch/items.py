# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    basic_qualifications = scrapy.Field()
    team = scrapy.Field()
    city = scrapy.Field()
    company = scrapy.Field()
    locations = scrapy.Field()
    description = scrapy.Field()
    job_category = scrapy.Field()
    job_family = scrapy.Field()
    job_schedule_type = scrapy.Field()
    update_time = scrapy.Field()
    preferred_qualifications = scrapy.Field()
    title = scrapy.Field()
    publish_time = scrapy.Field()
    apply_url = scrapy.Field()
    origin_id = scrapy.Field()
    from_url = scrapy.Field()


class ShopifyItem(scrapy.Item):
    # define the fields for your item here like:
    team = scrapy.Field()
    locations = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    title = scrapy.Field()
    from_url = scrapy.Field()
    apply_url = scrapy.Field()
    new_grad = scrapy.Field()

# add your new item class