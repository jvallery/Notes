  

logger:

default: info

logs:

frigate.event: debug

  

mqtt:

enabled: true

host: ingress.vallery.net

topic_prefix: frigate

client_id: frigate

user: home

password: CeRr9gngypVNLnmypAxykwN7

  

# --- Detectors: ONNX (Frigate+ native) using Nvidia GPUs ---

detectors:

onnx_0:

type: onnx

device: '0'

onnx_1:

type: onnx

device: '1'

  

database:

path: /data/frigate.db

  

tls:

enabled: false

  

auth:

enabled: true

reset_admin_password: false

cookie_name: frigate_token

cookie_secure: true

session_length: 86400

refresh_time: 43200

failed_login_rate_limit: 10/minute

trusted_proxies:

- 172.16.0.0/12

- 192.168.0.0/16

- 10.0.4.0/24

hash_iterations: 600000

  

model:

path: plus://a3fd8c0d627ddfb65ffe15172de704ba

  

# --- Audio: Disabled Globally to fix crash loop ---

audio:

enabled: false

  
  

birdseye:

enabled: true

restream: true

width: 1920

height: 1080

quality: 8

mode: continuous

inactivity_threshold: 10

layout:

scaling_factor: 1.2

max_cameras: 9

  

ffmpeg:

hwaccel_args: preset-nvidia

input_args: preset-rtsp-restream

output_args:

detect: -threads 2 -f rawvideo -pix_fmt yuv420p

record: preset-record-generic-audio-aac

retry_interval: 10

apple_compatibility: true

  

# --- Global Detect: Default to typical Sub-stream size ---

detect:

width: 640

height: 480

fps: 5

enabled: true

min_initialized: 2

max_disappeared: 35

stationary:

interval: 25

threshold: 50

  

objects:

track: [person, car, dog, cat, face, license_plate]

filters:

person:

min_score: 0.75

threshold: 0.80

face:

min_score: 0.55

car:

min_score: 0.60

threshold: 0.80

  

review:

alerts:

enabled: true

labels: [car, person]

detections:

enabled: true

labels: [car, person, dog, cat, face, license_plate, package, amazon, ups, fedex]

  

record:

enabled: true

expire_interval: 60

sync_recordings: true

export:

timelapse_args: -vf setpts=0.04*PTS -r 30

alerts:

pre_capture: 5

post_capture: 5

retain:

days: 365

mode: active_objects

detections:

pre_capture: 5

post_capture: 5

retain:

days: 14

mode: active_objects

continuous:

days: 2

motion:

days: 2

  

snapshots:

enabled: true

clean_copy: true

timestamp: false

bounding_box: true

crop: false

retain:

default: 365

quality: 70

  

semantic_search:

enabled: true

reindex: false

model_size: large

  

face_recognition:

enabled: true

model_size: large

detection_threshold: 0.7

min_area: 3000

recognition_threshold: 0.92

unknown_score: 0.85

min_faces: 1

save_attempts: 150

blur_confidence_filter: true

  

lpr:

enabled: true

device: GPU

model_size: large

detection_threshold: 0.75

min_area: 2000

recognition_threshold: 0.9

min_plate_length: 4

format: None

match_distance: 1

known_plates: {}

enhancement: 2

debug_save_plates: true

  

go2rtc:

webrtc:

listen: :8555

ice_servers:

- urls: [stun:stun.l.google.com:19302]

candidates:

- 192.168.30.212:8555

- 192.168.10.212:8555

- 8.44.158.103:8555

- stun:8555

api:

listen: :1984

origin: '*'

log:

level: info

streams:

# Skycams

skycam_east:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.35:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

skycam_east_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.35:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

skycam_west:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.85:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

skycam_west_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.85:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Backyard

backyard_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.232:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.232:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.132:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.132:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_breezeway_rear:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.8:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_breezeway_rear_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.8:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_shed_corner:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.79:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_shed_corner_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.79:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_storageyard_gate:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.101:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_storageyard_gate_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.101:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_suite_sidewalk_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.176:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_suite_sidewalk_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.176:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_suite_sidewalk_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.181:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_suite_sidewalk_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.181:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_wall_sidewalk:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.122:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_wall_sidewalk_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.122:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

backyard_workshop_door:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.250:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

backyard_workshop_door_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.250:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Driveway

driveway_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.131:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

