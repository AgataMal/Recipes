FROM python

RUN pip install flask flask_restful
RUN mkdir -p /opt/recipes/templates
COPY templates/* /opt/recipes/templates/
COPY *py /opt/recipes/
CMD /opt/recipes/server.py
