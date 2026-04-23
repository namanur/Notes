#!/bin/bash
# _SYSTEM/FALLBACK_CHAIN.sh
# Run when Gemini CLI is rate-limited.
# Usage: bash _SYSTEM/FALLBACK_CHAIN.sh "your prompt here"

PROMPT="$1"
KEY="${OPENROUTER_API_KEY}"

GEMINI_OUT=$(gemini "$PROMPT" 2>&1)
if echo "$GEMINI_OUT" | grep -qiE "429|rate.limit|quota|exhausted"; then
  echo "[FALLBACK] Gemini limited → trying DeepSeek R1"
  for MODEL in "deepseek/deepseek-r1" "qwen/qwen3-235b-a22b" "meta-llama/llama-4-scout"; do
    R=$(curl -s https://openrouter.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
      -d "{\"model\":\"$MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"$PROMPT\"}]}")
    if ! echo "$R" | grep -q '"error"'; then
      echo "[FALLBACK] Used: $MODEL"
      echo "$R" | python3 -c \
        "import sys,json; print(json.load(sys.stdin)['choices'][0]['message']['content'])"
      exit 0
    fi
    echo "[FALLBACK] $MODEL failed, trying next"
  done
  echo "[FALLBACK] All models failed. Log this and retry manually."
else
  echo "$GEMINI_OUT"
fi
