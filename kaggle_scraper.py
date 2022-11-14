import kaggle
class ScrapeKaggle:
    def __init__(self, username, keyword, num_datasets):
        self.username = username
        self.keyword = keyword
        self.num_datasets = num_datasets
        self.datasets = "Datasets have not been scraped."
        pass
    
    def set_config(self):
        '''
        This method links the file with the Kaggle username in ~/.kaggle/kaggle.json for Kaggle API authentication.
        '''
        api = kaggle.api
        api.get_config_value(self.username)
        return
    
    def search(self):
        '''
        This method returns the datasets of specified keyword and number.
        ''' 
        # first, get the max number of datasets for the specified keyword on Kaggle
        max_search_num = 0
        i = 1
        while True:
            try:
                datasets = kaggle.api.datasets_list(search = self.keyword, page = i)
                if datasets == []:  # if page doesn't contain any datasets, end loop
                    break
                i += 1  # next page
                max_search_num += len(datasets)  # get sum of all datasets in all non-empty pages
            except:  # if any errors, end loop
                break

        if self.num_datasets > max_search_num:  # if desired number of datasets exceeds the max number of datasets
            print("Since the desired number of datasets exceeds the total number of datasets on Kaggle, the total number of datasets ({}) will be returned".format(max_search_num))
            num_datasets = max_search_num  # examine the maximum number of datasets
        if self.num_datasets <= 20:  # if desired number of datasets less than or equal to 20 (each page contains 20 datasets)
            # get desired number of datasets from first page
            datasets = kaggle.api.datasets_list(search = self.keyword, page = 1)[:self.num_datasets]
        else:  # if desired number of datasets greater than 20
            # get 20 datasets from first page
            datasets = kaggle.api.datasets_list(search = self.keyword, page = 1)
            num_pages = self.num_datasets // 20 + 1  # total number of pages to be scraped
            remainder = self.num_datasets % 20  # number of datasets to be scraped from last page
            for i in range(2, num_pages):  # first page already scraped, so start from second 
                # scrape all datasets starting from second page (if applicable)
                datasets += kaggle.api.datasets_list(search = self.keyword, page = i)
            # scrape remaining datasets from last page (if only some datasets are to be scraped from last page)
            datasets += kaggle.api.datasets_list(search = self.keyword, page = num_pages)[:remainder]
        self.datasets = datasets
        return
    
    def get_num_datasets(self):
        '''
        This method returns the description of the number of datasets as a string.
        '''
        return str(len(self.datasets))
    
    def get_specific_dataset(self, index):
        '''
        This method takes the index as a parameter.
        It returns the unrefined information about the dataset at the specified index.
        '''
        return self.datasets[index]
    
    def get_url(self, dataset):
        '''
        This method returns the url of the instantiated dataset.
        '''
        return dataset['url']
    
    def get_creator(self, dataset):
        '''
        This method takes a dataset as the parameter and returns the name of its creator.
        '''
        # creator name exists and not empty
        if (dataset['hasCreatorName'] == True) and (dataset['creatorNameNullable'] != ''):
            return dataset['creatorNameNullable']
        else:
            return 'There is no available creator name.'

    def get_license(self, dataset):
        '''
        This method takes a dataset as the parameter and returns the license name.
        '''
        # license name exists and not empty
        if (dataset['hasLicenseName'] == True) and (dataset['licenseNameNullable'] != ''):
            return dataset['licenseNameNullable']
        else:
            return 'There is no available license name.'

    def get_title(self, dataset):
        '''
        This method takes a dataset as the parameter and returns the title.
        '''
        # title exists and not empty
        if (dataset['hasTitle'] == True) and (dataset['titleNullable'] != ''):
            return dataset['titleNullable']
        else:
            return 'There is no available title for the dataset.'

    def get_usability(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its usability.
        '''
        if (dataset['hasUsabilityRating'] == True) and (dataset['usabilityRatingNullable'] != ''):
            return str(round(float(dataset['usabilityRatingNullable']) * 10, 2)) # rounding to 2 decimal places fails when it is 10.00
        else:
            return 'There is no available usability rating for the dataset.'

    def get_subtitle(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its subtitle.
        '''
        # subtitle exists and not empty
        if (dataset['hasSubtitle'] == True) and (dataset['subtitle'] != ''):
            return dataset['subtitle']
        else:
            return 'There is no available subtitle.'

    def get_last_updated(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its last updated date.
        '''
        return dataset['lastUpdated']

    def get_download_count(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its download count.
        '''
        return dataset['downloadCount']

    def get_view_count(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its view count.
        '''
        return dataset['viewCount']
    
    def get_vote_count(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its upvote count.
        '''
        return dataset['voteCount']

    def get_download_size(self, dataset):
        '''
        This method takes a dataset as the parameter and returns its download size.
        '''
        # download size exists and not empty
        if (dataset['hasTotalBytes'] == True) and (dataset['totalBytes'] != ''):
            return dataset['totalBytes']
        else:
            return 'There is no available download size for the dataset.'
    
    def get_tags(self, dataset):
        '''
        This function takes a dataset as the parameter and returns its tags.
        '''

        tags = []
        for i in range(len(dataset['tags'])): # for every element in tag list
            tags.append(dataset['tags'][i]['nameNullable']) # tags element assigned to 'nameNullable' in dictionary
        return tags
    """
    def print_all(self, dataset):
        '''
        This method takes a dataset as the parameter and prints its title, subtitle, url, tags, creator name, view count, vote count, download count, usability, last updated date, download size, and license name.
        '''
        print('------------------------------------------')
        print('title = {title}\nsubtitle = {subtitle}'.format(title = self.get_title(dataset), subtitle = self.get_subtitle(dataset)))
        print('------------------------------------------')
    """
    '''
    def print_all_fields(self, dataset):
        dataset_fields_dict = dataset.keys()
        print('------------------------------------------')
        for field in dataset_fields_dict:
            print(f'{field} = {dataset[field]}')
        print('------------------------------------------')
    '''

    def print_all(self, dataset):
        '''
        This method takes a dataset as the parameter and prints its title, subtitle, url, tags, creator name, view count, vote count, download count, usability, last updated date, download size, and license name.
        '''
        print('------------------------------------------')
        print('title = {title}\nsubtitle = {subtitle}\nurl = {url}\ntags = {tags}\ncreator = {creator}\nview count = {view_count}\nvote count = {vote_count}\ndownload count = {download_count}\nusability = {usability}\nlast updated = {last_updated}\ndownload size = {download_size}\nlicense = {license_}'.format(title = self.get_title(dataset), subtitle = self.get_subtitle(dataset), url = self.get_url(dataset), tags = self.get_tags(dataset), creator = self.get_creator(dataset), view_count = self.get_view_count(dataset), vote_count = self.get_vote_count(dataset), download_count = self.get_download_count(dataset), usability = self.get_usability(dataset), last_updated = self.get_last_updated(dataset), download_size = self.get_download_size(dataset), license_ = self.get_license(dataset)))
        print('------------------------------------------')
        return 

if __name__ == "__main__":
    pass
