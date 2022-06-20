FROM python
WORKDIR /usr/src/app
COPY . .
RUN pip3 install flask
RUN pip3 install requests
CMD ["service-a.py"]
ENTRYPOINT ["python3"]