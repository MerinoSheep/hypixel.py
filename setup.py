from setuptools import setup

setup(name='hypixel-python',
      version='0.3.2',
      description='This is a simple, unofficial library for getting values from the public Hypixel-API in Python.',
      url='https://github.com/SnuggIes/hypixel-python',
      author='Snuggle',
      author_email='snuggle@sprinkly.net',
      packages=['hypixel'],
      install_requires=['requests'],
      python_requires='>=3',
      zip_safe=False)