import os
import subprocess
from pathlib import Path

start_dir = Path.cwd()

bin_folder = start_dir / "bin"

output_jar = start_dir / "lib" / "UI_AGENT_MANIFEST_ONLY.jar"
manifest_file = Path("imgui_2026") / "UI_Widget_Agent_MANIFEST.MF"

os.chdir(bin_folder)

subprocess.run(
    [
        "jar",
        "cfm",
        str(output_jar),
        str(manifest_file),
    ],
    check=True
)
