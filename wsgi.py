# Copyright (c) 2018-2020 Pepijn Oomen <oomen@piprograms.com>
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask,render_template
from os.path import isfile
from os import remove

application = Flask(__name__)

@application.route('/')
def index():
  if isfile('.status'):
    with open('.status') as f:
      status = int(f.read())
  else:
    status = 200
  return render_template('index.html', status='Hello World!'), status

@application.route('/status/<status>')
def status(status):
  status = status.upper()
  with open('.status', 'w') as f:
    f.write(status)
  return render_template('index.html', status='Status code set to: %s' % status)

if __name__ == '__main__':
    application.run(debug = True)
