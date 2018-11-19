FROM python:3.7

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y curl \
    && rm -rf /var/lib/apt/lists/*

# Install yarn
# RUN apt-get update
# RUN apt-get install -y apt-transport-https 

# RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
# RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# RUN apt-get install -y yarn

# Install node/npm
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

WORKDIR /app/app
COPY requirements.txt /app/app
RUN pip install -r requirements.txt

COPY package*.json /app/app/
RUN npm install -qy

COPY . /app/app

WORKDIR /app/app/project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]