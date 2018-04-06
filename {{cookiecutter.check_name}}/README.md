# {{cookiecutter.check_name}} Integration

## Overview

[...]

## Setup

### Installation

[...]

### Configuration

Create a `{{cookiecutter.check_name}}.yaml` in the Datadog Agent's `conf.d` directory.

#### Metric Collection

Add this configuration setup to your `{{cookiecutter.check_name}}.yaml` file to start gathering your [metrics](#metrics):

```
init_config:

instances:
  - []
```

Configuration Options:

[...]

[Restart the Agent](https://docs.datadoghq.com/agent/faq/agent-commands/#start-stop-restart-the-agent) to begin sending Redis metrics to Datadog.

### Validation

[Run the Agent's `status` subcommand](https://docs.datadoghq.com/agent/faq/agent-commands/#agent-status-and-information) and look for `{{cookiecutter.check_name}}` under the Checks section:

```
  Checks
  ======
    [...]

    {{cookiecutter.check_name}}
    -------
      - instance #0 [OK]
      - Collected 26 metrics, 0 events & 1 service check

    [...]
```

## Compatibility

The check is compatible with all major platforms.

## Data Collected

### Metrics

See [metadata.csv](metadata.csv) for a list of metrics provided by this integration.

### Events

The Redis check does not include any event at this time.

### Service Checks

[...]

## Troubleshooting

[...]

## Development

Please refer to the [main documentation](https://docs.datadoghq.com/developers/)
for more details about how to test and develop Agent based integrations.
