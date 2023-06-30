import json
import os.path
from typing import List, Optional, Dict

class JSONSchemaBuilder(object):

    def __init__(self, schema_file_path:str, root_path:str):
        _relative_path_without_extension = schema_file_path[len(root_path)+1:].replace(".schema.omi.json", "").split("/")
        self.version = _relative_path_without_extension[0]
        self.relative_path_without_extension = _relative_path_without_extension[1:]
        with open(schema_file_path, "r") as schema_f:
            self._schema_payload = json.load(schema_f)

    def _target_file_without_extension(self) -> str:
        return os.path.join(self.version, "/".join(self.relative_path_without_extension))

    def build(self):
        target_file = os.path.join("target", "schemas", f"{self._target_file_without_extension()}.schema.json")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as target_file:
            target_file.write(json.dumps(self._schema_payload, indent=2))