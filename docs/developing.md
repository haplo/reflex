# Development

Reflex uses gulp to compile LESS files into CSS and optimize the final build.

## Setup

`npm install`

## Compilation

`npm run watch`

## Example site

Create a virtualenv and install dependencies:

```shell
cd example
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run pelican:

```shell
make devserver
```

To deploy to Github Pages:

```shell
make github
```
