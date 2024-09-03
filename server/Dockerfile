FROM python

RUN pip install flask flask_restful
RUN mkdir /opt/recipes
COPY templates /opt/recipes
COPY *py /opt/recipes/
CMD /opt/recipes/server.py
