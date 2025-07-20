FROM debian:bookworm

RUN apt update && apt install -y \
    avahi-daemon \
    dbus \
    python3 \
    python3-pip \
    curl

RUN pip install docker flask

COPY app.py /app.py

CMD ["python3", "/app.py"]
