FROM python:3.9

#Set the current working directory to /code. This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code

#Copy and install requirements.txt
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#Copy app in code
COPY api-key /code/
COPY ./app /code/

#Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]