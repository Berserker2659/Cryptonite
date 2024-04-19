FROM ubuntu:22.04 AS chroot

RUN /usr/sbin/useradd --no-create-home -u 1000 user

RUN apt-get update && \
    apt-get install -y socat

COPY Zealot /home/user/chal
COPY flag.txt /home/user/flag.txt

RUN chmod 001 /home/user/chal
RUN chmod 004 /home/user/flag.txt

FROM gcr.io/kctf-docker/challenge@sha256:0f7d757bcda470c3bbc063606335b915e03795d72ba1d8fdb6f0f9ff3757364f AS runner

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      -T60 \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"nsjail --config /home/user/nsjail.cfg -- chal"
