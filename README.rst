..
    RERO ILS
    Copyright (C) 2019 RERO

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

================================
 Cookiecutter-Rero-Ils-Resource
================================

.. image:: https://img.shields.io/github/tag/rero/cookicutter-resource.svg
        :alt: Release Number
        :target: https://github.com/rero/cookiecutter-rero-ils-resource/releases/latest

.. image:: https://img.shields.io/github/license/rero/cookicutter-resource.svg
        :alt: License
        :target: https://github.com/rero/cookiecutter-rero-ils-resource/blob/master/LICENSE

This `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template is
designed to help you to bootstrap an `RERO ILS
<https://github.com/rero/rero-ils>`_ resource.

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet::

    pip install -U cookiecutter
    pip install -U jinja2_stringcase

Generate your rero-ils resource::

    cookiecutter https://github.com/rero/cookiecutter-rero-ils-resource.git

Configuration
-------------
To generate correct files, please provide the following input to Cookiecutter:

==================== =============================================
`name`               Name.
`resource_name`      Resource name (plurial of name).
`class_name`         Class name (name with capital first letter).
`app_name`           Application name.
`pid_type`           Pid_type
==================== =============================================
