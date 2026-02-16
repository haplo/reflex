from pathlib import Path


def pdm_build_update_files(context, files):
    if context.target != "wheel":
        return

    for dirname in ["static", "templates", "translations"]:
        to_rename = [
            (relpath, local_path)
            for relpath, local_path in list(files.items())
            if relpath.startswith(f"{dirname}/")
        ]
        for relpath, local_path in to_rename:
            del files[relpath]
            new_relpath = f"pelican/themes/reflex/{relpath}"
            files[new_relpath] = local_path
