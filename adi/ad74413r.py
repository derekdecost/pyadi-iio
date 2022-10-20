# Copyright (C) 2021 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from decimal import Decimal
import numpy as np
from adi.attribute import attribute
from adi.context_manager import context_manager
from adi.rx_tx import rx

class ad74413r(rx, context_manager):
    _device_name = "ad74413r"

    def __init__(self, uri=""):
        context_manager.__init__(self, uri, self._device_name)
        self.voltage_channels = []
        self.current_channels = []
        self._ctrl = self._ctx.find_device("ad74413r")
        self.voltage_channel_names = ["voltage1", "voltage2"]
        self.current_channel_names = ["current0", "current3"]

        for channel in self.voltage_channel_names:
            self.voltage_channels.append(self._voltage_channel(self._ctrl, channel))

        for channel in self.current_channel_names:
            self.current_channels.append(self._current_channel(self._ctrl, channel))

    class _voltage_channel(attribute):
        def __init__(self, ctrl, channel_name):
            self.name = channel_name
            self._ctrl = ctrl
        
        @property
        def offset(self):
            return self._get_iio_attr(self.name, "offset", False)

        @property
        def raw(self):
            return self._get_iio_attr(self.name, "raw", False)

        @property
        def sampling_frequency(self):
            return self._get_iio_attr(self.name, "sampling_frequency", False)

        @sampling_frequency.setter
        def sampling_frequency(self, sf):
            if not isinstance(sf, np.int16):
                return
            
            if str(sf) in self.sampling_frequency_available.split():
                self._set_iio_attr(self.name, "sampling_frequency", False, sf)

        @property
        def sampling_frequency_available(self):
            return self._get_iio_attr_str(self.name, "sampling_frequency_available", False)

        @property
        def scale(self):
            return float(self._get_iio_attr_str(self.name, "scale", False))

        @scale.setter
        def scale(self, value):
            self._set_iio_attr(self.name, "scale", False, str(Decimal(value).real))

    class _current_channel(attribute):
        def __init__(self, ctrl, channel_name):
            self.name = channel_name
            self._ctrl = ctrl
        
        @property
        def offset(self):
            return self._get_iio_attr(self.name, "offset", False)

        @property
        def raw(self):
            return self._get_iio_attr(self.name, "raw", False)

        @property
        def sampling_frequency(self):
            return self._get_iio_attr(self.name, "sampling_frequency", False)

        @sampling_frequency.setter
        def sampling_frequency(self, sf):
            if not isinstance(sf, np.int16):
                return
            
            if str(sf) in self.sampling_frequency_available.split():
                self._set_iio_attr(self.name, "sampling_frequency", False, sf)

        @property
        def sampling_frequency_available(self):
            return self._get_iio_attr_str(self.name, "sampling_frequency_available", False)

        @property
        def scale(self):
            return float(self._get_iio_attr_str(self.name, "scale", False))

        @scale.setter
        def scale(self, value):
            self._set_iio_attr(self.name, "scale", False, str(Decimal(value).real))

    def to_volts(self, index, val):
        _scale = self.channel[index].scale
        ret = None

        if isinstance(val, np.int16):
            ret = val * _scale
        
        if isinstance(val, np.ndarray):
            ret = [raw_val * _scale for raw_val in val]

        return ret

    def to_current(self, index, val):
        _scale = self.channel[index].scale
        ret = None

        if isinstance(val, np.int16):
            ret = val * _scale
        
        if isinstance(val, np.ndarray):
            ret = [raw_val * _scale for raw_val in val]

        return ret





