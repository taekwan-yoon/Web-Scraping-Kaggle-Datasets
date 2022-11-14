import kaggle_scraper
from kaggle_scraper import ScrapeKaggle

search1 = ScrapeKaggle('taekwanyoon', 'hunger', 50)
search1.set_config()
search1.search()

num = search1.get_num_datasets()
print(num)

dataset = search1.get_specific_dataset(0)

url = search1.get_url(dataset)
print(url)


