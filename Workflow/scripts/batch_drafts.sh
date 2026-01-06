#!/bin/bash
# Batch process all source emails to generate draft replies
# This script processes emails sequentially with progress tracking

cd "$(dirname "$0")/.."
source .venv/bin/activate

SOURCES_DIR="$HOME/Documents/Notes/Sources/Email/2025"
OUTBOX_DIR="$HOME/Documents/Notes/Outbox"
LOG_FILE="/tmp/batch_drafts_$(date +%Y%m%d_%H%M%S).log"

echo "=== Batch Draft Generation ===" | tee "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "Log file: $LOG_FILE"
echo ""

# Count files
total=$(ls "$SOURCES_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "Total source emails: $total" | tee -a "$LOG_FILE"

processed=0
failed=0

for f in "$SOURCES_DIR"/*.md; do
    ((processed++))
    basename_f=$(basename "$f")
    echo "" | tee -a "$LOG_FILE"
    echo "[$processed/$total] Processing: $basename_f" | tee -a "$LOG_FILE"
    
    # Run ingest and capture output
    output=$(python scripts/ingest.py --source --draft-replies --force --file "$f" 2>&1)
    exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        # Extract draft path from output
        draft=$(echo "$output" | grep "Draft reply:" | head -1)
        if [ -n "$draft" ]; then
            echo "  ✓ $draft" | tee -a "$LOG_FILE"
        else
            echo "  ✓ Completed (no draft in output)" | tee -a "$LOG_FILE"
        fi
    else
        ((failed++))
        echo "  ✗ FAILED (exit code: $exit_code)" | tee -a "$LOG_FILE"
        echo "$output" >> "$LOG_FILE"
    fi
done

echo "" | tee -a "$LOG_FILE"
echo "=== Summary ===" | tee -a "$LOG_FILE"
echo "Completed: $(date)" | tee -a "$LOG_FILE"
echo "Total processed: $processed" | tee -a "$LOG_FILE"
echo "Failed: $failed" | tee -a "$LOG_FILE"
echo "Outbox drafts: $(ls "$OUTBOX_DIR"/*.md 2>/dev/null | grep -v README | wc -l | tr -d ' ')" | tee -a "$LOG_FILE"
