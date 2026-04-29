#!/usr/bin/env bash
set -euo pipefail

SSH_KEY="${SSH_KEY:-$HOME/.ssh/portfolio_deploy}"
SSH_TARGET="${SSH_TARGET:-martin@192.168.50.237}"
REMOTE_DIR="/opt/projects/portfolio"

echo ">>> Deploying to $SSH_TARGET:$REMOTE_DIR"

ssh -i "$SSH_KEY" "$SSH_TARGET" "
  set -e
  cd '$REMOTE_DIR'
  git pull --ff-only
  docker compose up -d --build
  docker image prune -f
"

echo ">>> Done. Site: http://portfolio.lan"
