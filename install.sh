#!/bin/bash
# CodeStacker Install Script
# Usage: curl -sSL https://raw.githubusercontent.com/CoSama-Ai/CodeStacker/main/install.sh | bash

set -e

REPO="https://github.com/CoSama-Ai/CodeStacker.git"
TMP_DIR=$(mktemp -d)

echo ""
echo "📦 Installing CodeStacker..."
echo ""

# Clone repo to temp
git clone --depth 1 "$REPO" "$TMP_DIR" --quiet

# Copy entry point and system folder to current directory
cp "$TMP_DIR/stack.md" .
cp -r "$TMP_DIR/.codestacker" .

# Cleanup
rm -rf "$TMP_DIR"

echo "✅ CodeStacker installed successfully."
echo ""
echo "Your project now has:"
echo "  stack.md         ← AI entry point (single file in your project root)"
echo "  .codestacker/    ← system files (rules, skills, project tracking)"
echo ""
echo "Next steps:"
echo "  1. Open a chat with your AI assistant"
echo "  2. Say: \"Read stack.md and follow it\""
echo "  3. Run: Mode New Project"
echo ""
echo "  → codestacker.co for skills, props & workflows"
echo ""
