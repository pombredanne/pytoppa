import os
from jinja2 import Environment, PackageLoader


class PackageData(object):
    """With debian package data"""
    files = [
        'source/format',
        'changelog',
        'clean',
        'compat',
        'control',
        'copyright',
        'docs',
        'rules',
    ]

    def __init__(self, path, context):
        self._path = path
        self._context = context
        self.destination = os.path.join(self._path, 'debian')
        self._env = Environment(loader=PackageLoader('pytoppa'))

    def _create_dirs(self):
        """Create all dirs"""
        os.makedirs(self.destination)
        self._sources_dir = os.path.join(self.destination, 'sources')
        os.makedirs(self._sources_dir)

    def _render_file(self, path):
        """Render file"""
        template = self._env.get_template(path)
        full_path = os.path.join(self.destination, path)
        with open(full_path, 'w') as out:
            out.write(template.render(**self._context))

    def __enter__(self):
        """Create debian package data"""
        self._create_dirs()