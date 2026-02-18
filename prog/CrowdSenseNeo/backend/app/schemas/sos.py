from pydantic import BaseModel

class SosRequest(BaseModel):
    location: str
    source: str
    riskLevel: str