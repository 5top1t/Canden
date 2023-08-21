# Canden

Ever wanted to create a calendar or event for a concert, sport team, artist tour, trash collections give Canden a try. Canden creates calendar events from a webpage so you never miss what is important.

In the example, we create a calendar from the team USA basketball schedule <https://www.usab.com/teams/5x5-mens-world-cup/schedules>.

### Roadmap

- [x]  Try to build in java
  - Setting up maven on my own is too complex
- [x]  Scope the effort (2 days)
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

### Similar products

[Stanza](https://www.stanza.co/?&search=nba-warriors&goT=feature)

### Objective

Allow users to add events from a webpage to a calendar

Features

- Get events from a webpage
- Save events to a google calender
- Create a google calendar from a list of events

### Design

Google calendar API - support getting calendars and creating calendars with permissions based on the webpage. Needs to be tested. ics file format represents a calendar where the events are list in chronological order

[API Reference  |  Google Calendar  |  Google for Developers](https://developers.google.com/calendar/api/v3/reference)

[](https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md)

CadenCalendarService

- Search goggle calendar
- Get google calendar by id

### GoogleAPIClient

API connections are not support Oauth is required

```python
googleapiclient.errors.HttpError: <HttpError 401 when requesting https://www.googleapis.com/calendar/v3/users/me/calendarList?key=AIzaSyCAHNx-w6U3OEV3ypTpAeM8TCZgnPpIeGE&alt=json returned "API keys are not supported by this API. Expected OAuth2 access token or other authentication credentials that assert a principal. See https://cloud.google.com/docs/authentication". Details: "[{'message': 'Login Required.', 'domain': 'global', 'reason': 'required', 'location': 'Authorization', 'locationType': 'header'}]"
```

[](https://console.cloud.google.com/apis/credentials?project=canden)

**Minimum required scopes**

[Choose Google Calendar API scopes  |  Google for Developers](https://developers.google.com/calendar/api/auth)

- Calendar API
- <https://www.googleapis.com/auth/calendar> scope - See, edit, share, and permanently delete all the calendars you can access using Google Calendar.

************************************Sharing a calendar************************************

Approaches

1. Sharable link available to the user
2. Require users to sign in and insert a new copy in their calendar

It seems sharing a calendar requires manual from the web app and cannot be done via the API. When sharing a calendar the app displays a public link of the form:

```jsx
https://calendar.google.com/calendar/u/0?cid={{unique_cid}}
```

One solutions would be to building the sharable link and create the calendar as public. However, it seems the `cid` does not match any of the fields available on the [calendar](https://developers.google.com/calendar/api/v3/reference/calendars). Since this application will be deploy on a server navigating the web app is not feasible.

Approach #2 seems to be the winner.

### Scrapping the internet

[Schedules -  USA Basketball Men's World Cup Team - USA Basketball](https://www.usab.com/teams/5x5-mens-world-cup/schedules)

******************Prompting******************

Using a simple chat gpt prompt such as

`use python and beautifulsoup to get the game schedule from https://www.usab.com/teams/5x5-mens-world-cup/schedules`

does not work. Check github commits for solution.

********************************Prompting with div.font-title********************************

Using a simple chat gpt prompt such as

`use python and beautifulsoup to get the game schedule from the sub elements of div.font-title on https://www.usab.com/teams/5x5-mens-world-cup/schedules website`

It requires pasting the HTML body for closer inspection which is too long.

****************************************************************************************Modify the original script for the Fiba page****************************************************************************************

Inspecting the result, it seems the dates info is loaded using a script. The raw HTML file does not contain the desired element and class. This conclusion comes from inspecting the python request.content

**Selenium web driver**

[How to Scrape JavaScript-Rendered Web Pages with Python](https://www.zenrows.com/blog/scraping-javascript-rendered-web-pages#requirements)

Using a Selenium web driver will our the script to parse the DOM after the javascript schedule content is loaded.
