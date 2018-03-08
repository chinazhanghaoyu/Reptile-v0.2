class urlmanager(object):
    def __init__(self):
        self.new_urls = set() #no
        self.old_urls = set() #yes
    def has_new_url(self):
        '''

        :param self:
        :return:
        '''
        return self.new_urls_size()!=0
    def get_new_url(self):
        '''

        :param self:
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        '''

        :param self:
        :param url:
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        '''

        :param self:
        :param urls:
        :return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls_url(url)
    def new_url_size(self):
        '''

        :param self:
        :return:
        '''
        return  len(self.new_urls)
    def old_urls_size(self):
        '''

        :param self:
        :return:
        '''
        return len(self.old_urls)