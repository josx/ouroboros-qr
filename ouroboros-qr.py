#!/usr/bin/env python3

# This script comes with ABSOLUTELY NO WARRANTY, use at own risk
# Copyright (C) 2025 José Luis Di Biase <josx@interorganic.com.ar>
# Copyright (C) 2025 José Luis Di Biase <josx@camba.coop>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import inspect
import sys
import segno

source_code = inspect.getsource(sys.modules[__name__])
qrcode = segno.make(source_code)
qrcode.terminal(compact=True)
