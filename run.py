from pathlib import Path
import runpy
import traceback


def iter_python_files(root: Path) -> list[Path]:
    return sorted(
        p
        for p in root.rglob("*.py")
        if p.is_file() and p.name != "__init__.py"
    )


def run_all(root: Path) -> None:
    files = iter_python_files(root)
    if not files:
        print(f"No Python files found in {root}")
        return

    total = len(files)
    passed = 0
    failed = 0

    for idx, file_path in enumerate(files, start=1):
        rel_path = file_path.relative_to(Path.cwd())
        print(f"\n[{idx}/{total}] Running {rel_path}")
        try:
            runpy.run_path(str(file_path), run_name="__main__")
            passed += 1
        except Exception:
            failed += 1
            print(f"FAILED: {rel_path}")
            traceback.print_exc()

    print(
        f"\nFinished. Total: {total}, Passed: {passed}, Failed: {failed}"
    )


if __name__ == "__main__":
    run_all(Path("blind_75").resolve())
