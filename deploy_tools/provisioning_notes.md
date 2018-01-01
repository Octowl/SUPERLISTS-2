Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install nginx git python3.6 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com
* replace USERNAME with, e.g., nonrootuser

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com
* replace USERNAME with, e.g., nonrootuser

## Folder structure:
Assume we have a user account at /home/USERNAME

/home/USERNAME
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
