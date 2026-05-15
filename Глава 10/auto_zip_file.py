from pathlib import Path
import zipfile
import pyinputplus

def main():
    '''Осуществляет логику выполнения фунций и чуть чуть интерфейса'''
    location_file = pyinputplus.inputFilename(prompt='Какой файл вы хотите сохранить в виде копии архива?\n')
    zipping(location_file)

def zipping(location_file):
    '''Осуществляет всю работу'''
    zip_file_dir = Path.cwd()/'zip_save'
    zip_file_dir.mkdir(exist_ok=True)
    location_zip_file = Path(location_file).stem + '.zip'
    with zipfile.ZipFile(zip_file_dir/location_zip_file, 'w') as copy_file:
        copy_file.write(location_file, compress_type=zipfile.ZIP_DEFLATED)

main()