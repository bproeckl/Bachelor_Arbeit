FROM ghcr.io/mindee/doctr:torch-py3.9.18-cpu-2024-05 as build-base
WORKDIR /workdir

# Install OpenJDK 11 and other dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    curl \
    wget \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN wget -qO- https://get.nextflow.io | bash && \
    chmod +x nextflow && \
    mv nextflow /usr/local/bin/
COPY . .

CMD ["python3", "workflowstarter.py", "-c"]