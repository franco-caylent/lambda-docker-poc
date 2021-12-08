FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app/* ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.
WORKDIR ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

EXPOSE 5000

# Arguments
ARG VERSION
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# To run in docker, docker run -it -p 9000:8080 lambda-docker app.handler
# To run in lambda configure it to use the app.handler
#CMD [ "app.handler" ]

# For docker
#docker run -it -p 5000:5000 --entrypoint="" 131578276461.dkr.ecr.us-west-1.amazonaws.com/lambda-docker-poc:12 python3 -m flask  run --host=0.0.0.0
ENTRYPOINT []
CMD ["python3","-m", "flask", "run", "--host=0.0.0.0"]
