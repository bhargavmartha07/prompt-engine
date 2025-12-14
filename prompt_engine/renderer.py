from jinja2 import Template
from typing import Dict

from .models import PromptTemplate
from .exceptions import MissingInputVariableError


class PromptRenderer:
    """
    Renders prompt templates using Jinja2 with input validation.
    """

    def render(self, template: PromptTemplate, variables: Dict[str, str]) -> str:
        missing_vars = set(template.input_variables) - variables.keys()

        if missing_vars:
            raise MissingInputVariableError(
                f"Missing input variables: {', '.join(sorted(missing_vars))}"
            )

        jinja_template = Template(template.template)
        return jinja_template.render(**variables)
