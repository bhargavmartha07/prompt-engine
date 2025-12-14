from typing import Dict

from .loader import TemplateLoader
from .renderer import PromptRenderer
from .models import PromptTemplate


class PromptEngine:
    """
    Central engine that manages loading, rendering, and chaining prompt templates.
    """

    def __init__(self, template_dir: str):
        self.loader = TemplateLoader(template_dir)
        self.renderer = PromptRenderer()
        self.templates: Dict[str, PromptTemplate] = self.loader.load()

    def list_templates(self) -> Dict[str, PromptTemplate]:
        """
        Returns all loaded templates.
        """
        return self.templates

    def render(self, template_name: str, variables: Dict[str, str]) -> str:
        """
        Renders a prompt by template name with provided variables.
        """
        if template_name not in self.templates:
            raise KeyError(f"Template not found: {template_name}")

        template = self.templates[template_name]
        return self.renderer.render(template, variables)

    def chain(self, steps: list) -> str:
        """
        Executes a sequence of prompts where the output of one step
        can be used as input for the next.

        Each step must be a dict with:
        - template: template name
        - inputs: dict of input variables (can reference previous outputs)
        - output_key: key under which output is stored
        """
        context = {}
        last_output = ""

        for step in steps:
            template_name = step["template"]
            inputs = step.get("inputs", {})
            output_key = step["output_key"]

            # Resolve inputs: allow referencing previous outputs
            resolved_inputs = {}
            for key, value in inputs.items():
                if isinstance(value, str) and value in context:
                    resolved_inputs[key] = context[value]
                else:
                    resolved_inputs[key] = value

            # Merge previous outputs with current inputs
            merged_inputs = {**context, **resolved_inputs}

            output = self.render(template_name, merged_inputs)

            context[output_key] = output
            last_output = output

        return last_output
