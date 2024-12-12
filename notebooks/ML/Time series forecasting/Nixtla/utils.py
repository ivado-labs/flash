import pandas as pd
from utilsforecast.evaluation import evaluate
from utilsforecast.losses import coverage, mape, mse


def evaluate_cross_validation(df: pd.DataFrame, level: list[int]) -> pd.DataFrame:
    models = df.loc[:, ~df.columns.str.contains("unique_id|y|ds|cutoff|lo|hi")].columns
    evals = evaluate(df=df, metrics=[mape, mse, coverage], models=models, level=level)
    evals["best_model"] = evals.apply(
        lambda row: row[models].idxmax() if (row["metric"] == "coverage") else row[models].idxmin(), axis=1
    )
    return evals


def hour_index(times: int) -> int:
    return times % 24
