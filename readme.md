# Telegram Info Bot
This is a Python Bot that can frequently get the **vps info** and push it to your **Telegram bot**.

<br>
<br>
<br>

## Info List
- CPU Usage
- Cache Usage
- Storage Usage

<br>
<br>
<br>

## Service Mornitor  *(only for CentOS)*
This function can check the service status and tells whether the service are running or down.

### Default Check Service
- Aria2
- Bt-Panel
- Bt-Task
- Nginx
- MySQL

### Add Service

You can add your own service by rewriting the variable `service_dict` in `config.py`

<br>
<br>
<br>

## Todo List

|Function|Introduction|Status|
|:-----:|:-----|:----|
|BetterFileStructure|Program File Struct Update|Not Start|
|Auto-Restart|When Service-Monitor detect a service-down situation, Using shell commend to restart the service and send a restart log.|Not Start|
|Auto Detect Sys|When starting, detect the system environment automatically and choose a right config and setting.(Now we just offer Ubuntu and CentOS version)|Not Start|