import subprocess
import sys

# Which tests to run when a file changes
ROUTES = {
    "src/pricing.py": ["tests/test_pricing.py", "tests/test_cart.py"],
    "src/cart.py": ["tests/test_cart.py"],
    "src/inventory.py": ["tests/test_inventory.py"],
}
RUN_ALL = ("requirements.txt", "pytest.ini", ".github/workflows/ci.yml")


def changed_files(base, head="HEAD"):
    out = subprocess.run(
        ["git", "diff", "--name-only", base, head],
        capture_output=True, text=True, check=True,
    ).stdout
    return [line.strip() for line in out.splitlines() if line.strip()]


def select_tests(files):
    if any(f in RUN_ALL for f in files):
        return ["tests"]
    chosen = []
    for f in files:
        for t in ROUTES.get(f, []):
            if t not in chosen:
                chosen.append(t)
    if not chosen and any(f.startswith(("src/", "tests/")) for f in files):
        return ["tests"]
    return chosen


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD~1"
    files = changed_files(base)
    print(" ".join(select_tests(files)))