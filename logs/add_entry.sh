if [ -z "$1" ]; then
    echo "Error: No message provided"
    echo "Usage: bash add_entry.sh 'your message'"
    exit 1
fi
echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> logs/system.log
echo "Entry added successfully."