driveway_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.131:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

driveway_breezeway:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.114:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

driveway_breezeway_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.114:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

driveway_gate:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.55:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

driveway_gate_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.55:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

driveway_suite_door:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.247:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

driveway_suite_door_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.247:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Entryway

entryway_front_door:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.78:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

entryway_front_door_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.78:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Frontyard

frontyard_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.16:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

frontyard_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.16:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

frontyard_circle_driveway:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.199:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

frontyard_circle_driveway_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.199:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

frontyard_circle_driveway_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.89:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

frontyard_circle_driveway__2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.89:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

frontyard_garden:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.224:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

frontyard_garden_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.224:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Garage

garage_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.9:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

garage_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.9:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

garage_breezeway:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.133:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

garage_breezeway_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.133:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Panorama Cir

panorama_cir_gate:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.7:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

panorama_cir_gate_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.7:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

panorama_cir_north:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.127:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

panorama_cir_north_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.127:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

panorama_cir_west:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.234:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

panorama_cir_west_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.234:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Patio

patio_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.59:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

patio_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.59:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

patio_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.83:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

patio_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.83:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

patio_japanese_garden:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.98:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

patio_japanese_garden_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.98:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Pool

pool_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.126:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

pool_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.126:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

pool_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.84:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

pool_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.84:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Southyard

southyard_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.33:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

southyard_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.33:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

southyard_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.175:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

southyard_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.175:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

southyard_3:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.188:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

southyard_3_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.188:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Storageyard

storageyard_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.18:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

storageyard_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.18:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

storageyard_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.117:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

storageyard_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.117:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

storageyard_powerwall:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.32:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

storageyard_powerwall_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.32:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

# Greenhouse

greenhouse_1:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.146:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

greenhouse_1_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.146:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

greenhouse_2:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.118:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif

greenhouse_2_sub:

- rtsp://{FRIGATE_RTSP_USER}:{FRIGATE_RTSP_PASSWORD}@192.168.20.118:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

  

cameras:

# === Skycams (Substream Valid + Audio OK) ===

skycam_west:

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/skycam_west_sub # Substream for Detect

roles: [detect]

- path: rtsp://127.0.0.1:8554/skycam_west # Main for Record/Audio

roles: [audio, record]

detect:

width: 1024 # Probe result

height: 576

audio:

enabled: true

live:

streams:

Main Stream: skycam_west

Sub Stream: skycam_west_sub

onvif:

host: 192.168.20.85

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.833,0.039,0.832,0.128,0.961,0.136,0.97,0.034

  

skycam_east:

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/skycam_east_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/skycam_east

roles: [audio, record]

detect:

width: 1024

height: 576

audio:

enabled: true

onvif:

host: 192.168.20.35

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.833,0.026,0.837,0.135,0.957,0.139,0.949,0.029

  

# === Backyard (Mixed Substream Support, Audio mostly NONE) ===

backyard_1: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/backyard_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_1

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: backyard_1

Sub Stream: backyard_1_sub

onvif:

host: 192.168.20.232

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

zones:

backyard_zone:

coordinates: 0,0.231,0.327,0.057,0.327,0,1,0,1,1,0,1

garage_zone:

coordinates:

0.737,0.268,0.79,0.29,0.938,0.339,0.999,0.408,1,0.462,1,1,0.237,1,0.315,0.978,0.379,0.915,0.483,0.786,0.751,0.327

motion:

mask: 0.625,0.038,0.627,0.084,0.959,0.085,0.962,0.036

objects:

filters:

car:

mask: 0.113,0.713,0.07,0.307,0.056,0.201,0.001,0.23,0.001,1,0.153,1

  

backyard_2: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/backyard_2_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_2

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: backyard_2

Sub Stream: backyard_2_sub

onvif:

host: 192.168.20.132

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

zones:

backyard_zone:

coordinates:

1,0.232,1,1,0,1,0.028,0.788,0.136,0.413,0.225,0.374,0.205,0.231,0.662,0.089,0.735,0.147,0.823,0.125

garage_zone:

coordinates:

0.501,1,0.372,0.453,0.376,0.363,0.359,0.242,0.227,0.242,0.129,0.303,0.002,0.556,-0.001,0.997

motion:

mask: 0.626,0.033,0.624,0.083,0.974,0.085,0.97,0.021

objects:

filters:

car:

mask:

