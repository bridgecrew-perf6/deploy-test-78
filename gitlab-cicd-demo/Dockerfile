FROM alpine:3.10.3

LABEL maintainer="basharenslak@godatadriven.com"

# Hadolint will fail here without ignoring anything
RUN apk update && apk add fortune

ENTRYPOINT ["fortune"]
