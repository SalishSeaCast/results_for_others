# Copyright 2013-2014 The Salish Sea MEOPAR Contributors
# and The University of British Columbia

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Salish Sea NEMO IPython Notebook collection README generator
"""
import datetime
import json
import os
import re


nbviewer = 'http://nbviewer.ipython.org/urls'
repo = 'bitbucket.org/salishsea/results/raw/tip'
repo_dir = 'preliminary'
url = os.path.join(nbviewer, repo, repo_dir)
title_pattern = re.compile('#{1,6} ?')
readme = """The IPython Notebooks in this directory present preliminary
results and analysis from the Salish Sea MEOPAR project NEMO model.

The links below are to static renderings of the notebooks via
[nbviewer.ipython.org](http://nbviewer.ipython.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

"""
notebooks = (fn for fn in os.listdir('./') if fn.endswith('ipynb'))
for fn in notebooks:
    readme += '* ##[{fn}]({url}/{fn})  \n    \n'.format(fn=fn, url=url)
    with open(fn, 'rt') as notebook:
        contents = json.load(notebook)
    first_cell_type = contents['worksheets'][0]['cells'][0]['cell_type']
    if first_cell_type in 'markdown raw'.split():
        desc_lines = contents['worksheets'][0]['cells'][0]['source']
        for line in desc_lines:
            suffix = ''
            if title_pattern.match(line):
                line = title_pattern.sub('**', line)
                suffix = '**'
            if line.endswith('\n'):
                readme += (
                    '    {line}{suffix}  \n'
                    .format(line=line[:-1], suffix=suffix))
            else:
                readme += (
                    '    {line}{suffix}  '.format(line=line, suffix=suffix))
        readme += '\n' * 2
license = """
##Copyright

These notebooks and files are copyright {this_year}
by the [Salish Sea MEOPAR Project Contributors](https://bitbucket.org/salishsea/docs/src/tip/CONTRIBUTORS.rst)
and The University of British Columbia.

Please contact Dr. Susan Allen <sallen@eos.ubc.ca> for permission
to use or cite any of the contents of this repository.
""".format(this_year=datetime.date.today().year)
with open('README.md', 'wt') as f:
    f.writelines(readme)
    f.writelines(license)