0.57,0.293,0.751,0.243,0.723,0.098,0.671,0.075,0.376,0.166,0.37,0.234,0.377,0.333,0.566,0.259

  

backyard_breezeway_rear: # Substream OK, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/backyard_breezeway_rear_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_breezeway_rear

roles: [audio, record]

detect:

width: 640

height: 480

audio:

enabled: true

live:

streams:

Main Stream: backyard_breezeway_rear

Sub Stream: backyard_breezeway_rear_sub

onvif:

host: 192.168.20.8

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

zones:

garage_zone:

coordinates:

0.001,0.269,0.153,0.158,0.449,0.067,0.618,0.059,0.696,0.063,0.792,0.11,0.898,0.303,0.869,0.413,0.735,0.994,0.001,0.994

backyard_zone:

coordinates:

0.997,1,0.999,0.353,0.889,0.303,0.676,0.197,0.095,0.502,0.047,0.551,0.003,0.841,0.004,0.996

motion:

mask: 0.628,0.034,0.626,0.083,0.97,0.087,0.971,0.037

threshold: 30

contour_area: 20

improve_contrast: true

objects:

filters:

car:

mask: 0.289,0.116,0.295,0.269,0.572,0.181,0.58,0.061

  

backyard_shed_corner: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/backyard_shed_corner_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_shed_corner

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: backyard_shed_corner

Sub Stream: backyard_shed_corner_sub

onvif:

host: 192.168.20.79

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

zones:

backyard_zone:

coordinates:

0,0,0.082,0,0.165,0.096,0.48,0.057,0.747,0.262,1,0.499,1,1,0,1

motion:

mask: 0.704,0.033,0.702,0.082,0.969,0.081,0.972,0.037

  

backyard_storageyard_gate: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/backyard_storageyard_gate_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_storageyard_gate

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: backyard_storageyard_gate

Sub Stream: backyard_storageyard_gate_sub

zones:

backyard_zone:

coordinates:

0,0.75,0.075,0.565,0.111,0.642,0.348,0.262,0.565,0,1,0,1,1,0,1

onvif:

host: 192.168.20.101

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.703,0.04,0.702,0.081,0.967,0.081,0.968,0.033

objects:

filters:

car:

mask: 0.83,0.381,0.474,0.11,0.563,0.002,0.998,0,1,0.436

  

backyard_suite_sidewalk_1: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/backyard_suite_sidewalk_1

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: backyard_suite_sidewalk_1

Sub Stream: backyard_suite_sidewalk_1_sub

objects:

track: [person, dog, cat, face]

zones:

backyard_zone:

coordinates:

0,0.201,0.054,0.152,0.061,0.184,0.243,0.08,0.449,0,1,0,1,1,0,1

inertia: 3

loitering_time: 0

onvif:

host: 192.168.20.176

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.702,0.032,0.702,0.087,0.973,0.084,0.971,0.032

lpr:

enabled: false

  

backyard_suite_sidewalk_2: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/backyard_suite_sidewalk_2

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: backyard_suite_sidewalk_2

Sub Stream: backyard_suite_sidewalk_2_sub

objects:

track: [person, dog, cat, face]

zones:

backyard_zone:

coordinates:

0,0,0.229,0,0.457,0.03,0.458,0.065,0.747,0.203,1,0.416,1,1,0,1

inertia: 3

loitering_time: 0

onvif:

host: 192.168.20.181

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.702,0.038,0.704,0.078,0.969,0.078,0.967,0.029

lpr:

enabled: false

  

backyard_wall_sidewalk: # Substream OK, Audio OK -> Sub + Audio

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/backyard_wall_sidewalk_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_wall_sidewalk

roles: [record, audio]

detect:

width: 640

height: 480

audio:

enabled: true

live:

streams:

Main Stream: backyard_wall_sidewalk

Sub Stream: backyard_wall_sidewalk_sub

objects:

track: [person, dog, cat, face]

zones:

backyard_zone:

coordinates: 0,0.819,0.368,0.606,0.475,0.438,0.742,0.444,1,0.567,1,1,0,1

onvif:

host: 192.168.20.122

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.503,0.032,0.503,0.103,0.952,0.102,0.952,0.029

lpr:

enabled: false

  

backyard_workshop_door: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/backyard_workshop_door_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/backyard_workshop_door

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: backyard_workshop_door

