from game_helper.helper import y


def get_files_from_yadisk(folder_path):
    meta = (y.get_meta(folder_path))
    fields = meta.FIELDS
    embedded = fields['embedded'].FIELDS
    items = embedded['items']
    zero_item = items[0].FIELDS
    name_zero_item = zero_item['name']
    file = zero_item['file']
    files = y.listdir(folder_path)

    return [file['name'] for file in files]
