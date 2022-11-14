import kaggle  # import kaggle api module 

def set_config(username):
    '''
    This function links the file with the Kaggle username (in ~/.kaggle/kaggle.json) for API authentication.
    '''
    api = kaggle.api
    api.get_config_value(username)
    return

def max_search(keyword):
    '''
    This function takes the keyword as the parameter and returns the total number of datasets associated with the keyword on Kaggle.
    '''
    max_search_num = 0
    i = 1
    while True:
        try:
            datasets = kaggle.api.datasets_list(search = keyword, page = i)
            if datasets == []:  # if page doesn't contain any datasets, end the loop
                break
            i += 1  # increase page number by 1
            max_search_num += len(datasets)  # get sum of all datasets in all non-empty pages
        except:
            break
    return max_search_num

def search(keyword, num_datasets):
    '''
    This function takes two parameters: a search keyword as the first parameter and the desired number of datasets to be scraped.
    Then it returns the datasets. 
    '''
    max_search_num = max_search(keyword)  # get the maximum number of datasets associated with keyword
    if num_datasets > max_search_num:  # if user input for desired number of datasets exceeds the maximum number of datasets
        print("Since the desired number of datasets exceeds the current total number of datasets, the current total number of datasets ({}) will be returned".format(max_search_num))
        num_datasets = max_search_num  # examine the maximum number of datasets

    if num_datasets <= 20:  # if desired number of datasets less than or equal to 20 (each page contains 20 datasets)
        # get the desired number of datasets from the first page
        datasets = kaggle.api.datasets_list(search = keyword, page = 1)[:num_datasets]
    else:  # if desired number of datasets greater than 20
        # get 20 datasets from the first page
        datasets = kaggle.api.datasets_list(search = keyword, page = 1)
        num_pages = num_datasets // 20 + 1  # total number of pages to be scraped
        remainder = num_datasets % 20  # number of datasets to be scraped from last page
        for i in range(2, num_pages):  # first page already scraped, so start from second page
            # scrape all datasets starting from second page (if applicable)
            datasets += kaggle.api.datasets_list(search = keyword, page = i)
        # scrape remaining datasets from last page (if only some datasets are to be scraped from the last page)
        datasets += kaggle.api.datasets_list(search = keyword , page = num_pages)[:remainder]        
    return datasets

def get_num_datasets(datasets):
    '''
    This function takes the datasets as the parameter and returns the description of the number of datasets as a string.
    '''
    return 'There are {num} datasets in the list'.format(num=len(datasets))

def get_specific_dataset(datasets, index):
    '''
    This function takes the datasets as the first parameter and the index as the second parameter. 
    It returns the comprehensive, unrefined information about the dataset at the specified index.
    '''
    return datasets[index]

def get_url(dataset):
    '''
    This function takes a dataset as the parameter and returns its url.
    '''
    return dataset['url']

def has_creator(dataset):
    '''
    This function takes a dataset as the parameter and returns True if there is a creator name -- otherwise, False.
    '''
    return dataset['hasCreatorName']

def get_creator(dataset):
    '''
    This function takes a dataset as the parameter and returns the name of its creator.
    '''
    # creator name exists and not empty
    if (has_creator(dataset) == True) and (dataset['creatorNameNullable'] != ''):
        return dataset['creatorNameNullable']
    else:
        return 'There is no available creator name.'

def has_license(dataset):
    '''
    This function takes a dataset as the parameter and returns True if there is a license -- otherwise, False.
    '''
    return dataset['hasLicenseName']

def get_license(dataset):
    '''
    This function takes a dataset as the parameter and returns the license name.
    '''
    # license name exists and not empty
    if (has_license(dataset) == True) and (dataset['licenseNameNullable'] != ''):
        return dataset['licenseNameNullable']
    else:
        return 'There is no available license name.'

def has_title(dataset):
    '''
    This function takes a dataset as the parameter and returns True if there is a title -- otherwise, False.
    '''
    return dataset['hasTitle']

def get_title(dataset):
    '''
    This function takes a dataset as the parameter and returns the title.
    '''
    # title exists and not empty
    if (has_title(dataset) == True) and (dataset['titleNullable'] != ''):
        return dataset['titleNullable']
    else:
        return 'There is no available title for the dataset.'

