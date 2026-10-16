from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.calculator import CalculationError, calculate
from app.database import get_db
from app.models import Calculation
from app.schemas import CalculationInput, CalculationOutput, LabelUpdate

router = APIRouter(prefix="/api")
DB = Annotated[Session, Depends(get_db)]


def evaluate(data: CalculationInput) -> float:
    try:
        return calculate(data.expression, data.angle_mode)
    except CalculationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/evaluate")
def preview(data: CalculationInput):
    return {"result": evaluate(data), "angle_mode": data.angle_mode}


@router.post("/calculations", response_model=CalculationOutput, status_code=201)
def create_calculation(data: CalculationInput, db: DB):
    row = Calculation(**data.model_dump(), result=evaluate(data))
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/calculations", response_model=list[CalculationOutput])
def list_calculations(db: DB, limit: int = Query(50, ge=1, le=100),
                      offset: int = Query(0, ge=0)):
    return db.scalars(select(Calculation).order_by(Calculation.id.desc()).offset(offset).limit(limit)).all()


def find_calculation(calculation_id: int, db: Session) -> Calculation:
    row = db.get(Calculation, calculation_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Calculation not found.")
    return row


@router.get("/calculations/{calculation_id}", response_model=CalculationOutput)
def get_calculation(calculation_id: int, db: DB):
    return find_calculation(calculation_id, db)


@router.put("/calculations/{calculation_id}", response_model=CalculationOutput)
def label_calculation(calculation_id: int, data: LabelUpdate, db: DB):
    row = find_calculation(calculation_id, db)
    row.label = data.label.strip()
    db.commit()
    db.refresh(row)
    return row


@router.delete("/calculations/{calculation_id}", status_code=204)
def delete_calculation(calculation_id: int, db: DB):
    db.delete(find_calculation(calculation_id, db))
    db.commit()
    return Response(status_code=204)
