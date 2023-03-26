# log_compressor
Simple log compressor script
- The script goes through the *.log files in "PATH" and compress to gzip files, replaces the original file with an empty file and overwrites the existing gzip file compression

### Use with crone:
> sudo apt install cron  
> crontab -e  
> 0 9 1 * * python3 /path/to/my/script  
