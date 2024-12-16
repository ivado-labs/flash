from pathlib import Path
from unittest import TestCase

import papermill as pm


class NotebooksTestCase(TestCase):
    def setUp(self):
        self.notebooks_dir = Path(__file__).parent.parent / "notebooks"

    def __run_notebook(self, notebook_file_path: str, notebook_file_name: str) -> None:
        pm.execute_notebook(
            self.notebooks_dir / notebook_file_path / notebook_file_name,
            None,
            cwd=self.notebooks_dir / notebook_file_path,
        )

    def test_intro_to_ydata_profiling(self):
        self.__run_notebook("EDA/ydata-profiling", "intro_tutorial.ipynb")

    def test_timeseries_example_with_ydata_profiling(self):
        self.__run_notebook("EDA/ydata-profiling", "time_series_tutorial.ipynb")

    def test_intro_to_nixtla(self):
        self.__run_notebook("ML/Time series forecasting/Nixtla", "intro_tutorial.ipynb")

    def test_hierarchical_timeseries_example_with_nixtla(self):
        self.__run_notebook("ML/Time series forecasting/Nixtla", "hierarchical_data_tutorial.ipynb")