Sub Stream: backyard_workshop_door_sub

zones:

backyard_zone:

coordinates:

0,0.119,0.339,0,0.343,0.103,0.643,0.128,0.821,0.186,0.95,0.243,0.95,0.274,1,0.293,1,1,0,1

onvif:

host: 192.168.20.250

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.702,0.038,0.7,0.084,0.971,0.079,0.972,0.032

  

# === Driveway ===

driveway_1: # LPR High Res Request (Substream is offline anyway), Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/driveway_1

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: driveway_1

Sub Stream: driveway_1_sub

zones:

driveway_zone:

coordinates:

0,0.129,0.053,0.059,0.08,0.016,0.085,0.071,0.258,0.057,0.33,0.043,0.412,0.023,0.475,0,1,0,1,1,0,1

garage_zone:

coordinates:

0.872,0.211,0.87,0.543,0.998,0.695,1,0.999,0.209,1,0.077,0.668,0.215,0.512,0.41,0.293,0.651,0.075,0.82,0.176

onvif:

host: 192.168.20.131

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.701,0.035,0.701,0.084,0.969,0.081,0.969,0.035

  

driveway_breezeway: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/driveway_breezeway

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: driveway_breezeway

Sub Stream: driveway_breezeway_sub

zones:

driveway_zone:

coordinates: 0,0,1,0,1,1,0,1

garage_zone:

coordinates: 0,0,0.999,0.002,1,1,0,1

onvif:

host: 192.168.20.114

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.699,0.033,0.7,0.082,0.971,0.086,0.971,0.034

  

driveway_gate: # LPR High Res Request (Using Main stream), Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/driveway_gate

roles: [audio, record, detect]

detect:

width: 1920 # Using Main stream for LPR

height: 1080

audio:

enabled: true

live:

streams:

Main Stream: driveway_gate

Sub Stream: driveway_gate_sub

zones:

panorama_cir_zone:

coordinates: 0.507,0,0.841,0,0.813,0.089,0.751,0.121,0.512,0.134

frontyard_zone:

coordinates: 0,0,0.505,0,0.507,0.096,0.493,0.116,0.409,0.168,0,0.527

gate_zone:

coordinates:

0,0.534,0.167,0.37,0.295,0.257,0.402,0.181,0.511,0.099,0.515,0.219,0.782,0.272,0.782,0.201,0.817,0.213,0.832,0.349,0.784,1,0,1

inertia: 3

loitering_time: 0

onvif:

host: 192.168.20.55

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.735,0.043,0.732,0.102,0.913,0.099,0.92,0.041

  

driveway_suite_door: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/driveway_suite_door

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: driveway_suite_door

Sub Stream: driveway_suite_door_sub

zones:

driveway_zone:

coordinates:

0,0,0.12,0,0.124,0.178,0.433,0.097,0.404,0.086,0.438,0.082,0.52,0.098,0.64,0.113,0.732,0.127,0.728,0.187,0.758,0.269,0.798,0.329,0.853,0.4,1,0.482,1,1,0,1

panorama_cir_zone:

coordinates:

0.87,0.146,0.873,0,1,0,1,0.492,0.83,0.371,0.757,0.263,0.729,0.186,0.731,0.128

frontyard_zone:

coordinates:

0.125,0.173,0.122,0,0.871,0.002,0.868,0.142,0.733,0.125,0.528,0.095,0.442,0.077,0.401,0.083,0.427,0.097

onvif:

host: 192.168.20.247

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

  

# === Entryway ===

entryway_front_door: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/entryway_front_door

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: entryway_front_door

Sub Stream: entryway_front_door_sub

objects:

track: [person, dog, cat, face]

zones:

entryway:

coordinates: 0,0,0.204,0,0.247,0.629,0.627,0.499,0.664,0,1,0,1,1,0,1

frontyard_zone:

coordinates: 0,0,1,0,1,1,0,1

inertia: 3

loitering_time: 0

onvif:

host: 192.168.20.78

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.933,0.082,0.825,0.086,0.824,0.036,0.932,0.036

lpr:

enabled: false

  

# === Frontyard ===

frontyard_1: # Substream OK, Audio OK -> Sub + Audio

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/frontyard_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/frontyard_1

roles: [audio, record]

detect:

width: 640

height: 480

audio:

enabled: true

live:

streams:

Main Stream: frontyard_1

