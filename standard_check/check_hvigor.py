#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2024-2024 Huawei Device Co., Ltd.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import sys
import hashlib
import json5


class HvigorChecker:

    HVIGOR_BASE_VERSION = [
        '4.0.5',
        '4.0.9',
        '5.0.0'
    ]
    
    def __init__(self, suite_name):
        self._current_dir = os.path.dirname(os.path.realpath(__file__))
        self._suite_name = suite_name
        self._xts_root_dir = os.path.realpath(os.path.join(self._current_dir, '../..', suite_name))

    def get_file_md5(self, file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_hvigor_version(self, json_file):
        with open(json_file, 'r') as f:
            data = json5.load(f)
            version = data.get('hvigorVersion')
            if version:
                return version
            return data.get('modelVersion')

    def output_unmatched_project(self, prject_list, filename):
        print("")
        print("Error: The {} in the following directory does not meet the requirements:".format(filename))
        for prj in prject_list:
            print(prj[0], prj[1])

    def check_hvigor_wrapper_js(self, hvigor_prj_list):
        unmatch_info = []
        baseline_file = os.path.join(self._current_dir, 'hvigor-wrapper.js')
        baseline_md5 = self.get_file_md5(os.path.join(baseline_file))
        for dir in hvigor_prj_list:
            filename = os.path.join(dir, 'hvigor', 'hvigor-wrapper.js')
            if not os.path.exists(filename):
                return True
            md5 = self.get_file_md5(filename)
            if md5 != baseline_md5:
                unmatch_info.append((md5, filename))

        if len(unmatch_info):
            self.output_unmatched_project(unmatch_info, 'hvigor-wrapper.js')
            print('Please copy from {}'.format(baseline_file))
            return False
        return True

    def check_hvigor_version(self, hvigor_prj_list):
        unmatch_prj_list = []
        for dir in hvigor_prj_list:
            filename = os.path.join(dir, 'hvigor', 'hvigor-config.json5')
            version = self.get_hvigor_version(filename)
            if version not in self.HVIGOR_BASE_VERSION:
                unmatch_prj_list.append((version, filename))

        if len(unmatch_prj_list):
            self.output_unmatched_project(unmatch_prj_list, 'hvigor-config.json5')
            print("Plesse use {}".format(self.HVIGOR_BASE_VERSION))
            return False
        return True

    def check_hvigorw_bat(self, hvigor_prj_list):
        unmatch_info = []
        baseline_file = os.path.join(self._current_dir, 'hvigorw.bat')
        baseline_md5 = self.get_file_md5(os.path.join(baseline_file))
        for dir in hvigor_prj_list:
            filename = os.path.join(dir, 'hvigorw.bat')
            if not os.path.exists(filename):
                return True
            md5 = self.get_file_md5(filename)
            if md5 != baseline_md5:
                unmatch_info.append((md5, filename))

        if len(unmatch_info):
            self.output_unmatched_project(unmatch_info, 'hvigorw.bat')
            print('Please copy from {}'.format(baseline_file))
            return False
        return True

    def get_hvigor_prject_list(self):
        hvigor_prj_list = []
        for root, dirs, files in os.walk(self._xts_root_dir):
            if '.cxx' in dirs:
                dirs.remove('.cxx')
            for dir in dirs:
                if dir == 'hvigor':
                    hvigor_prj_list.append(root)
        return hvigor_prj_list


def main():
    suite_name = ""
    if 'XTS_SUITENAME' in os.environ:
        suite_name = os.environ.get('XTS_SUITENAME')
    elif 'xts_suitename' in os.environ:
        suite_name = os.environ.get('xts_suitename')
    else:
        suite_name = sys.argv[1]

    obj = HvigorChecker(suite_name)

    hvigor_prj_list = obj.get_hvigor_prject_list()

    js_valid = obj.check_hvigor_wrapper_js(hvigor_prj_list)
    json_valid = obj.check_hvigor_version(hvigor_prj_list)
    bat_valid = obj.check_hvigorw_bat(hvigor_prj_list)

    if not js_valid or not json_valid or not bat_valid:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