def has_usability(dataset):
    '''
    This function takes a dataset as the parameter and returns True if there is a usability -- otherwise, False.
    '''
    return dataset['hasUsabilityRating']

def get_usability(dataset):
    '''
    This function takes a dataset as the parameter and returns its usability.
    '''
    if (has_usability(dataset) == True) and (dataset['usabilityRatingNullable'] != ''):
        return str(round(float(dataset['usabilityRatingNullable']) * 10, 2)) # rounding to 2 decimal places fails when it is 10.00
    else:
        return 'There is no available usability rating for the dataset.'

def has_subtitle(dataset):
    '''
    This function takes a dataset as the parameter and returns True if there is a subtitle -- otherwise, False.
    '''
    return dataset['hasSubtitle']

def get_subtitle(dataset): 
    '''
    This function takes a dataset as the parameter and returns its subtitle.
    '''
    # subtitle exists and not empty
    if (has_subtitle(dataset) == True) and (dataset['subtitle'] != ''):
        return dataset['subtitle']
    else:
        return 'There is no available subtitle.'

def get_last_updated(dataset):
    '''
    This function takes a dataset as the parameter and returns its last updated date.
    '''
    return dataset['lastUpdated']

def get_download_count(dataset):
    '''
    This function takes a dataset as the parameter and returns its download count.
    '''
    return dataset['downloadCount']

def get_view_count(dataset):
    '''
    This function takes a dataset as the parameter and returns its view count.
    '''
    return dataset['viewCount']

def get_vote_count(dataset):
    '''
    This function takes a dataset as the parameter and returns its upvote count.
    '''
    return dataset['voteCount']

def has_download_size(dataset):
    '''
    This function takes a dataset as the parameter and returns True if there is a download size -- otherwise, False.
    '''
    return dataset['hasTotalBytes']

def get_download_size(dataset):
    '''
    This function takes a dataset as the parameter and returns its download size.
    '''
    # download size exists and not empty
    if (has_download_size(dataset) == True) and (dataset['totalBytes'] != ''):
        return dataset['totalBytes']
    else:
        return 'There is no available download size for the dataset.'

def get_tags(dataset):
    '''
    This function takes a dataset as the parameter and returns its tags.
    '''
    tags = []
    for i in range(len(dataset['tags'])):  # for every element in the list of tags
        tags.append(dataset['tags'][i]['nameNullable'])  # tag element assigned to 'nameNullable' in dictionary
    return tags

def print_all(dataset):
    '''
    This function takes a dataset as the parameter and prints its title, subtitle, url, tags, creator name, view count, vote count, download count, usability, last updated date, download size, and license name.
    '''
    print('---------------------------------------------------')
    print(
            'title = {title}\nsubtitle = {subtitle}\nurl = {url}\ntags = {tags}\ncreator = {creator}\nview count = {view_count}\nvote count = {vote_count}\ndownload count = {download_count}\nusability = {usability}\nlast updated = {last_updated}\ndownload size = {download_size}\nlicense = {license_}'.format(title = get_title(dataset),
                     subtitle = get_subtitle(dataset),
                     url = get_url(dataset),
                     tags = get_tags(dataset),
                     creator = get_creator(dataset),
                     view_count = get_view_count(dataset),
                     vote_count = get_vote_count(dataset),
                     download_count = get_download_count(dataset),
                     usability = get_usability(dataset),
                     last_updated = get_last_updated(dataset),
                     download_size = get_download_size(dataset),
                     license_ = get_license(dataset)
                                    )
            )
    print('---------------------------------------------------')

""" # this function could be useful to examine every possible information that can be extracted from Kaggle API
def print_all_fields(dataset):
    dataset_fields_dict = dataset.keys()
    print('------------------------------------------')
    for field in dataset_fields_dict:
        print(f'{field} = {dataset[field]}')
    print('------------------------------------------')
"""

if __name__ == "__main__":
    set_config('taekwanyoon')
    datasets = search('korean', 100)
    
    number = get_num_datasets(datasets)
    print(number)
    
    for i in range(len(datasets)):
        dataset = get_specific_dataset(datasets, i)
        print_all(dataset)
