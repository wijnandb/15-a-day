--- 
draft: true
title: "Setting up Amazon S3 for user-uploaded files on Django Heroku"
date: "2021-09-03T13:33:13+0200"
layout: post
tags: ["static files","user upload", "heroku","amazon S3", "django","notes"]
slug: "setting-up-amazon-s3-for-user-uploaded-files-on-django-heroku"
---


For the Bredeschool project, we need teachers to upload a document proving that are allowed to teach kids (in Dutch: VOG, literally translated "Declaration about behavior").

The application is hosted on Heroku with Whitenoise installed, but that doesn't support uploaded content. The advice is to use Amazon S3. So, assuming I will do this more often in the future, I decided to take notes. You are looking at them :smiley:.

First of all, I need to create an S3 bucket. That shouldn't be too hard, although I have some trouble unnderstanding the implications of choosing the access level (I chose Allow *all* public access) and encryption (*on*). For this specific purpose I also chose the option of "Object lock", meaning an uploaded document can not be overwritten.

I am adviced to use *django-storages* and since I chose Amazon S3 as a storage location, I will need *S3Boto3Storage* as well.

```bash
$ pipenv install django-storages
$ pipenv install boto3
```

Then add the right settings to the Django SETTINGS file:
```
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

Getting the S3 credentials is quite a task, lots of settings and forms to fill out. I have created a policy, applied the policy to a group and created a user to be a member of that group.

So, I now have the Acces_key_ID and the Secret Access Key. I put them in my local .env variables (don't forget to put them in the Config vars in the Settings on Heroku as well).

Some more settings:
```
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'no-need-to-share-real-name-here'
AWS_S3_REGION_NAME = 'eu-central-1'
```

At this point, I should be able to upload files to the S3 bucket from the local Django admin, so let's give that a try.

An error occurred (InvalidAccessKeyId) when calling the PutObject operation: The AWS Access Key Id you provided does not exist in our records.

Mmm, that's interesting. What is going wrong? Aha, I made a copy/paste error: in the .env I still had the ```python os.environ.get ``` where I should have the key directly. 

Try again: yes, it works!

Well, partially: uploading files works, I can see them appearing in the S3 bucket, but clicking on the file in the admin console gives me the same error every time I try: 
```
<Code>SignatureDoesNotMatch</Code>
<Message>The request signature we calculated does not match the signature you provided. Check your key and signing method.</Message>
```

There are different messages to be found on this error, one of them being: just wait, it will work after a day.
Another one: your key gets malformed if it contains certain characters.

But the real solution turned out the be this line, to be added to SETTINGS:
```
AWS_S3_ADDRESSING_STYLE = "virtual"
```
And just like that, it works!
