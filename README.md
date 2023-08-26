# Canden

Ever wanted to create a calendar or event for a concert, sport team, artist tour, trash collections give Canden a try. Canden creates calendar events from a webpage so you never miss what is important.

In the example, we create a calendar from the team USA basketball schedule <https://www.usab.com/teams/5x5-mens-world-cup/schedules>.

⚠️ : represents potential issues  
✅: represents the approach used in code


## Existing products

[Stanza](https://www.stanza.co/?&search=nba-warriors&goT=feature) is an existing product that allows users to sync events, sports, shows, etc schedules to their calendars. However not all events are in Stanza such as the Team USA mens basketball schedule. Canden is another to quickly add events to calendar once you know which HTML elements hold the date and info on the websites.

## Roadmap

- [x]  Try to build in java
  - Setting up maven on my own is too complex
- [x]  Scope the effort
  - [x]  Design
  - [x]  Test the Google Calendar API
  - [x]  Find website tags
  - [x]  Roadmap
- [x]  Set up GoogleCalendar and Fetch all calendars
  - [x]  Create a calendar
  - [x]  Create an event on the calendar
  - [x]  Storing the calendar key as “name” vs “id”
- [x]  Parse webpage for dates and event name
  - [x]  BS4
  - [x]  Selenium
- [x]  Create a main file to seal the deal
  - [x]  Move the timezone to the main file

## References

- [Google Calendar API scopes  |  Google for Developers](https://developers.google.com/calendar/api/auth)
- [Selenium docs](https://selenium-python.readthedocs.io/index.html)
- [Beautiful Soup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [How to S***pe JavaScript-Rendered Web Pages with Python](https://www.zenrows.com/blog/scraping-javascript-rendered-web-pages#requirements)

## Design

Allow users to add events from a webpage to a calendar. Write some python scripts to get the schedule from the website and insert events to Google Calendar.

- Get events from a webpage
- Create a google calendar from a list of events

### GoogleAPIClient

Get started with [Google Calendar Client](https://developers.google.com/calendar/api/quickstart/python) in python. 

#### ⚠️ API Key Auth

API Auth connections are not supported so we need to set up a Oauth Client.

```python
googleapiclient.errors.HttpError: <HttpError 401 when requesting https://www.googleapis.com/calendar/v3/users/me/calendarList?key=AIzaSyCAHNx-w6U3OEV3ypTpAeM8TCZgnPpIeGE&alt=json returned "API keys are not supported by this API. Expected OAuth2 access token or other authentication credentials that assert a principal. See https://cloud.google.com/docs/authentication". Details: "[{'message': 'Login Required.', 'domain': 'global', 'reason': 'required', 'location': 'Authorization', 'locationType': 'header'}]"
```

#### ✅ Oauth 2.0 Client Id

- Create a project in GCP and add Google Calendar to the project
- Set up an OathClient and copy the client_secrets.json to the root of the project
- python oauth2client will look for the secrets file to connect to the project

### S***ping the website

Read the game schedule from the team website - [Schedules -  USA Basketball Men's World Cup Team - USA Basketball](https://www.usab.com/teams/5x5-mens-world-cup/schedules)

Approaches

- ⚠️ Use chat gpt prompt to do the grunt work - `use python and beautifulsoup to get the game schedule from https://www.usab.com/teams/5x5-mens-world-cup/schedules` does not work. Check github commits for solution.

- ⚠️ ChatGPT chose the wrong element so specify the elements in the prompt. Using a simple chat gpt prompt such as `use python and beautifulsoup to get the game schedule from the sub elements of div.font-title on https://www.usab.com/teams/5x5-mens-world-cup/schedules website`
- ✅ Inspecting the result, it seems the dates info is loaded using a script tag. On page load the HTML body may not contain the desired element and class. This conclusion comes from inspecting the python `request.content`. We can use **selenium** to load the page and then get the schedule using bs4.
