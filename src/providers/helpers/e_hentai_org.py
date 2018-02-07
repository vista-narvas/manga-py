from src.provider import Provider


class EHentaiOrg:
    provider = None

    def __init__(self, provider: Provider):
        self.provider = provider

    def get_pages_count(self, parser):
        selector = '.gtb table.ptt td[onclick] > a'
        paginate = parser.cssselect(selector)
        max_idx = 0
        for i in paginate:
            idx = self.provider.re.search('\\?p=(\\d+)', i.get('href'))
            max_idx = max(max_idx, int(idx.group(1)))
        return max_idx

    def parse_background(self, image):
        selector = 'background.+?url\\([\'"]?([^\\s]+?)[\'"]?\\)'
        url = self.provider.re.search(selector, image.get('style'))
        return self.provider.http().normalize_uri(url.group(1))

    def get_cover_from_content(self, selector):
        if self.provider.get_storage_content():
            content = self.provider.get_storage_content()
            image = self.provider.document_fromstring(content, selector)
            if image and len(image):
                return self.parse_background(image[0])

    def get_image(self, i):
        url = i.get('href')
        src = self.provider.html_fromstring(url, 'img#img', 0)
        return src.get('src')

    def get_url(self):
        url = self.provider.get_url()
        if url.find('?') > 0:
            url = url[:url.find('?')]
        return url
