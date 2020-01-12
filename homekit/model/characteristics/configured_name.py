#
# Copyright 2018 Joachim Lusiardi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from homekit.model.characteristics import CharacteristicsTypes, CharacteristicFormats, AbstractCharacteristic, \
    CharacteristicPermissions


class ConfiguredNameCharacteristic(AbstractCharacteristic):
    """
    Defined on page XXX  (look https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts instead)
    """

    def __init__(self, iid):
        AbstractCharacteristic.__init__(self, iid, CharacteristicsTypes.CONFIGURED_NAME, CharacteristicFormats.string)
        self.maxLen = 64
        self.description = 'Configured Name'
        # TODO notify is missing here
        self.perms = [CharacteristicPermissions.paired_write, CharacteristicPermissions.paired_read]


class ConfiguredNameCharacteristicMixin(object):
    def __init__(self, iid):
        self._configuredNameCharacteristic = ConfiguredNameCharacteristic(iid)
        self.characteristics.append(self._configuredNameCharacteristic)

    def set_on_set_callback(self, callback):
        self._configuredNameCharacteristic.set_set_value_callback(callback)

    def set_on_get_callback(self, callback):
        self._configuredNameCharacteristic.set_get_value_callback(callback)
