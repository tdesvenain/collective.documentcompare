import tempfile
from pyodcompare import DocumentCompare
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.documentfusion.converter import _store_namedfile_in_fs_temp,\
    _get_blob_from_fs_file
from collective.documentfusion.interfaces import ISOfficeSettings


def get_files_comparison(namedfile_v2, namedfile_v1):
    """Get a namedfile which is a comparison between two namedfiles
    """
    tmp_v2_filepath = _store_namedfile_in_fs_temp(namedfile_v2)
    tmp_v1_filepath = _store_namedfile_in_fs_temp(namedfile_v1)
    tmp_diff_file_path = tempfile.mktemp(suffix='--%s.odt' % namedfile_v2.filename)
    settings = getUtility(IRegistry).forInterface(ISOfficeSettings)
    compare = DocumentCompare(listener=(settings.host, settings.port))
    compare.compare(tmp_v2_filepath, tmp_v1_filepath, tmp_diff_file_path)
    return _get_blob_from_fs_file(tmp_diff_file_path)
