A framework for neuroscience experiments on the web.

# Introduction

We are using Amazon Turk to get people involved in the experiment, but it must be hosted somewhere. It could have been done at Amazon servers, but we opted for [OpenShift](https://www.openshift.com/) after a recent lock-in problem with App Engine. See [OpenShift vs App Engine](http://blog.yeradis.com/2012/11/hello-red-hat-openshift-bye-bye-google.html). The source code is available for a local installation [here](http://openshift.github.io/).

# Installation

...

- Clone this github repo (see link on this page).

## OpenShift

This application is ready to be deployed to OpenShift.

- Register an account [here](https://www.openshift.com/).
- Create an application and add the "Python 3.3 cartridge".
- Set up your log-in credentials (public SSH keys) if you want.
- Install the [RHC client](https://www.openshift.com/developers/rhc-client-tools-install) on your computer
- See the second half of [this article](https://www.openshift.com/blogs/look-ma-no-hands-developing-for-the-cloud-in-the-cloud-with-cloud9-ide), the site is updated on each push to openshift.

## Locally

Alternatively, you can use it directly on your computer or personal server.

After installing Python 3 on your OS, run these commands:

```
pyvenv virtenv
source virtenv/bin/activate
pip install django
python neuro-turk/wsgi/neuroturk/manage.py runserver
```

Now follow this link: http://localhost:8000/

**TODO**: add local server info with WebOb/etc

# Links

- https://github.com/johnmcdonnell/psiTurk
- http://experimentalturk.wordpress.com/2013/04/22/turkgate/
- http://gureckislab.org/blog/?p=2557
- http://xcorr.net/2013/04/17/evaluating-ides-for-scientific-python/
- http://www.psychopy.org/
