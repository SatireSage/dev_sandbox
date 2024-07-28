FROM alpine:latest

# Install OpenSSH
RUN apk update && apk add openssh

# Configure SSH
RUN echo 'root:password' | chpasswd
RUN mkdir -p /run/openrc && touch /run/openrc/softlevel
RUN rc-update add sshd
RUN rc-service sshd start

# Expose SSH port
EXPOSE 22

# Command to run the SSH service
CMD ["/usr/sbin/sshd", "-D"]
