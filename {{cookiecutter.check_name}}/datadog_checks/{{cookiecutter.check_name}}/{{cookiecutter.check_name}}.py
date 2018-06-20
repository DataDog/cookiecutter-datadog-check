# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.checks import AgentCheck


class {{cookiecutter.class_name}}(AgentCheck):

    def check(self, instance):
        # collect metrics here
        pass
