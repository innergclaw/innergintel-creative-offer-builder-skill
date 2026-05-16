#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$TARGET_DIR"
rm -rf "$TARGET_DIR/creative-offer-builder"
cp -R "$ROOT_DIR/skill/creative-offer-builder" "$TARGET_DIR/creative-offer-builder"

echo "Installed creative-offer-builder to $TARGET_DIR/creative-offer-builder"
