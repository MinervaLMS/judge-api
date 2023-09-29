"""This module contains FileCreator class"""
from typing import List
import os
import zipfile
import yaml

from app.utils.constants import PROBLEMS_FOLDER


class FileCreator:
    """
    A class for creating problem folder and files.

    This class provides methods to create input and output files for a problem,
    package them into a zip archive, and generate a YAML metadata file in a
    new problem_id folder.
    """

    def __init__(
        self,
        problem_id: str,
        input_data: List[str],
        output_data: List[str],
        points: List[int],
    ):
        """
        Initialize a FileCreator object to create problem files.

        Args:
            problem_id (str): The unique identifier for the problem.
            input_data (List[str]): List of input data strings.
            output_data (List[str]): List of output data strings.
            points (List[int]): List of points corresponding to each test case.
        """
        self.problem_id = problem_id
        self.input_data = input_data
        self.output_data = output_data
        self.points = points
        self.folder_path = os.path.join(PROBLEMS_FOLDER, problem_id)
        os.makedirs(self.folder_path, exist_ok=True)

    def save(self):
        """create remove and save de files"""
        self.create_input_output_files()
        self.create_zip_file()
        self.create_yaml_file()
        self.remove_input_output_files()

    def create_input_output_files(self):
        """
        Create input and output files for the problem.
        """
        for i, (input_text, output_text) in enumerate(
            zip(self.input_data, self.output_data), start=0
        ):
            with open(
                os.path.join(self.folder_path, f"{self.problem_id}.{i}.in"),
                "w",
                encoding="utf-8",
            ) as f_in:
                f_in.write(input_text)
            with open(
                os.path.join(self.folder_path, f"{self.problem_id}.{i}.out"),
                "w",
                encoding="utf-8",
            ) as f_out:
                f_out.write(output_text)

    def remove_input_output_files(self) -> None:
        """remove files from the problem_id folder that are not present in a ZIP file"""

        for i in range(0, len(self.input_data)):
            in_file = os.path.join(self.folder_path, f"{self.problem_id}.{i}.in")
            out_file = os.path.join(self.folder_path, f"{self.problem_id}.{i}.out")
            os.remove(in_file)
            os.remove(out_file)

    def create_zip_file(self) -> None:
        """
        Create a zip file containing input and output files.
        """
        zip_filename = f"{self.problem_id}.zip"
        with zipfile.ZipFile(
            os.path.join(self.folder_path, zip_filename), "w", zipfile.ZIP_DEFLATED
        ) as zipf:
            for i in range(0, len(self.input_data)):
                zipf.write(
                    os.path.join(self.folder_path, f"{self.problem_id}.{i}.in"),
                    f"{self.problem_id}.{i}.in",
                )
                zipf.write(
                    os.path.join(self.folder_path, f"{self.problem_id}.{i}.out"),
                    f"{self.problem_id}.{i}.out",
                )

    def create_yaml_file(self):
        """
        Create a YAML file with problem metadata.
        """
        yml_data = {
            "archive": f"{self.problem_id}.zip",
            "test_cases": [
                {
                    "in": f"{self.problem_id}.{i}.in",
                    "out": f"{self.problem_id}.{i}.out",
                    "points": p,
                }
                for i, p in enumerate(self.points)
            ],
        }
        with open(os.path.join(self.folder_path, "init.yml"), "w") as yml_file:
            yaml.dump(yml_data, yml_file, default_flow_style=None)