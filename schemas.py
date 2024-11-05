from pydantic import BaseModel


class FixedInvestmentWithoutReinvestment(BaseModel):
    amount: float
    interest_rate: float
    months_duration: int  # Cambiado a meses


class FixedInvestmentWithoutReinvestmentResponse(BaseModel):
    amount: float
    month: int


class FixedInvestmentWithReinvestment(BaseModel):
    amount: float
    interest_rate: float
    months_duration: int


class FixedInvestmentWithReinvestmentResponse(BaseModel):
    amount: float
    month: int


class MoneyMarketInvestment(BaseModel):
    amount: float
    interest_rate: float  # Tasa de interés anual
    months_duration: int  # Duración en meses


class MoneyMarketInvestmentResponse(BaseModel):
    amount: float
    month: int
