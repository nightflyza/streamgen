import os
import subprocess
import itertools
import sys

def launchRtspStreams(numStreams, startPort=8554, videoDir="vids", streamUrl="h264"):
    authLogin="admin"
    authPassword="password"
    streamHost="0.0.0.0"

    videoFiles = [os.path.join(videoDir, f) for f in os.listdir(videoDir) if f.endswith(('.mp4', '.mkv', '.avi'))]
    if not videoFiles:
        print(f"Any existing files in {videoDir} directory")
        sys.exit(1)

    videoCycle = itertools.cycle(videoFiles)
    processes = []

    for i in range(numStreams):
        port = startPort + i
        videoFile = next(videoCycle)
        
        cmd = [
            "cvlc", "--random", "--loop", videoFile,
            f":sout=#gather:rtp{{sdp=rtsp://{authLogin}:{authPassword}@{streamHost}:{port}/{streamUrl}}}",
            ":network-caching=1500", ":sout-all", ":sout-keep"
        ]

        print(f"Starting RTSP stream {i + 1}: file {videoFile} at {authLogin}:{authPassword}@{streamHost}:{port}/{streamUrl}")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)

    print("=====\nPress ^C to shutdown streams")
    return processes

def renderHelp():
    print(
        "Usage: python streamgen.py <num_streams> [start_port] [stream_url]\n"
        "  <num_streams>  : Number of RTSP streams to start (required)\n"
        "  [start_port]   : Initial port for the streams (default: 8554)\n"
        "  [stream_url]   : URL path for the stream (default: h264)\n"
    )

if __name__ == "__main__":
    if len(sys.argv) == 1:
        renderHelp()
        sys.exit(0)

    try:
        numStreams = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Error: <num_streams> must be a valid integer.")
        renderHelp()
        sys.exit(1)

    startPort = int(sys.argv[2]) if len(sys.argv) > 2 else 8554
    streamUrl = sys.argv[3] if len(sys.argv) > 3 else "h264"

    processes = launchRtspStreams(numStreams, startPort=startPort, streamUrl=streamUrl)

    try:
        for process in processes:
            process.wait()
    except KeyboardInterrupt:
        print("Shutting down streams...")
        for process in processes:
            process.terminate()
