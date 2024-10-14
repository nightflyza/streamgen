# RTSP Stream Generator

This simple script launches multiple RTSP streams using `cvlc`, looping through videos in the `vids/` directory.

## Usage
```bash
python3 streamgen.py <num_streams> [start_port] [stream_url]
```

## Options
 - <num_streams>: Number of streams to launch (required).
 - [start_port]: Initial port for the streams (default: 8554).
 - [stream_url]: Stream path (default: h264).
