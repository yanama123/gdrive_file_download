import setuptools


# Fields marked as "Optional" may be commented out.
setuptools.setup(
    name="Gdrive_file_download",  # Required
    version=1.0,  # Required
    author="Anjan",  # Optional
    description="Gdrive_file_download",  # Required
    packages=setuptools.find_packages(exclude=['contrib', 'docs']),  # Required
    include_package_data=True  # Optional
    )