import os


def save_uploaded_file(file, upload_folder="uploads"):
    """Save the uploaded file to the server"""
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    return file_path
