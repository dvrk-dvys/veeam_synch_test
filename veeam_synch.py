import os
import argparse
import hashlib
import datetime
import time



# Synchronization must be one-way: after the synchronization content of the
# store folder should be modified to exactly match content of the source
# folder;

def logger(event, source_path, replica_path, log_path):
    # File creation/copying/removal operations should be logged to a file and to the console output;
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, 'w') as file:
        if event == 'create':
            logged = f"\n {timestamp}: File copied: {source_path} -> {replica_path}"
        elif event == 'copy':
            logged = f"\n {timestamp}: Directory created: {replica_path}"
        elif event == 'delete':
            logged = f"\n {timestamp}: File removed: {replica_path}"
        file.write(logged)
    print(logged)
    return logged


def synch_folders(source_path, replica_path, interval, log_file):
    md5_hash = hashlib.md5()



    while True:
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            source_contents = os.listdir(source_path)
            # os.scandir(source_path) as entries:
            print(source_contents, timestamp)
            time.sleep(interval)

        except KeyboardInterrupt:
            print("Synch ended.")
            break

    return None


if __name__ == "__main__":
    # Folder paths, synchronization interval and log file path should be provided using the command line arguments;
    parser = argparse.ArgumentParser(description="Run older synch")
    parser.add_argument("--source_path", required=True, help="Path to the source folder")
    parser.add_argument("--replica_path", required=True, default="./store", help="Path to the stored replicas folder")
    parser.add_argument("--interval", required=True, type=int, default=8, help="Synch interval in seconds")
    parser.add_argument("--log_file", required=True, default="./logs/log_run_0.txt", help="Path to the log file")

    args = parser.parse_args()

    synch_folders(args.source_path, args.replica_path, args.interval, args.log_file)

    # !python veeam_synch.py --source_path "./source" --replica_path ./store --interval 5 --log_file "./logs/log_run_0.txt"