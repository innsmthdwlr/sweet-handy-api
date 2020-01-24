import os.path
from auth import Auth
from picture_repository import PictureRepository
from picture_transform import PictureTransformator
from diabetes_registry import DiabetesRegistry
from meal_parser import MealParser

def iterate_pictures(cwd):
    for _, _, files in os.walk(cwd):
        for file in files:
            if not file.endswith(".json"):
                yield os.path.join(cwd, file)

def update_registry(registry_file_path, meals_data):
    meal_parser = MealParser(registry_file_path)

    print(meal_parser.data)

    for meal in meals_data:
        meal_parser.create_meal(meal)
    meal_parser.update_registry_file()

def upload_files_to_dropbox(cwd):
    optimus_prime = PictureTransformator()
    diabetes_registry = DiabetesRegistry(cwd)
    picture_data = []
    registry_file_path = diabetes_registry.download("registry.json")

    # process all files in temp
    for picture_path in iterate_pictures(os.path.join(cwd, 'temp')):
        single_picture_data = optimus_prime.resize(picture_path)
        picture_data.append(single_picture_data)
        try:
            diabetes_registry.upload(picture_path, single_picture_data[0])
            os.remove(picture_path)
        except ValueError:
            print('Could not upload')
            raise

    update_registry(registry_file_path, picture_data)

    # upload registry file
    registry_file = os.path.join(registry_file_path)
    diabetes_registry.upload(registry_file, "registry.json")
    os.remove(registry_file)

def get_pictures_from_google(cwd, SCOPES):
    # get files
    auth = Auth(cwd, SCOPES)
    diabetes_drive = PictureRepository(auth.get_credentials())

    file_names = diabetes_drive.get_file_list()
    for k, v in file_names.items():
        file_name, file_id = k, v
        diabetes_drive.download_file(file_id, file_name, os.path.join(cwd, 'temp'))
        diabetes_drive.delete_file(file_id)

def main():
    # delete the file token.pickle after modifying the SCOPE
    SCOPES = ['https://www.googleapis.com/auth/drive']
    cwd = os.getcwd()
    get_pictures_from_google(cwd, SCOPES)
    # upload_files_to_dropbox(cwd)

    update_registry(os.path.join(cwd, 'temp', 'registry.json'), [])


if __name__ == '__main__':
    main()
