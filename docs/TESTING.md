# Testing Guide

Run the unit tests:

~~~bash
pip install -r requirements.txt
pytest -q
~~~

Recommended manual checks:

- Confirm the dashboard loads.
- Submit a sample POST /api/analyze request.
- Confirm the finding appears in /api/findings and the dashboard table.
