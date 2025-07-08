import subprocess

subprocess.run(['git', 'clone', ''])

# subprocess.run(['cd', 'wazuh-docker/single-node/'])

yaml_text = """
services:
  generator:
    build:
      context: ../indexer-certs-creator
    volumes:
      - ./config/wazuh_indexer_ssl_certs/:/certificates/
      - ./config/certs.yml:/config/certs.yml
"""

with open("placeholder", "w") as file:
    file.write(yaml_text)

