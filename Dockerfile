FROM byran/python-screenplay
LABEL maintainer="Byran Wills-Heath"

COPY --chown=user:user . /home/user/files/

WORKDIR /home/user/files
RUN ./create_virtual_environment.sh
RUN ./install_requirements.sh
