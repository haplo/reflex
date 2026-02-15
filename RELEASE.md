# Release Process

This document describes how to release a new version of Reflex.

## First-time setup

1. Go to https://pypi.org/manage/projects/ and create a new project named `pelican-reflex`.
2. **Configure trusted publishing** (one-time only):
  1. In PyPI project settings, add a trusted publisher:
    1. PyPI project → Publishing → Add a new pending publisher
    2. PyPI project name: `pelican-reflex`
    3. Owner: `haplo`
    4. Repository name: `reflex`
    5. Workflow name: `pypi-publish.yml`
    6. Environment name: `pypi`
  2. In Github repository settings, set up the *pypi* environment:
    1. Go to repo Settings → Environments → New environment
    2. Name it `pypi`
    3. Enable *Required reviewers* and add at least one.
    4. In *Deployment branches and tags* select *Selected branches and tags*
    5. In *Deployment branches and tags* add a new rule with *Ref type: tag*, and use the pattern `v*`.

## Release Steps

### 1. Update version and changelog

Update the version number in these files:
- `pyproject.toml` - `version` field
- `package.json` - `version` field

Update `CHANGELOG.md` with the changes for this release.

### 2. Build assets

```bash
npm run build
```

This compiles LESS to CSS, minifies JavaScript, and copies font assets.

### 3. Commit changes

```bash
git add .
git commit -m "Prepare release vX.Y.Z"
```

### 4. Create and push tag

```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z" --sign
git push origin main
git push origin vX.Y.Z
```

Pushing the tag triggers the [`pypi-publish.yml`](.github/workflows/pypi-publish.yml) workflow which publishes to PyPI.

### 5. Create GitHub release

```bash
gh release create vX.Y.Z --generate-notes
```

Or create manually at https://github.com/haplo/reflex/releases/new

### 6. Approve PyPI publish workflow

The workflow that publishes to PyPI requires manual approval in case an attacker gains git push access.
Go to [GitHub Actions](https://github.com/haplo/reflex/actions/workflows/pypi-publish.yml), review and approve.

### 7. Verify

- Check PyPI: https://pypi.org/project/pelican-reflex/
- Test installation: `pip install pelican-reflex`

## Versioning

Use semantic versioning (*MAJOR.MINOR.PATCH*):

- **MAJOR**: Breaking changes.
- **MINOR**: New features, backwards compatible.
- **PATCH**: Bug fixes, backwards compatible.

## Troubleshooting

### PyPI publish failed

1. Check the [workflow run in GitHub Actions](https://github.com/haplo/reflex/actions/workflows/pypi-publish.yml).
2. Verify the trusted publisher is configured correctly on both Github and PyPI.
3. Ensure the `pypi` environment exists in Github repository settings and has the right settings.

### Package already exists

If you try to publish a version that already exists on PyPI, the publish will fail. You must increment the version number.

### Assets not updated

Always run `npm run build` before releasing. The CI will fail if built assets are not up to date.