Sub Stream: frontyard_1_sub

zones: {}

onvif:

host: 192.168.20.16

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.973,0.084,0.971,0.027,0.834,0.029,0.836,0.089

  

frontyard_circle_driveway: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/frontyard_circle_driveway

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: frontyard_circle_driveway

Sub Stream: frontyard_circle_driveway_sub

zones:

frontyard_zone:

coordinates:

0,0.268,0.406,0.202,0.799,0.223,1,0.288,0.89,0.291,0.887,0.402,0.954,0.456,0.962,0.337,1,0.357,1,1,0,1

onvif:

host: 192.168.20.199

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.969,0.082,0.969,0.034,0.862,0.036,0.86,0.084

  

frontyard_circle_driveway_2: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/frontyard_circle_driveway_2

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: frontyard_circle_driveway_2

Sub Stream: frontyard_circle_driveway__2_sub

zones:

frontyard_zone:

coordinates:

0,0.242,0.263,0.087,0.458,0.039,0.665,0.018,1,0.054,1,0.175,0.786,0.132,0.782,0.365,0.833,0.619,0.87,0.25,0.893,0.304,0.965,0.313,1,0.342,1,1,0,1

inertia: 3

loitering_time: 0

gate_zone:

coordinates:

0.833,0.619,0.443,0.839,0.507,0.285,0.573,0.325,0.715,0.354,0.782,0.361,0.786,0.132,0.87,0.25

loitering_time: 0

inertia: 3

gate_exit:

coordinates: 0.782,0.361,0.833,0.621,0.601,0.75,0.601,0.332

loitering_time: 0

objects: [car, person]

onvif:

host: 192.168.20.89

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.97,0.081,0.969,0.043,0.86,0.041,0.861,0.083

  

frontyard_garden: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/frontyard_garden

roles: [record, detect]

detect:

width: 1920

height: 1080

zones:

frontyard_zone:

coordinates: 0.003,0.2,0.309,0.129,0.502,0.127,0.84,0.187,1,0.29,1,1,0,1

live:

streams:

Main Stream: frontyard_garden

Sub Stream: frontyard_garden_sub

onvif:

host: 192.168.20.224

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.859,0.035,0.861,0.081,0.972,0.08,0.971,0.034

  

# === Garage ===

garage_1: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/garage_1

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: garage_1

Sub Stream: garage_1_sub

objects:

track: [person, dog, cat]

zones:

garage_zone:

coordinates: 0,1,0,0,1,0,1,1

onvif:

host: 192.168.20.9

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.918,0.078,0.918,0.039,0.877,0.037,0.878,0.08

lpr:

enabled: false

  

garage_breezeway: # Substream OFFLINE, Audio NONE -> Main

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/garage_breezeway

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: garage_breezeway

Sub Stream: garage_breezeway_sub

objects:

track: [person, dog, cat]

zones:

garage_zone:

coordinates: 0,0,1,0,1,1,0,1

onvif:

host: 192.168.20.133

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

lpr:

enabled: false

  

# === Panorama Cir ===

panorama_cir_gate: # LPR High Res Request (Substream is offline anyway), Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/panorama_cir_gate

roles: [record, detect]

detect:

width: 1920

height: 1080

live:

streams:

Main Stream: panorama_cir_gate

Sub Stream: panorama_cir_gate_sub

zones:

panorama_cir_zone:

coordinates: 0,0,0.718,0,0.651,0.317,0,1

backyard_zone:

coordinates:

0.06,1,1,0.999,1,0.494,0.801,0.258,0.746,0.208,0.696,0.261,0.673,0.343

onvif:

host: 192.168.20.7

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.968,0.081,0.969,0.031,0.858,0.039,0.862,0.084

  

panorama_cir_north: # LPR High Res Request, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/panorama_cir_north

roles: [audio, record, detect]

detect:

width: 1920

height: 1080

audio:

enabled: true

live:

streams:

Main Stream: panorama_cir_north

Sub Stream: panorama_cir_north_sub

zones:

driveway_zone:

coordinates:

0.58,0.737,0.686,0.691,0.824,0.71,0.998,0.701,1,1,0.002,0.998,0.001,0.896,0.261,0.827,0.46,0.776

panorama_cir_zone:

coordinates:

