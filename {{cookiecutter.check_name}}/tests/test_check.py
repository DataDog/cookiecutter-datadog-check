# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.{{cookiecutter.check_name}} import {{cookiecutter.class_name}}


def test_check(aggregator):
    c = {{cookiecutter.class_name}}('{{cookiecutter.check_name}}', {}, {}, None)
    c.check({})
    aggregator.assert_all_metrics_covered()
