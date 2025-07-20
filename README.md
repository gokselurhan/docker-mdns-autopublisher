# Docker mDNS AutoPublisher

Bu sistem, Docker üzerinde çalışan tüm container'ları otomatik algılar ve `.local` olarak mDNS (avahi) üzerinden yayınlar.

## Özellikler

- Docker olaylarını dinler
- Her yeni container için hostname + IP'yi alır
- mDNS yayını yapar (`hostname.local`)
- Windows, Synology gibi sistemler bu adları otomatik görebilir

## Kurulum

```bash
git clone https://github.com/gokselurhan/docker-mdns-autopublisher.git
cd docker-mdns-autopublisher
docker compose up -d
