import pandas as pd
from utilsforecast.evaluation import evaluate
from utilsforecast.losses import coverage, mse


def evaluate_cross_validation(df: pd.DataFrame, level: list[int]) -> pd.DataFrame:
    models = df.loc[:, ~df.columns.str.contains("unique_id|y|ds|cutoff|lo|hi")].columns

    evals = []
    for cutoff in df["cutoff"].unique():
        cutoff_df = df[df["cutoff"] == cutoff].drop(columns="cutoff")
        eval_ = evaluate(df=cutoff_df, metrics=[mse, coverage], models=models, level=level)
        evals.append(eval_)

    evals = pd.concat(evals)
    evals["best_model"] = evals.apply(
        lambda row: row[models].idxmin() if (row["metric"] == "mse") else row[models].idxmax(), axis=1
    )
    return evals


def hour_index(times: int) -> int:
    return times % 24