0.002,0.697,0.003,0.895,0.687,0.687,0.631,0.642,0.63,0.503,0.626,0.453,0.549,0.45,0.43,0.553,0.344,0.629,0.24,0.663,0.112,0.684

onvif:

host: 192.168.20.127

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.954,0.102,0.953,0.033,0.772,0.039,0.775,0.095

  

panorama_cir_west: # LPR High Res Request, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/panorama_cir_west

roles: [audio, record, detect]

detect:

width: 1920

height: 1080

audio:

enabled: true

live:

streams:

Main Stream: panorama_cir_west

Sub Stream: panorama_cir_west_sub

zones:

driveway_zone:

coordinates:

0.155,0.458,0.164,0.648,0.273,0.853,0.41,0.907,1,1,0,1,0,0.506,0.079,0.494

panorama_cir_zone:

coordinates:

0.157,0.455,0.332,0.352,0.33,0,1,0,1,1,0.414,0.902,0.274,0.852,0.164,0.649

frontyard_zone:

coordinates:

0,0.237,0.335,0.221,0.328,0.355,0.285,0.381,0.192,0.43,0.095,0.479,0,0.496

onvif:

host: 192.168.20.234

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

  

# === Patio ===

patio_1: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/patio_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/patio_1

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: patio_1

Sub Stream: patio_1_sub

objects:

track: [person, dog, cat, face]

zones:

patio_zone:

coordinates:

0,0.196,0.107,0.139,0.165,0.074,0.249,0.07,0.432,0.052,0.459,0.085,0.561,0.059,0.76,0.169,0.766,0.026,0.834,0.039,0.813,0.208,1,0.375,1,0.515,1,0.993,0,1,0,0.413

inertia: 3

loitering_time: 0

pool_deck_zone:

coordinates:

0.046,0.64,0.001,0.441,0.002,0.366,0.038,0.32,0.081,0.42,0.083,0.523,0.088,0.638

inertia: 3

loitering_time: 0

objects: person

onvif:

host: 192.168.20.59

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.922,0.083,0.922,0.036,0.848,0.039,0.843,0.083

lpr:

enabled: false

  

patio_2: # Substream OK, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/patio_2_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/patio_2

roles: [record, audio]

detect:

width: 1024

height: 576

audio:

enabled: true

live:

streams:

Main Stream: patio_2

Sub Stream: patio_2_sub

objects:

track: [person, dog, cat, face]

zones:

patio_zone:

coordinates:

0.24,0.495,0.274,0.472,0.325,0.451,0.294,0.321,0.287,0.221,0.432,0.206,0.432,0.296,0.566,0.304,0.614,0.323,0.63,0.32,0.793,0.41,0.881,0.475,0.925,0.535,0.982,0.6,1,0.621,1,0.997,0,0.997,0,0.64,0.044,0.572,0.18,0.515

inertia: 3

loitering_time: 0

objects: person

pool_deck_zone:

coordinates:

0.354,1,0.361,0.893,0.499,0.804,0.569,0.756,0.697,0.81,0.815,0.827,0.895,0.862,0.957,0.861,1,0.882,1,1

inertia: 3

loitering_time: 0

japanese_garden_zone:

coordinates:

0.191,0.543,0.239,0.526,0.24,0.495,0.324,0.451,0.293,0.31,0.288,0.232,0.193,0.284,0.047,0.508,0.044,0.572,0.18,0.515

loitering_time: 0

objects: person

onvif:

host: 192.168.20.146

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.956,0.125,0.952,0.038,0.826,0.036,0.815,0.142

lpr:

enabled: false

  

patio_japanese_garden: # Substream OK, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/patio_japanese_garden_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/patio_japanese_garden

roles: [record, audio]

detect:

width: 640

height: 480

audio:

enabled: true

live:

streams:

Main Stream: patio_japanese_garden

Sub Stream: patio_japanese_garden_sub

objects:

track: [person, dog, cat, face]

zones:

japanese_garden_zone:

coordinates:

0,0.714,0,0.457,0.375,0.252,0.582,0.256,0.804,0.256,0.832,0.421,0.94,0.782,0.581,0.765,0.579,1,0.391,1,0.393,0.757

loitering_time: 0

inertia: 3

onvif:

host: 192.168.20.98

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

lpr:

enabled: false

  

# === Pool ===

pool_1: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/pool_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/pool_1

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: pool_1

Sub Stream: pool_1_sub

objects:

