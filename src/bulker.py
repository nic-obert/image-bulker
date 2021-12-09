import os
from typing import Tuple
from werkzeug.datastructures import FileStorage

from werkzeug.utils import secure_filename


def bulk_file(file: FileStorage, final_size: int, save_path: str) -> Tuple[str, int]:
    content: bytes = file.read()
    size = len(content)
    filename = secure_filename(file.filename)

    if size < final_size:
        difference = final_size - size

        print(f'Adding {difference} bytes to {filename}')

        content += b'\x84' * difference
        file.seek(0)
        file.write(content)    

    with open(os.path.join(save_path, filename), 'wb') as f:
        f.write(content)

    print(f'{filename} saved in {save_path}: {len(content)} bytes')

    return filename, size

