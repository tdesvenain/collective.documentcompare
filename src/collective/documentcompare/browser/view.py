from plone import api
from Products.Five.browser import BrowserView
from plone.namedfile.utils import set_headers, stream_data
from collective.documentcompare.api import get_files_comparison


class CompareDocuments(BrowserView):

    def __call__(self):
        uids, pathes = self.request.get('uids', ''), self.request.get('pathes', '')
        if pathes and len(pathes) != 2 or uids and len(uids) != 2:
            raise ValueError("You have to compare two documents")

        if uids:
            file1, file2 = [api.content.get(UID=uids[0]),
                            api.content.get(UID=uids[1])],
        elif pathes:
            file1, file2 = [api.content.get(path=pathes[0]),
                            api.content.get(path=pathes[1])],

        filev1, filev2 = sorted([file1, file2], key=lambda x: x.modified())
        named_file_diff = get_files_comparison(filev2.file, filev1.file)
        set_headers(named_file_diff,
                    self.request.response, filename=named_file_diff.filename)
        return stream_data(named_file_diff)
