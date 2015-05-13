# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


readme = open('README.md').read()

setup(
    name='RebootRaspberryOnConnectionLost',
    version='0.1',
    description=('Reboots the raspberry if the connection was lost '
                 'for too long'),
    long_description=readme,
    author='Romain Endelin',
    author_email='romain.endelin@mines-telecom.fr',
    url='https://github.com/pawmint/reboot-raspberry-on-connection-lost',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.6.2'
    ],
    entry_points = {
        'console_scripts': [
            'reboot_on_connection_lost=reboot_on_connection_lost.reboot:main'
        ]
    },
    license='Copyright',
    zip_safe=True,  # To be verified
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Environment :: Console',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering',
    ],
)
