from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setup(
  name = 'timelog',         # How you named your package folder (MyLib)
  long_description = long_description,
  long_description_content_type = "text/markdown",
  packages = ['timelog'],   # Chose the same as "name"
  package_dir={'timelog': 'timelog'},
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A lightweight timestring generator for logging',   # Give a short description about your library
  author = 'Mohamed Abdelhack',                   # Type in your name
  author_email = 'mohamed.abdelhack.37a@kyoto-u.jp',      # Type in your E-Mail
  url = 'https://github.com/mabdelhack/timelog',   # Provide either the link to the package's github or website
  #download_url = 'https://github.com/mabdelhack/timelog/archive/refs/tags/v_02.tar.gz',    # I explain this later on
  keywords = ['timestamp', 'timestring', 'logging'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)