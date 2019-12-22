from setuptools import setup, find_packages

setup(name='rpi_ws281x_light_show',
      version='0.0',
      description='Cool animations for led matrixes of the family rpi_ws281x on Raspbian',
      long_description="Cool animations for led matrixes of the family rpi_ws281x on Raspbian",
      keywords='raspberry raspbian matrix rpi_ws281x animations',
      url='http://github.com/RiccardoCereghino/rpi_ws281x_light_show',
      author='Riccardo Cereghino',
      author_email='riccardo.cereghino@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False, install_requires=['numpy']
      )
