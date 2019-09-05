# -*- coding: utf-8 -*-
#
# RERO ILS
# Copyright (C) 2019 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""API for manipulating {{ cookiecutter.resource_name }}."""

from __future__ import absolute_import, print_function

from .fetchers import {{ cookiecutter.name }}_id_fetcher
from .minters import {{ cookiecutter.name }}_id_minter
from .providers import {{ cookiecutter.class_name }}Provider
from ..api import IlsRecord


class {{ cookiecutter.class_name }}(IlsRecord):
    """{{ cookiecutter.class_name }} class."""

    minter = {{ cookiecutter.name }}_id_minter
    fetcher = {{ cookiecutter.name }}_id_fetcher
    provider = {{ cookiecutter.class_name }}Provider
