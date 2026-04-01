#!/usr/bin/env bash

# 1. Archive Directory Check
# Check if a directory named archive exists. If not, create it.
if [ ! -d "archive" ]; then
    mkdir archive
    echo "Created 'archive' directory."
fi

# 2. Timestamp Generation
# Create a string representing the current date and time.
# Format: YearMonthDay-HourMinuteSecond (e.g., 20260401-214500)
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# 3. The Archival Process
# Check if the file exists before trying to move it.
if [ -f "grades.csv" ]; then
    ORIGINAL_FILE="grades.csv"
    NEW_FILE="grades_$TIMESTAMP.csv"

    # Rename and move the file to the archive directory.
    mv "$ORIGINAL_FILE" "archive/$NEW_FILE"
    
    # 4. Workspace Reset
    # Create a new, empty grades.csv for the next batch.
    touch grades.csv
    
    # 5. Logging
    # Append details to organizer.log. This file accumulates entries.
    echo "[$TIMESTAMP] Archived: $ORIGINAL_FILE -> $NEW_FILE" >> organizer.log
    
    echo "Success: File archived and workspace reset."
else
    echo "Error: grades.csv not found in the current directory."
fi