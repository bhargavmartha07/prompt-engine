class PromptEngineError(Exception):
    """Base exception for prompt engine errors."""
    pass


class MissingInputVariableError(PromptEngineError):
    """Raised when required input variables are missing."""
    pass