track: [person, dog, cat, face]

zones:

pool_deck_zone:

coordinates: 0,0,1,0,1,1,0,1,0,0.473

pool_water_zone:

coordinates:

0,0.482,0.161,0.216,0.178,0.21,0.192,0.185,0.267,0.169,0.343,0.166,0.37,0.178,0.42,0.176,0.422,0.201,0.449,0.203,0.603,0.665,0.551,0.672,0.63,1,0,1

onvif:

host: 192.168.20.126

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.817,0.021,0.821,0.113,0.957,0.109,0.948,0.025

lpr:

enabled: false

  

pool_2: # Substream OK, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/pool_2_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/pool_2

roles: [record, audio]

detect:

width: 640

height: 480

max_disappeared: 60

stationary:

interval: 15

threshold: 60

audio:

enabled: true

live:

streams:

Main Stream: pool_2

Sub Stream: pool_2_sub

objects:

track: [person, dog, cat, face]

zones:

pool_water_zone:

coordinates:

0.34,0.195,0.412,0.139,0.467,0.137,0.504,0.134,0.646,0.316,0.629,0.326,0.678,0.403,0.626,0.433,0.625,0.548,0.597,0.601,0.573,0.658,0.54,0.673,0.494,0.667,0.416,0.581,0.322,0.637,0.332,0.505,0.305,0.521

pool_deck_zone:

coordinates:

0.064,0.998,0.249,0.339,0.299,0.192,0.477,0.101,0.648,0.119,0.75,0.315,0.938,0.696,1,0.998,0.303,0.998

onvif:

host: 192.168.20.84

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

lpr:

enabled: false

  

# === Southyard ===

southyard_1: # Substream OK, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/southyard_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/southyard_1

roles: [record, audio]

detect:

width: 640

height: 480

audio:

enabled: true

live:

streams:

Main Stream: southyard_1

Sub Stream: southyard_1_sub

onvif:

host: 192.168.20.33

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask:

- 0.149,0.976,0.213,0.871,0.265,0.934,0.238,0.998,0.165,0.999

- 0.836,0.089,0.974,0.084,0.969,0.041,0.832,0.034

- 0.144,0.999,0.117,0.682,0.101,0.336,0.001,0.339,0.002,0.999

zones:

southyard_zone:

coordinates:

0.392,0.232,0.512,0.216,0.642,0.234,0.775,0.305,0.879,0.379,0.939,0.424,0.983,0.472,0.997,0.486,0.999,0.999,0.002,0.999,0.001,0.702,0.039,0.669,0.096,0.474,0.161,0.467,0.199,0.435,0.21,0.495,0.258,0.451,0.249,0.395

loitering_time: 0

inertia: 3

gazebo_zone:

coordinates: 0.208,0.484,0.184,0.359,0.235,0.311,0.258,0.451

loitering_time: 0

  

southyard_2: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/southyard_2_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/southyard_2

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: southyard_2

Sub Stream: southyard_2_sub

onvif:

host: 192.168.20.175

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask:

- 0.306,0.835,0.44,0.758,0.514,0.923,0.409,1,0.355,0.996,0.352,0.986

- 0.425,0.998,0.375,0.424,0.41,0,0,0,0,1

zones:

southyard_zone:

coordinates:

1,0.995,1,0.294,0.879,0.205,0.874,0.24,0.625,0.216,0.62,0.304,0.523,0.3,0.524,0.09,0.439,0.082,0.346,0.126,0.162,0.146,0,0.168,0,1

loitering_time: 0

inertia: 3

gazebo_zone:

coordinates: 0.523,0.3,0.531,0.107,0.63,0.112,0.62,0.304

loitering_time: 0

  

southyard_3: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/southyard_3_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/southyard_3

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: southyard_3

Sub Stream: southyard_3_sub

onvif:

host: 192.168.20.188

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

  

# === Storageyard ===

storageyard_1: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/storageyard_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/storageyard_1

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: storageyard_1

Sub Stream: storageyard_1_sub

objects:

track: [person, dog, cat, face]

zones:

storageyard_zone:

coordinates:

0,0.817,0.381,0.615,0.645,0.424,0.826,0.302,0.836,0,1,0,1,1,0,1

onvif:

host: 192.168.20.18

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.852,0.036,0.856,0.082,0.971,0.08,0.97,0.033

lpr:

