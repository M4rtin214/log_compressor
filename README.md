# log_compressor
Log files compression script
- The script goes through the *.log files in "PATH" and compress to gzip files, replace the original file with an empty file

### Use with crone:
> sudo apt install cron  
> crontab -e  
> 0 9 1 * * python3 /path/to/my/script  
