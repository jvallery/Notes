#!/usr/bin/env python3
"""
Bootstrap script for Notes Vault automation environment.
Run this once on each Mac to set up the Python environment.

Usage:
    cd ~/Documents/Notes/Workflow
    python3 bootstrap.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    workflow_dir = Path(__file__).parent
    venv_dir = workflow_dir / ".venv"
    requirements_file = workflow_dir / "requirements.txt"
    env_example = workflow_dir / ".env.example"
    env_file = workflow_dir / ".env"

    print("🚀 Notes Vault Automation Bootstrap")
    print("=" * 50)

    # Step 1: Create virtual environment
    if not venv_dir.exists():
        print("\n📦 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
        print(f"   ✓ Created {venv_dir}")
    else:
        print(f"\n📦 Virtual environment already exists: {venv_dir}")

    # Step 2: Determine pip path
    if sys.platform == "win32":
        pip_path = venv_dir / "Scripts" / "pip"
        python_path = venv_dir / "Scripts" / "python"
    else:
        pip_path = venv_dir / "bin" / "pip"
        python_path = venv_dir / "bin" / "python"

    # Step 3: Upgrade pip
    print("\n⬆️  Upgrading pip...")
    subprocess.run([str(pip_path), "install", "--upgrade", "pip"], check=True)

    # Step 4: Install requirements
    if requirements_file.exists():
        print("\n📥 Installing dependencies...")
        subprocess.run([str(pip_path), "install", "-r", str(requirements_file)], check=True)
        print("   ✓ Dependencies installed")
    else:
        print(f"\n⚠️  No requirements.txt found at {requirements_file}")

    # Step 5: Create .env from example if needed
    if not env_file.exists() and env_example.exists():
        print("\n🔐 Creating .env from template...")
        env_file.write_text(env_example.read_text())
        print(f"   ✓ Created {env_file}")
        print("   ⚠️  IMPORTANT: Edit .env and add your OPENAI_API_KEY")
    elif env_file.exists():
        print(f"\n🔐 .env already exists: {env_file}")
    else:
        print("\n⚠️  No .env.example found")

    # Step 6: Create logs directory
    logs_dir = workflow_dir / "logs"
    logs_dir.mkdir(exist_ok=True)
    (logs_dir / ".gitkeep").touch()

    # Step 7: Verify installation
    print("\n✅ Verifying installation...")
    result = subprocess.run(
        [str(python_path), "-c", "import openai; import yaml; import frontmatter; print('All imports OK')"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"   ✓ {result.stdout.strip()}")
    else:
        print(f"   ❌ Import check failed: {result.stderr}")

    print("\n" + "=" * 50)
    print("🎉 Bootstrap complete!")
    print("\nNext steps:")
    print(f"  1. Edit {env_file} and add your OPENAI_API_KEY")
    print(f"  2. Open VS Code: code ~/Documents/Notes/Notes.code-workspace")
    print("  3. The Python interpreter should auto-select the venv")
    print("\nTo activate manually:")
    print(f"  source {venv_dir}/bin/activate")


if __name__ == "__main__":
    main()
