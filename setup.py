from setuptools import setup, find_packages
setup(
    name = "nose-html",
    version = '1.1',
    author = "Wai Yip Tung, The SIO2 Project Team",
    author_email = 'sio2@sio2project.mimuw.edu.pl',
    description = "HTML report generation plugin for nose",
    url = 'https://github.com/sio2project/nose-html',
    license = 'BSD',

    packages = find_packages(),

    install_requires = [
        'nose >= 0.11.1',
    ],

    entry_points = {
        'nose.plugins': [
            'html = nose_html:HTML',
        ],
    }
)

