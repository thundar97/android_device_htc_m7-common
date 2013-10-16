# Copyright (C) 2012 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Change ro.product.device from m7whatever to m7"""

import common

def RunPropFix(self):
    self.script.AppendExtra('ui_print("Implementing PRODUCT_DEVICE override for camera");')
    self.script.AppendExtra('package_extract_file("system/bin/device_prop.sh", "/tmp/device_prop.sh");')
    self.script.AppendExtra('set_perm(0, 0, 0777, "/tmp/device_prop.sh");')
    self.script.AppendExtra('run_program("/tmp/device_prop.sh");')

def FullOTA_InstallEnd(self):
   RunPropFix(self)

def IncrementalOTA_InstallEnd(self):
   RunPropFix(self)

