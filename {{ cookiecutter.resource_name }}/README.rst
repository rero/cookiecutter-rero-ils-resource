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

# Cookiecutter Rero Ils Resource
Copy this directory to your modules directory and addapt the following files.


## Please add following to the *setup.py* file section:
### entry_points

```
    'invenio_base.blueprints': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.views:blueprint',
        ...
    ],
    'invenio_db.models': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.models',
        ...
    ],
        'invenio_pidstore.minters': [
        '{{ cookiecutter.name }}_id = rero_ils.modules.{{ cookiecutter.resource_name }}.api:{{ cookiecutter.name }}_id_minter',
        ...
    ],
    'invenio_pidstore.fetchers': [
        '{{ cookiecutter.name }}_id = rero_ils.modules.{{ cookiecutter.resource_name }}.api:{{ cookiecutter.name }}_id_fetcher',
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
    'invenio_celery.tasks': [
        'rero_ils_{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.tasks',
        ...
    ]
    'invenio_records.jsonresolver': [
        '{{ cookiecutter.resource_name }} = rero_ils.modules.{{ cookiecutter.resource_name }}.jsonresolver',
        ...
    ]
```

## Please add following to the *config.py* file section:
### Import:
```
from .modules.{{ cookiecutter.resource_name }}.api import {{ cookiecutter.class_name }}
```

### RECORDS\_REST\_ENDPOINTS
```
	{{ cookiecutter.pid_type }}=dict(
        pid_type='{{ cookiecutter.pid_type }}',
        pid_minter='{{ cookiecutter.name }}_id',
        pid_fetcher='{{ cookiecutter.name }}_id',
        search_class=RecordsSearch,
        search_index='{{ cookiecutter.resource_name }}',
        search_type=None,
        indexer_class=IlsRecordIndexer,
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
        record_loaders={   
            'application/json': lambda: {{ cookiecutter.class_name }}(request.get_json()),
        },
        record_class='rero_ils.modules.{{ cookiecutter.resource_name }}.api:{{ cookiecutter.class_name }}',
        list_route='/{{ cookiecutter.resource_name }}/',
        item_route='/{{ cookiecutter.resource_name }}/<pid({{ cookiecutter.pid_type }}, record_class="rero_ils.modules.{{ cookiecutter.resource_name }}.api:{{ cookiecutter.class_name }}")):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        search_factory_imp='rero_ils.query:search_factory',
        read_permission_factory_imp=allow_all,
        list_permission_factory_imp=allow_all,
        create_permission_factory_imp=deny_all,
        update_permission_factory_imp=deny_all,
        delete_permission_factory_imp=deny_all,
    ),
```

### RECORDS\_UI\_ENDPOINTS
```
	'{{ cookiecutter.pid_type }}': dict(
        pid_type= '{{ cookiecutter.pid_type }}',
        route= '/{{ cookiecutter.resource_name }}/<pid_value>',
        template= 'rero_ils/detailed_view_{{ cookiecutter.resource_name }}.html',
        record_class= 'rero_ils.modules.{{ cookiecutter.resource_name }}.api:{{ cookiecutter.class_name }}',
        permission_factory_imp='rero_ils.permissions.'
                               'librarian_permission_factory',
    ),
```

### RECORDS\_JSON\_SCHEMA
```
    '{{ cookiecutter.pid_type }}': '/{{ cookiecutter.resource_name }}/{{ cookiecutter.name }}-v0.0.1.json',
```


## Note for *api.py* file :

If create and update functions are similar to rero_ils.modules.api then, these two functions can be safely removed.