FROM jenkins/jenkins:lts

USER root

# Install Python, pip, and Selenium dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip wget unzip && \
    apt-get clean

# Install Chrome and ChromeDriver for Selenium
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y /tmp/chrome.deb && \
    rm /tmp/chrome.deb

RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Add ChromeDriver to PATH
ENV PATH="/usr/local/bin:$PATH"

USER jenkins