enabled: false

  

storageyard_2: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/storageyard_2_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/storageyard_2

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: storageyard_2

Sub Stream: storageyard_2_sub

objects:

track: [person, dog, cat, face]

filters:

cat:

mask: 0.174,0.516,0.212,0.999,0.998,0.996,1,0.788,0.527,0.495

zones:

storageyard_zone:

coordinates:

0,0,0.178,0,0.173,0.098,0.354,0.104,0.347,0.2,0.658,0.46,1,0.777,1,1,0,1

onvif:

host: 192.168.20.117

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.809,0.034,0.808,0.083,0.922,0.083,0.923,0.035

lpr:

enabled: false

  

storageyard_powerwall: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/storageyard_powerwall_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/storageyard_powerwall

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: storageyard_powerwall

Sub Stream: storageyard_powerwall_sub

objects:

track: [person, dog, cat, face]

zones:

backyard_zone:

coordinates:

0,0.213,0.357,0.248,0.36,0.361,0.507,0.356,0.509,0.454,0.563,0.453,0.563,0.327,1,0.676,1,1,0,1

onvif:

host: 192.168.20.32

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.854,0.033,0.855,0.089,0.965,0.084,0.971,0.035

lpr:

enabled: false

  

# === Greenhouse ===

greenhouse_1: # Substream OK, Audio NONE

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 1

inputs:

- path: rtsp://127.0.0.1:8554/greenhouse_1_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/greenhouse_1

roles: [record]

detect:

width: 640

height: 480

live:

streams:

Main Stream: greenhouse_1

Sub Stream: greenhouse_1_sub

objects:

track: [person, dog, cat, face]

zones:

greenhouse_zone:

coordinates: 0,0,1,0,1,1,0,1

inertia: 3

loitering_time: 0

onvif:

host: 192.168.20.146

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.852,0.036,0.856,0.082,0.971,0.08,0.97,0.033

lpr:

enabled: false

  

greenhouse_2: # Substream OK, Audio OK

ffmpeg:

hwaccel_args: -hwaccel cuda -hwaccel_device 0

inputs:

- path: rtsp://127.0.0.1:8554/greenhouse_2_sub

roles: [detect]

- path: rtsp://127.0.0.1:8554/greenhouse_2

roles: [record, audio]

detect:

width: 704

height: 480

audio:

enabled: true

live:

streams:

Main Stream: greenhouse_2

Sub Stream: greenhouse_2_sub

objects:

track: [person, dog, cat, face]

zones:

greenhouse_zone:

coordinates:

0,0,0.269,0,0.283,0.322,0.375,0.315,0.373,0,1,0,1,0.777,1,1,0,1

inertia: 3

loitering_time: 0

onvif:

host: 192.168.20.118

port: 80

user: '{FRIGATE_RTSP_USER}'

password: '{FRIGATE_RTSP_PASSWORD}'

tls_insecure: false

ignore_time_mismatch: true

motion:

mask: 0.864,0.029,0.863,0.078,0.977,0.078,0.978,0.031

lpr:

enabled: false

  

camera_groups:

Backyard:

cameras:

- backyard_1

- backyard_2

- backyard_breezeway_rear

- backyard_shed_corner

- backyard_storageyard_gate

- backyard_suite_sidewalk_1

- backyard_suite_sidewalk_2

- backyard_wall_sidewalk

- backyard_workshop_door

  

Driveway:

cameras:

- driveway_1

- driveway_breezeway

- driveway_gate

- driveway_suite_door

  

Entryway:

cameras:

- entryway_front_door

  

Frontyard:

cameras:

- frontyard_1

- frontyard_circle_driveway

- frontyard_garden

- frontyard_circle_driveway_2

  

Garage and Driveway:

cameras:

- driveway_1

- driveway_breezeway

- garage_1

- garage_breezeway

- backyard_breezeway_rear

  

Panorama_Cir:

cameras:

- panorama_cir_gate

- panorama_cir_north

- panorama_cir_west

  

Patio:

cameras:

- patio_1

- patio_2

- patio_japanese_garden

  

Pool:

cameras:

- pool_1

- pool_2

  

Southyard:

cameras:

- southyard_1

- southyard_2

- southyard_3

  

Storageyard:

cameras:

- storageyard_1

- storageyard_2

- storageyard_powerwall

  

version: 0.17-0