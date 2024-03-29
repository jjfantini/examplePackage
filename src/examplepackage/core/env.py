import os
from pathlib import Path
from typing import Dict, Optional

import dotenv

from examplepackage.core.models.abstract.singleton import SingletonMeta


class Env(metaclass=SingletonMeta):
    """Environment variables."""

    _environ: Dict[str, str]

    def __init__(self) -> None:
        env_path = dotenv.find_dotenv()
        dotenv.load_dotenv(Path(env_path))

        self._environ = os.environ.copy()

    @property
    def SERVICE_API(self) -> Optional[str]:
        """Example API KEY"""
        return self._environ.get("SERVICE_API", None)

    # Use this when you want a variable to return a bool
    @staticmethod
    def str2bool(value) -> bool:
        """Match a value to its boolean correspondent."""
        if isinstance(value, bool):
            return value
        if value.lower() in {"false", "f", "0", "no", "n"}:
            return False
        if value.lower() in {"true", "t", "1", "yes", "y"}:
            return True
        raise ValueError(f"Failed to cast {value} to bool.")
