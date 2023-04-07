FROM alpine AS build
WORKDIR /dist
RUN apk add --no-cache --update curl
RUN echo -e '[General]\nAutoFind=0\n' > /dist/.vhui
RUN curl -fsSL https://www.virtualhere.com/sites/default/files/usbclient/vhclientx86_64 -o /dist/vhclientx86_64
RUN chmod +x /dist/vhclientx86_64

FROM alpine
# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY --from=build /dist/* /vhclient/
COPY run.sh /vhclient/
COPY src src
RUN chmod +x /vhclient/run.sh

ENV HOME=/vhclient
WORKDIR /vhclient

CMD /vhclient/run.sh