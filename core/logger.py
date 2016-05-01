#!/usr/bin/env python
# encoding: utf-8
"""
Do all the logging for this system.
 
=======================================================================
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
=======================================================================
"""


from datetime import datetime
import os


class Logger:
    def __init__(self, sc, tcfg, result):
        self.sc = sc
        self.tcfg = tcfg
        self.result = result

    def write2html(self):
        content = []

        content.append('''
<html>
<head>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js'></script>
  <script src='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js'></script>
  <style>
    body {padding:40px;line-height:2em}
    table {font-size:0.9em}
  </style>
</head>
<body>
<h1>Results of Test Automation</h1>
<div class='table-responsive'>
''')

        content.append('''
  <div class='panel panel-primary'>
    <div class='panel-heading'>
        <h3 class='panel-title'>Summary</h3>
    </div>
    <div class='panel-body'>
    ''')
    
        content.append("<b>Start Time</b>: {}<br>".format(str(self.tcfg.startts)[:19]))
        endts = datetime.now()
        content.append("<b>End Time</b>: {}<br>".format(str(endts)[:19]))
        content.append("<b>Duration</b>: {}<br>".format(str(endts-self.tcfg.startts)[:-7]))
        content.append("<b>Command</b>: {}<br>".format(self.tcfg.command))
        content.append("<b>Directory</b>: {}<br>".format(self.tcfg.path))
        content.append("<b>User</b>: {}<br>".format(self.tcfg.username))
        content.append("<b>No. of Tests Executed</b>: {}<br>".format(self.result.testsRun))
        num_passed = '<button class="btn btn-xs btn-success" type="button">Passed <span class="badge">{:d}</span></button>'.format(self.result.testsRun - len(self.result.skipped) - len(self.result.failures))
        num_failed = '<button class="btn btn-xs btn-danger" type="button">Failed <span class="badge">{:d}</span></button>'.format(len(self.result.failures))
        num_skipped = '<button class="btn btn-xs btn-info" type="button">Skipped <span class="badge">{:d}</span></button>'.format(len(self.result.skipped))
        content.append("<b>Verdict</b>: {} {} {}<br>".format(num_passed, num_failed, num_skipped))

        content.append('''
    </div>
  </div>
  ''')

        content.append('''
  <table class='table table-bordered table-striped'>
    <thead>
        <tr class='alert alert-danger'>
          <th>Failed Test</th>
          <th>Traceback</th>
        </tr>
    </thead>
    <tbody>
    ''')
        for tc in self.result.failures:
            content.append("<tr class='alert alert-danger'>")
            content.append("  <td>{}</td><td>{}</td>".format(tc[0], tc[1].replace("\n", "<br>")))
            content.append("</tr>")
        content.append('''
    </tbody>
  </table>
  ''')

        content.append('''
  <table class='table table-bordered table-striped'>
    <thead>
        <tr class='alert alert-info'>
          <th>Skipped Test</th>
          <th>Remarks</th>
        </tr>
    </thead>
    <tbody>
    ''')
        for tc in self.result.skipped:
            content.append("<tr class='alert alert-info'>")
            content.append("  <td>{}</td><td>{}</td>".format(tc[0], tc[1].replace("\n", "<br>")))
            content.append("</tr>")
        content.append('''
    </tbody>
  </table>
  ''')

        content.append('''
</div>
</body>
</html>
''')

        with open('out.htm', 'w') as f:
            f.write("\n".join(content))
