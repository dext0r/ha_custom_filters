import json

from homeassistant.helpers import template


_TemplateEnvironment = template.TemplateEnvironment


def to_ascii_json(string):
    return json.dumps(string, ensure_ascii=False)


def init(*args):
    env = _TemplateEnvironment(*args)
    env.filters['to_ascii_json'] = to_ascii_json
    return env


template.TemplateEnvironment = init
template._NO_HASS_ENV.filters['to_ascii_json'] = to_ascii_json


async def async_setup(hass, hass_config):
    return True
