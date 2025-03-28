from setuptools import setup, find_packages
from distutils.util import convert_path

setup(name = "promo_plot",
    version = 0.1,
    description = "Code for Promo Corner Plot",
    author = "Dom Rowan",
    author_email = "",
    url = "https://github.com/dmrowan/promo_plot",
    packages = find_packages(include=['promo_plot', 'promo_plot.*']),
    package_data = {'promo_plot':['ad_images/*']},
    include_package_data = True,
    classifiers=[
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=["matplotlib", "numpy", "pandas", "scipy"]
)
