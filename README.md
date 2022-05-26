# Custom filters for Jinja (Home Assistant)

## Installation
*__Manual mode__*

Place the `custom_filters` folder into your `custom_components` folder.

*__Adding custom repository to [HACS](https://hacs.xyz/)__*

Go to the Integrations page in HACS and select the three dots in the top right corner. Select Custom repositories.
Add repository url. Category - Integration. Read more on https://hacs.xyz/docs/faq/custom_repositories.


## Setup
Add `custom_filters:` to your configuration.yaml or add integration `Custom filters` on the Integrations page.


## Filters
```
to_ascii_json               - encode to JSON with ensure_ascii option enabled
```

## Credits
Based on https://github.com/zvldz/ha_custom_filters
