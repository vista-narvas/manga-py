from src.provider import Provider


class MangaOnNet(Provider):

    def get_archive_name(self) -> str:
        return 'vol_' + self.get_chapter_index()

    def get_chapter_index(self) -> str:
        selector = r'(?:vol\-?(\d+))?(?:\-ch\-?(\d+))'
        ch = self.get_current_chapter()
        re = self.re.search(selector, ch)
        if re:
            re = re.groups()
            return '{}-{}'.format(
                0 if not re[0] else re[0],
                re[1]
            )
        selector = r'.+-(\d+)'
        re = self.re.search(selector, ch)
        return '0-{}'.format(re.group(1))

    def get_main_content(self):
        name = self._storage.get('manga_name', self.get_manga_name())
        url = '{}/manga-info/{}'.format(self.get_domain(), name)
        return self.http_get(url)

    def get_manga_name(self) -> str:
        url = self.get_url()
        if url.find('read-online') > 0:
            url = self.html_fromstring(url, '.back-info a', 0).get('href')
        return self.re.search(r'/manga\-info/([^/]+)', url).group(1)

    def get_chapters(self):
        return self.document_fromstring(self.get_storage_content(), '.list-chapter li > a')

    def get_files(self):
        items = self.html_fromstring(self.get_current_chapter(), '#list-img img')
        return [i.get('src') for i in items]

    def get_cover(self) -> str:
        return self._get_cover_from_content('.cover img')


main = MangaOnNet
