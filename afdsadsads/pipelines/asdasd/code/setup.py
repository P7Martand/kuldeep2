from setuptools import setup, find_packages
setup(
    name = 'asdasd',
    version = '1.0',
    packages = find_packages(include = ('asdasd*', )) + ['prophecy_config_instances.asdasd'],
    package_dir = {'prophecy_config_instances.asdasd' : 'configs/resources/asdasd'},
    package_data = {'prophecy_config_instances.asdasd' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = asdasd.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
