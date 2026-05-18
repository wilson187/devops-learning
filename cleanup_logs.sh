#!/bin/sh

# This script checks the size of the cron log file and archives it if it exceeds a specified size limit.

LOG_FILE="logs/cron.log"
ARCHIVE_DIR="logs/archive"
MAX_SIZE=1048576 # 1mb in bytes

# Check if the log file exists
if [ -f "$LOG_FILE" ]; then
    FILE_SIZE=$(stat -c%s "$LOG_FILE")
    
    if [ $FILE_SIZE -gt $MAX_SIZE ]; then
        TIMESTAMP=$(date +%Y%m%d%H%M%S)
        ARCHIVE_FILE="$ARCHIVE_DIR/cron_backup_$TIMESTAMP.log"
        
        # Create archive directory if it doesn't exist
        mkdir -p "$ARCHIVE_DIR"
        
        # Move the log file to the archive directory
        mv "$LOG_FILE" "$ARCHIVE_FILE"
        
        # Clear the main log file
        > "$LOG_FILE"
        
        echo "Archived $LOG_FILE to $ARCHIVE_FILE and cleared the main log file."
    else
        echo "Log file size is within the limit. No action taken."
    fi
else
    echo "Log file $LOG_FILE does not exist."
fi