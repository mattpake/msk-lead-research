"""Run backend (uvicorn) and frontend (next dev) dev servers concurrently.

Usage:
    python start_dev_server.py

Prerequisites:
    - Backend deps installed: cd server && uv sync
    - Frontend deps installed: cd client && npm install

Stop with Ctrl+C — both processes are terminated together. If either server
exits on its own, the other is shut down and its exit code is propagated.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SERVER_DIR = PROJECT_ROOT / "server"
CLIENT_DIR = PROJECT_ROOT / "client"

BACKEND_PORT = 8000
FRONTEND_PORT = 3000
SHUTDOWN_TIMEOUT_SECONDS = 10

NPM_EXECUTABLE = "npm.cmd" if sys.platform == "win32" else "npm"

# uv run resolves server/pyproject.toml from cwd and guarantees the locked env.
BACKEND_COMMAND = [
    "uv",
    "run",
    "uvicorn",
    "src.main:app",
    "--reload",
    "--port",
    str(BACKEND_PORT),
]
FRONTEND_COMMAND = [NPM_EXECUTABLE, "run", "dev", "--", "--port", str(FRONTEND_PORT)]


def spawn_dev_servers() -> list[subprocess.Popen[bytes]]:
    backend_process = subprocess.Popen(BACKEND_COMMAND, cwd=SERVER_DIR)
    frontend_process = subprocess.Popen(FRONTEND_COMMAND, cwd=CLIENT_DIR)
    return [backend_process, frontend_process]


def terminate_dev_servers(processes: list[subprocess.Popen[bytes]]) -> None:
    for process in processes:
        if process.poll() is None:
            process.terminate()
    for process in processes:
        try:
            process.wait(timeout=SHUTDOWN_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            process.kill()


def main() -> int:
    processes = spawn_dev_servers()
    print(f"Backend  -> http://localhost:{BACKEND_PORT} (API docs: /docs)")
    print(f"Frontend -> http://localhost:{FRONTEND_PORT}")
    print("Press Ctrl+C to stop both servers.")
    try:
        while True:
            time.sleep(1)
            for process in processes:
                if process.poll() is not None:
                    print(
                        f"A dev server exited with code {process.returncode}; "
                        "shutting down the other."
                    )
                    return process.returncode or 1
    except KeyboardInterrupt:
        print("\nStopping dev servers...")
        return 0
    finally:
        terminate_dev_servers(processes)


if __name__ == "__main__":
    raise SystemExit(main())
