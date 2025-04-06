def get_extension_folder(filename):
    ext = filename.split(".")[-1].lower()
    if ext in ['jpg', 'png', 'gif']:
        return 'Images'
    elif ext in ['txt', 'md', 'doc']:
        return 'TextFiles'
    elif ext in ['mp4', 'mov']:
        return 'Videos'
    else:
        return 'Others'
