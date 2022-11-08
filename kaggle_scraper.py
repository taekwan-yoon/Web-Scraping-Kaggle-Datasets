from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # to silently run selenium

class ScrapeKaggle:
    def __init__(self, url, path):
        self.url = url  # url to dataset page (i.e., https://www.kaggle.com/datasets/ankitmishra0/narendra-modi-speeches)
        # local path to chromedriver (Available at: https://chromedriver.chromium.org/downloads)
        self.path = path
        self.title = "Scraping title not done or failed."
        self.usability = "Scraping usability not done or failed."
        self.upvotes = "Scraping upvotes not done or failed."
        self.description = "Scraping description not done or failed."
        self.update_frequency = "Scraping update frequency not done or failed."
        self.last_updated = "Scraping last updated not done or failed."
        self.author = "Scraping author not done or failed."
        self.license_ = "Scraping license not done or failed."
        self.views = "Scraping views not done or failed."
        self.downloads = "Scraping downloads not done or failed."
        self.download_per_view = "Scraping download per view not done or failed."
        self.download_size = "Scraping download size not done or failed."

    def scrape(self):
        '''
        This method modifies the attributes in __init__ by scraping web data of specified url using selenium through xpath. 
        '''
        
        chrome_options = Options()
        # silently runs selenium; otherwise, it opens the browser every time
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)
        driver.get(self.url)
        self.title = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[2]/div/div[2]/div[1]/h1").text
        self.usability = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[1]/div[2]/div/p/span").text
        self.upvotes = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[2]/div/div[1]/div/div[1]/button[2]").text
        self.description = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[1]/div[1]/div[2]/div/div/div/p").text
        self.update_frequency = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[1]/div[2]/p[2]").text
        self.last_updated = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[2]/div/div[1]/span/span[2]/span").text
        self.author = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[2]/div/div[1]/span/span[1]").text
        
        i = 0
        while i == 0:  # two possible xpaths for license
            try:
                self.license_ = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[1]/div[2]/p[1]/a").text
                i = 1
            except:  # try other xpath if dysfunctional
                self.license_ = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[1]/div[2]/p[1]/p").text
                i = 1

        self.views = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[4]/div[2]/div[1]/div/div[2]/h1").text
        self.downloads = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[4]/div[2]/div[1]/div/div[3]/h1").text
        self.download_per_view = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[5]/div[4]/div[2]/div[1]/div/div[4]/h1").text
        self.download_size = driver.find_element("xpath", "//*[@id='site-content']/div[2]/div[2]/div/div[1]/div/a/button/span").text.split()[1:]
        
        # fix formatting of scraped string of download size
        for i in range(len(self.download_size)):
            if "(" in self.download_size[i]:
                self.download_size[i] = self.download_size[i].replace("(","")
            elif ")" in self.download_size[i]:
                self.download_size[i] = self.download_size[i].replace(")","")
        self.download_size = " ".join(self.download_size)
        
        # terminate driver
        driver.close()
        driver.quit()

    def print_all(self):
        '''
        This method prints all current attributes (title, usability, upvotes, description, update frequency, 
        data of last update, author, license, views, downloads, download per view, download size) of the dataset.
        '''
        print("---------------------------------------------------------------------------")
        print("Title:", self.title)
        print("Usability:", self.usability)
        print("Upvotes:", self.upvotes)
        print("Description:", self.description)
        print("Update Frequency:", self.update_frequency)
        print("Last Updated:", self.last_updated)
        print("Author:", self.author)
        print("License:", self.license_)
        print("Views:", self.views)
        print("Downloads:", self.downloads)
        print("Download per View:", self.download_per_view)
        print("Download Size:", self.download_size)
        print("URL:", self.url)
        print("---------------------------------------------------------------------------")

    def get_title(self):
        '''
        This method returns the title of the dataset.
        '''
        return self.title

    def get_usability(self):
        '''
        This method returns the usability of the dataset. 
        '''
        return self.usability

    def get_upvotes(self):
        '''
        This method returns the upvotes of the dataset.
        '''
        return self.get_upvotes
    
    def get_description(self):
        '''
        This method returns the description of the dataset.
        '''
        return self.description

    def get_update_frequency(self):
        '''
        This method returns the update frequency of the dataset.
        '''
        return self.update_frequency

    def get_last_updated(self):
        '''
        This method returns the last updated time of the dataset.
        '''
        return self.last_updated

    def get_author(self):
        '''
        This method returns the author of the dataset.
        '''
        return self.author

    def get_license(self):
        '''
        This method returns the license of the dataset.
        '''
        return self.license_

    def get_views(self):
        '''
        This method returns the views of the dataset.
        '''
        return self.views

    def get_downloads(self):
        '''
        This method returns the number of downloads of the dataset.
        '''
        return self.downloads

    def get_download_per_view(self):
        '''
        This method returns the ratio of the download per view of the dataset.
        '''
        return self.download_per_view
    
    def get_download_size(self):
        '''
        This method returns the download size of the dataset.
        '''
        return self.download_size
    
    def get_url(self):
        '''
        This method returns the url of the dataset.
        '''
        return self.url

if __name__ == "__main__":
    driver_path = "/Users/taekwan/Desktop/Web-Scraping-Kaggle-Datasets/webdriver/chromedriver"

    sample1 = ScrapeKaggle("https://www.kaggle.com/datasets/matthieugimbert/french-bakery-daily-sales", driver_path)
    sample1.scrape()
    sample1.print_all()

    sample2 = ScrapeKaggle("https://www.kaggle.com/datasets/ankitmishra0/narendra-modi-speeches", driver_path)
    sample2.scrape()
    sample2.print_all()
    
    sample3 = ScrapeKaggle("https://www.kaggle.com/datasets/thedevastator/housing-prices-and-access-to-cannabis", driver_path)
    sample3.scrape()
    sample3.print_all()

    sample4 = ScrapeKaggle("https://www.kaggle.com/datasets/dilwong/flightprices", driver_path)
    sample4.scrape()
    sample4.print_all()

    sample5 = ScrapeKaggle("https://www.kaggle.com/datasets/mattop/world-series-2022-baseball-phillies-vs-astros", driver_path)
    sample5.scrape()
    sample5.print_all()





