import os
import subprocess

def convertToH264NoSound(videoDir="vids"):
    if not os.path.exists(videoDir):
        print(f"Directory '{videoDir}' not found.")
        return

    videoFiles = [f for f in os.listdir(videoDir) if f.endswith(('.mp4', '.mkv', '.avi'))]
    
    if not videoFiles:
        print(f"No video files found in '{videoDir}'.")
        return

    for file in videoFiles:
        inputPath = os.path.join(videoDir, file)
        tempOutputPath = os.path.join(videoDir, f"temp_{file}")

        cmd = [
            "ffmpeg", "-i", inputPath, "-an",
            "-c:v", "libx264", "-crf", "23",
            "-preset", "fast", tempOutputPath
        ]

        print(f"Converting '{file}' to H.264 without audio...")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f"Replacing original file: {inputPath}")
            os.replace(tempOutputPath, inputPath)
        else:
            print(f"Failed to convert '{file}'. Error: {result.stderr.decode()}")

if __name__ == "__main__":
    convertToH264NoSound()
