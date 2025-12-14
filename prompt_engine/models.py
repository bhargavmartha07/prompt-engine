from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class PromptTemplate(BaseModel):
    """
    Defines and validates a prompt template schema.
    """

    name: str = Field(..., description="Unique name of the prompt template")
    description: str = Field(..., description="Description of the prompt purpose")
    pattern: str = Field(..., description="Prompt pattern type")
    input_variables: List[str] = Field(
        ..., description="List of required input variables"
    )
    template: str = Field(..., description="Jinja2 template string")

    # Used only for few-shot prompts
    examples: Optional[List[Dict[str, str]]] = Field(
        default=None,
        description="Few-shot examples as input/output pairs"
    )
