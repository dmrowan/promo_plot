from setuptools import setup, find_packages
from distutils.util import convert_path

setup(name = "promoplot",
    version = '1.2.0',
    description = "Code for Promo Corner Plot",
    author = "Dom Rowan",
    author_email = "",
    url = "https://github.com/dmrowan/promoplot",
    packages = find_packages(include=['promoplot', 'promoplot.*']),
    package_data = {'promoplot':['ad_images/**/*']},
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
