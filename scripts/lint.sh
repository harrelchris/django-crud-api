#!/usr/bin/env bash

source .venv/bin/activate

ruff format
ruff check --fix
