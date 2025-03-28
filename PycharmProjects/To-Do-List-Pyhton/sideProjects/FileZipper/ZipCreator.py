import zipfile
import pathlib

def make_archive(filepaths, dest_dir, archive_name):
    dest_path = pathlib.Path(dest_dir, archive_name + ".zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
