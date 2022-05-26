import json
from typing import Any, cast

from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.template import TemplateEnvironment
from homeassistant.helpers.typing import ConfigType

DOMAIN = 'custom_filters'


def to_ascii_json(string):
    return json.dumps(string, ensure_ascii=False)


async def async_setup(hass: HomeAssistant, yaml_config: ConfigType):
    if DOMAIN in yaml_config and not hass.config_entries.async_entries(DOMAIN):
        hass.async_create_task(hass.config_entries.flow.async_init(
            DOMAIN, context={'source': SOURCE_IMPORT}
        ))

    return True


async def async_setup_entry(hass: HomeAssistant, _: ConfigEntry):
    for env in hass.data.values():
        if isinstance(env, TemplateEnvironment):
            env.filters['to_ascii_json'] = to_ascii_json

    CustomTemplateEnvironment.base_init = cast(Any, TemplateEnvironment.__init__)
    TemplateEnvironment.__init__ = CustomTemplateEnvironment.init

    return True


async def async_unload_entry(*_):
    TemplateEnvironment.__init__ = CustomTemplateEnvironment.base_init
    return True


class CustomTemplateEnvironment:
    base_init = None

    @staticmethod
    def init(*args, **kwargs):
        CustomTemplateEnvironment.base_init(*args, **kwargs)
        env = args[0]
        env.filters['to_ascii_json'] = to_ascii_json
