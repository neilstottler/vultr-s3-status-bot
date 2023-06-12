# vultr-s3-status-bot
I made a discord bot to check if vultr is having S3 issues cause NJ is cursed for some reason. It will check if an item on the bucket desigated in a config.yaml file is 200 and if it is check the response time to make sure it's less than 500ms.

# Note:
This has to be run as sudo due to a socket being created in order to ping a host.
