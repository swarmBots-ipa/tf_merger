from setuptools import setup

package_name = 'tf_merger'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ipa326',
    maintainer_email='ragesh.ramachandran@ipa.fraunhofer.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf_merger = tf_merger.tf_merger:main',
            'tf_repub = tf_merger.tf_repub:main',
            'test_tf_merger = tf_merger.test_tf_merger:main'
        ],
    },
)
