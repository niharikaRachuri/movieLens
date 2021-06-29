FROM python:3
WORKDIR C:/Users/pvnsk/OneDrive/Desktop/buaProject
COPY . .
RUN pip3 install -r requirements.txt
CMD ["testPy.py"]
ENTRYPOINT ["python3"]