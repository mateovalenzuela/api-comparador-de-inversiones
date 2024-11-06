from pydantic import BaseModel


class FixedInvestmentWithoutReinvestment(BaseModel):
    amount: float
    interest_rate: float
    months_duration: int  # Cambiado a meses


class FixedInvestmentWithReinvestment(BaseModel):
    amount: float
    interest_rate: float
    months_duration: int


class MoneyMarketInvestment(BaseModel):
    amount: float
    interest_rate: float  # Tasa de interés anual
    months_duration: int  # Duración en meses


class InvestmentResponse(BaseModel):
    amount: float
    month: int
