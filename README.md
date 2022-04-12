# DevOps at Deepgram

Thanks for your interest in devops at Deepgram! This is a template project that we will experiment
with during your on-site interview.

# Setup and Installation

Create/activate a virtual environment, then:

```bash
$ pip install -e .
```

An obsolete way of installing is:

```bash
$ python setup.py install
```

And an obsolete way of install dependencies is:

```bash
$ pip install -r requirements.txt
```

# Running the Service

```bash
$ gram
```

# Description

The project is a simple web server, powered by the Tornado web framework.

To register a new route handlers, we derive from Tornado's `RequestHandler`.
Shared application state can be handed off to Tornado when the request handlers
are registered. Registration occurs in `src/gram/__main__.py:main`.

We create a custom global state object (`State`), defined in `src/gram/state.py`. This can be used
for holding global application state (number of active requests, etc.).

In order to make dependency injection easy, we create our own base class for our request handlers.
This `BaseHandler`, defined in `src/gram/handlers/__init__.py`, derives from Tornado's
`RequestHandler`. This centralizes some simple tasks, such as reporting to the `Status` object,
which helps us not to repeat ourselves.

The handlers themselves live in `src/gram/handlers` and do a number of things:

- `/` (`MainHandler`): just returns a static message with a 200 response code.
- `/sleep/{sleep}` (`SleepHandler`): sleeps for `sleep` milliseconds and then returns a 200.
- `/code/{code}` (`CodeHandler`): immediately returns a `code` status code.
- `/work` (`WorkHandler`): mimics a fallible workload by sleeping for a random duration and then
  returning a weighted, random status code.
- `/status` (`StatusHandler`): a TODO handler for querying service metrics.
- `/health` (`HealthHandler`): a TODO handler for returning service health.

# Docker

A Dockerfile is provided for containerizing the service. To build it:

```
$ docker build -t deepgram/devops-onsite:latest .
```

And to run it:

```
$ docker run --rm -p 8080:8080 deepgram/devops-onsite:latest
```

# Tests

This is set up for testing using `pytest`.

First, install `pytest`:

```bash
$ pip install pytest
```

Then you can do:

```bash
$ pytest
```

or

```bash
$ python -m pytest
```
