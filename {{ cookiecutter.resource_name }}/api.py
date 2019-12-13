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

from functools import partial

from .models import {{ cookiecutter.class_name }}Identifier
from ..fetchers import id_fetcher
from ..minters import id_minter
from ..providers import Provider
from ..api import IlsRecord, IlsRecordsSearch

# provider
{{ cookiecutter.class_name }}Provider = type(
    '{{ cookiecutter.class_name }}Provider',
    (Provider,),
    dict(identifier={{ cookiecutter.class_name }}Identifier, pid_type='{{ cookiecutter.pid_type }}')
)
# minter
{{ cookiecutter.name }}_id_minter = partial(id_minter, provider={{ cookiecutter.class_name }}Provider)
# fetcher
{{ cookiecutter.name }}_id_fetcher = partial(id_fetcher, provider={{ cookiecutter.class_name }}Provider)


class {{ cookiecutter.class_name }}sSearch(IlsRecordsSearch):
    """{{ cookiecutter.class_name }}sSearch."""

    class Meta:
        """Search only on {{ cookiecutter.name }} index."""

        index = '{{ cookiecutter.resource_name }}'


class {{ cookiecutter.class_name }}(IlsRecord):
    """{{ cookiecutter.class_name }} class."""

    minter = {{ cookiecutter.name }}_id_minter
    fetcher = {{ cookiecutter.name }}_id_fetcher
    provider = {{ cookiecutter.class_name }}Provider

    @classmethod
    def create(cls, data, id_=None, delete_pid=False,
               dbcommit=False, reindex=False, **kwargs):
        """Create {{ cookiecutter.name }} record."""
        record = super({{ cookiecutter.class_name }}, cls).create(
            data, id_, delete_pid, dbcommit, reindex, **kwargs)
        return record

    def update(self, data, dbcommit=False, reindex=False):
        """Update {{ cookiecutter.name }} record."""
        super({{ cookiecutter.class_name }}, self).update(data, dbcommit, reindex)
        
        return self

