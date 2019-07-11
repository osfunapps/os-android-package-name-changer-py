from distutils.core import setup

setup(
    name='os-android-package-name-changer',
    packages=['os_android_package_name_changer'],
    version='1.04',
    license='MIT',
    description='will change the package name of an android app programmatically (dynamically)',
    author='Oz Shabat',
    author_email='osfunapps@gmail.com',
    url='https://github.com/osfunapps',
    download_url='https://github.com/osfunapps/os-xcode-tools-py/archive/v1.01.tar.gz',
    keywords=['python', 'osfunapps', 'android', 'package', 'automation'],
    install_requires=['ostools'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
