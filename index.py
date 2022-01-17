import imp
from amazon_tracker import AmazonData
import constants as const

bot = AmazonData(const.SEARCH_TERM, const.BASE_URL, const.CURRENCY)
bot.run_script()




