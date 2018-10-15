..
    This file is part of RERO ILS.
    Copyright (C) 2017 RERO.

    RERO ILS is free software; you can redistribute it
    and/or modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation; either version 2 of the
    License, or (at your option) any later version.

    RERO ILS is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with RERO ILS; if not, write to the
    Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
    MA 02111-1307, USA.

    In applying this license, RERO does not
    waive the privileges and immunities granted to it by virtue of its status
    as an Intergovernmental Organization or submit itself to any jurisdiction.

# Cookiecutter Rero Ils Resource
Copy this directory to your modules directory and addapt the following files.


## Please add following to the *setup.py* file section:
### entry_points

```
    'invenio_base.blueprints': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.views:blueprint'
        ...
    ],
    'invenio_db.models': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.models',
        ...
    ],
        'invenio_pidstore.minters': [
        '{{ cookiecutter.name }}_id = rero_ils.modules.{{ cookiecutter.resource_name }}.minters:{{ cookiecutter.name }}_id_minter'
        ...
    ],
    'invenio_pidstore.fetchers': [
        '{{ cookiecutter.name }}_id = rero_ils.modules.{{ cookiecutter.resource_name }}.fetchers:{{ cookiecutter.name }}_id_fetcher'
    ...
    ],
    'invenio_jsonschemas.schemas': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.jsonschemas',
        ...
    ],
    'invenio_search.mappings': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.mappings',
        ...
    ]
```

## Please add following to the *config.py* file section:
### RECORDS\_REST\_ENDPOINTS
```
	{{ cookiecutter.pid_type }}=dict(
        pid_type='{{ cookiecutter.pid_type }}',
        pid_minter='{{ cookiecutter.name }}_id',
        pid_fetcher='{{ cookiecutter.name }}_id',
        search_class=RecordsSearch,
        search_index='{{ cookiecutter.resource_name }}',
        search_type=None,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/rero+json': ('rero_ils.modules.serializers'
                                      ':json_v1_search'),
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/{{ cookiecutter.resource_name }}/',
        item_route='/{{ cookiecutter.resource_name }}/<pid({{ cookiecutter.pid_type }}):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        search_factory_imp='rero_ils.query:and_search_factory'
    ),
```

### RECORDS\_UI\_ENDPOINTS
```
	'{{ cookiecutter.pid_type }}': {
        'pid_type': '{{ cookiecutter.pid_type }}',
        'route': '/{{ cookiecutter.resource_name }}/<pid_value>',
        'template': '{{ cookiecutter.app_name }}/detailed_view_{{ cookiecutter.resource_name }}.html',
        'record_class': '{{ cookiecutter.app_name }}.modules.{{ cookiecutter.resource_name }}.api:{{ cookiecutter.class_name }}',
        'permission_factory_imp':
            'rero_ils.permissions.cataloguer_permission_factory'
    }
```
