from scrapy.item import Item, Field
class chubbiesItem(Item):
    '''
    Class for the item retrieved by scrapy.
    '''
    # Here are the fields that will be crawled and stored
    name = Field() # Name of shorts
    link = Field()  # Link to individual shorts page
    price = Field() # Price of shorts
    desc = Field()  # Description of shorts
