from enum import Enum
from pydantic import BaseModel, Field


class SQLMatchStatus(str, Enum):
    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NOT_MATCH = "not_match"
    UNCLEAR = "unclear"


class SQLComparisonEvaluation(BaseModel):
    model_config = {"extra": "forbid"}

    sql_match: SQLMatchStatus = Field(
        ...,
        description="Required. Semantic comparison result between silver SQL and actual SQL. Must be one of: match, partial_match, not_match, unclear."
    )
    sql_reason: str = Field(
        ...,
        min_length=1,
        description="Required. Reason for why the actual SQL is match, partial_match, not_match, or unclear against the silver SQL."
    )
