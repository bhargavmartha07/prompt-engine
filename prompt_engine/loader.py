from pathlib import Path
import yaml
import json

from .models import PromptTemplate


class TemplateLoader:
    """
    Loads and validates prompt templates from a directory.
    """

    def __init__(self, template_dir: str):
        self.template_dir = Path(template_dir)
        self.templates = {}

    def load(self) -> dict:
        if not self.template_dir.exists():
            raise FileNotFoundError(
                f"Template directory not found: {self.template_dir}"
            )

        for file in self.template_dir.iterdir():
            if file.suffix in [".yaml", ".yml"]:
                data = yaml.safe_load(file.read_text())
            elif file.suffix == ".json":
                data = json.loads(file.read_text())
            else:
                continue

            template = PromptTemplate(**data)

            if template.name in self.templates:
                raise ValueError(
                    f"Duplicate template name found: {template.name}"
                )

            self.templates[template.name] = template

        return self.templates
