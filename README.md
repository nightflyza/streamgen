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

Example:

```bash
$ python3.11 streamgen.py 16
Starting RTSP stream 1: source file vids/5.mp4 at admin:password@0.0.0.0:8554/h264
Starting RTSP stream 2: source file vids/6.mp4 at admin:password@0.0.0.0:8555/h264
Starting RTSP stream 3: source file vids/8.mp4 at admin:password@0.0.0.0:8556/h264
Starting RTSP stream 4: source file vids/2.mp4 at admin:password@0.0.0.0:8557/h264
Starting RTSP stream 5: source file vids/7.mp4 at admin:password@0.0.0.0:8558/h264
Starting RTSP stream 6: source file vids/9.mp4 at admin:password@0.0.0.0:8559/h264
Starting RTSP stream 7: source file vids/3.mp4 at admin:password@0.0.0.0:8560/h264
Starting RTSP stream 8: source file vids/4.mp4 at admin:password@0.0.0.0:8561/h264
Starting RTSP stream 9: source file vids/10.mp4 at admin:password@0.0.0.0:8562/h264
Starting RTSP stream 10: source file vids/1.mp4 at admin:password@0.0.0.0:8563/h264
Starting RTSP stream 11: source file vids/5.mp4 at admin:password@0.0.0.0:8564/h264
Starting RTSP stream 12: source file vids/6.mp4 at admin:password@0.0.0.0:8565/h264
Starting RTSP stream 13: source file vids/8.mp4 at admin:password@0.0.0.0:8566/h264
Starting RTSP stream 14: source file vids/2.mp4 at admin:password@0.0.0.0:8567/h264
Starting RTSP stream 15: source file vids/7.mp4 at admin:password@0.0.0.0:8568/h264
Starting RTSP stream 16: source file vids/9.mp4 at admin:password@0.0.0.0:8569/h264
=====
Press ^C to shutdown all streams
```