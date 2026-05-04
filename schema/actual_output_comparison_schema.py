from enum import Enum
from pydantic import BaseModel, Field


class ActualOutputMatchStatus(str, Enum):
    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NOT_MATCH = "not_match"
    UNCLEAR = "unclear"


class OutputComparisonEvaluation(BaseModel):
    model_config = {"extra": "forbid"}

    actual_output_match: ActualOutputMatchStatus = Field(
        ...,
        description="Required. Semantic comparison result between silver output and actual output. Must be one of: match, partial_match, not_match, unclear."
    )
    actual_output_reason: str = Field(
        ...,
        min_length=1,
        description="Required. Reason for why the actual output is match, partial_match, not_match, or unclear against the silver output."
    )
