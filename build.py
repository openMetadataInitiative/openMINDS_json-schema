import os.path
import shutil

from pipeline.utils import clone_sources, SchemaLoader, copy_static_structures, GitPusher

print("***************************************")
print(f"Triggering the generation of JSON-Schemas for openMINDS")
print("***************************************")

# Step 1 - clone central repository in main branch to get the latest sources
clone_sources()
schema_loader = SchemaLoader()
if os.path.exists("target"):
    shutil.rmtree("target")
