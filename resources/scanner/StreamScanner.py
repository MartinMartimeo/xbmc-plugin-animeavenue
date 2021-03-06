#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import re
from resources.scanner.BasicScanner import BasicScanner, NoContentProvided
from resources.scanner.VideoScanner import VideoScanner

__author__ = 'MartinMartimeo <martin@martimeo.de>'
__date__ = '03.02.13 - 11:37'


class UpcomingEpisode(NoContentProvided):
    pass


class StreamScanner(BasicScanner):
    """
        Scans thorugh the streams of an episode and tries to extract video urls
    """

    def __init__(self, tag, type, episode):
        super(StreamScanner, self).__init__("http://www.animeavenue.net/%s-%s-%s/" % (tag, type, episode))

        # Our Regex
        self.re = re.compile(
            r'(?:<div[\s\n\r]*class=[\'"]entry.*[\'"].*>[\s\n\r]*<p>|<div[\s\n\r]*class=[\'"]postTabs_divs.*[\'"].*>[\s\n\r]*<span[\s\n\r]*.*>.*(?:<br[\s\n\r]*/>)?)[\s\n\r]*<iframe[\s\n\r]*[^>]*(?:SRC|src)=[\'"]([^\'">]+)[\'"][^>]*>')

    def parse(self, content):
        """
            Parses the request return
            :param content: Content from Request
        """
        rtn = []
        matches = self.re.findall(content)

        # Try urlresolver
        import urlresolver

        sources = [urlresolver.HostedMediaFile(url=url) for url in matches]
        for source in urlresolver.filter_source_list(sources):
            web_url = source.resolve()
            if web_url:
                rtn.append(web_url)
        if rtn:
            return rtn

        # Try own approach
        for url in matches:
            mp = VideoScanner(url)

            # Try to add video url
            try:
                rtn.extend(mp.run())
            except NoContentProvided:
                continue

            # Just Loop until a mp4/flv/avi has been found
            if rtn:
                break

        if not rtn and "/upcoming.jpg" in content:
            raise UpcomingEpisode()

        return rtn


if __name__ == "__main__":
    gs = StreamScanner("zetsuen-no-tempest", "episode", "20")
    iframes = gs.run()
    print "%s" % iframes