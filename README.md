A framework for neuroscience experiments on the web.

# Introduction

...

# Installation

...

- Clone this github repo (see link on this page).

## OpenShift

This application is ready to be deployed to OpenShift.

- Register an account [here](https://www.openshift.com/).
- Create an application and add the "Python 3.3 cartridge".
- Set up your log-in credentials (public SSH keys) if you want.
- Install the RHC client on your computer with `gem install rhc` (requires Ruby).
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

# Links

- https://github.com/johnmcdonnell/psiTurk
- http://experimentalturk.wordpress.com/2013/04/22/turkgate/
- http://gureckislab.org/blog/?p=2557
- http://xcorr.net/2013/04/17/evaluating-ides-for-scientific-python/
