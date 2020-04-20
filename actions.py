# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from __future__ import unicode_literals

from pathlib import Path
from typing import Any, Text, Dict, List

import os
import requests
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup as bs
import fitz
from imgurpython import ImgurClient

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, FollowupAction


def scrape_url():  # This function srapes the pdf from WHO website
    whourl = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports"
    resp = requests.get(whourl)
    whopage = resp.text
    who_html = bs(whopage, "html.parser")
    doc_url = who_html.find("div", attrs={"class": "sf_colsIn col-md-10"}).div.div.p.a['href']
    finalurl = "https://www.who.int" + doc_url
    return finalurl


def imageuploader():  # This function uploades the image from  the pdf to imgur
    client_id = '9d213e9aa66dc00'
    client_secret = '2d7eb20e11df6e8ae52046706d04b20a63d668d4'

    client = ImgurClient(client_id, client_secret)
    link = client.upload_from_path("p1.png", config=None, anon=True)
    return link['link']


def getpdf():  # THis function is, used to scrape image from pdf.

    filename = Path('worldviz.pdf')
    finalurl = scrape_url()
    response = requests.get(finalurl)
    filename.write_bytes(response.content)

    doc = fitz.open(filename)
    imglist = doc.getPageImageList(0)
    img = imglist[1]
    xref = img[0]
    pix = fitz.Pixmap(doc, xref)
    if pix.n < 5:  # this is GRAY or RGB

        pix.writePNG("p1.png")

    else:  # CMYK: convert to RGB first
        pix1 = fitz.Pixmap(fitz.csRGB, pix)

        pix1.writePNG("p1.png")
        pix1 = None
        pix = None


def sent_email(usermail, username):
    finalurl = scrape_url()
    botmail = 'covidinfobot@gmail.com'
    passwd = 'testbot#1'
    msg = EmailMessage()
    msg['Subject'] = 'Covid latest reports and preventive measures.'
    msg['From'] = botmail
    msg['To'] = usermail
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <p>Hello {username},<br/>
            You are receiving this mail as per your request, via chat.</p>
            <h4>Check latest reports worldwide via this link :{finalurl}"</h4>
            <h4 style="color:SlateGray;">Preventive measures againt Covid19.</h4>
            <img src="https://www.unicef.org/bangladesh/sites/unicef.org.bangladesh/files/Dos%20and%20Dont%27s.png">
            <p>Data source: UNICEF, WHO</p>
            <h4> Stay safe, <br/>       
                         - covidinfobot</h4>
            <h6>(Powered by Rasa)</h6>
        </body>
    </html>
    """.format(username=username, finalurl=finalurl), subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(botmail, passwd)
        smtp.send_message(msg)


def call_api(select, country):  # This is to configure the api and fetch cases details.
    url = "https://covid-19-data.p.rapidapi.com/"
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "ca525b0b4amshd1cc1be598c5872p16788bjsn91429d8e8683"
    }
    if select == "world":
        url = url + "totals"
    else:
        url = url + "country"
    if country is None:
        querystring = {"format": "json"}
    else:
        querystring = {"format": "json", "name": country}

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


class ActionFetchVisual(Action):

    def name(self) -> Text:
        return "action_fetch_visual"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Please wait a moment....Fetching data...")
        link = imageuploader()
        dispatcher.utter_message(image=link)
        dispatcher.utter_message(text="This is the latest world map visual from WHO website.")
        return []


class ActionCasesWorldwide(Action):

    def name(self) -> Text:
        return "action_cases_worldwide"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = call_api("world", None)
        dispatcher.utter_message(text="World wide reports : ")
        for key in ("confirmed", "recovered", "critical", "deaths"):
            dispatcher.utter_message("{} : {}".format(key, response[0][key]))

        return []


class ActionCasesCountrywise(Action):

    def name(self) -> Text:
        return "action_cases_countrywise"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        country = tracker.latest_message['entities'][0]['value']
        response = call_api("country", country)
        dispatcher.utter_message(text="Latest reports from {}:".format(country))
        for key in ("confirmed", "recovered", "critical", "deaths"):
            dispatcher.utter_message("{} : {}".format(key, response[0][key]))

        return []


class ActionCheckUserInfo(Action):

    def name(self) -> Text:
        return "action_check_userinfo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        flag = 0
        for key in ("name", "email"):
            value = tracker.get_slot(key)
            if value is None:  # this is how to check if slot value is filled or not.
                dispatcher.utter_message(text="I don't have your details yet.")
                return [FollowupAction("user_info")]

        usermail = tracker.get_slot("email")
        username = tracker.get_slot("name")
        dispatcher.utter_message(text="Please wait a moment....")
        sent_email(usermail, username)
        dispatcher.utter_message(text="You will receive a mail from me shortly.Stay safe ! :)")
        return []


class ActionSessionStart(Action):  # This function is to override the session start action
    def name(self) -> Text:
        return "action_session_start"  # This name function returns the name of the custom action.Here is is
        # action_session_start

    @staticmethod
    def fetch_slots(tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and phone number."""

        slots = []

        for key in ("name", "email", "pincode", "mobnumber"):
            value = tracker.get_slot(key)
            if value is not None:  # this is how to check if slot value is filled or not.
                slots.append(SlotSet(key=key, value=value))

        return slots

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        #
        # # any slots that should be carried over should come after the
        # # `session_started` event
        events.extend(self.fetch_slots(tracker))
        #
        # # an `action_listen` should be added at the end as a user message follows
        dispatcher.utter_message(template="utter_bot_function")
        events.append(ActionExecuted("action_listen"))
        #

        return events


class UserInfo(FormAction):  # This form collects user info

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "user_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["name", "email"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"name": self.from_entity(entity="name",
                                         intent=["give_user_info", "greet"]),
                "email": self.from_entity(entity="email",
                                          intent=["give_user_info"]),
                "pincode": self.from_entity(entity="pincode",
                                            intent=["give_user_info"]),
                "mobnumber": self.from_entity(entity="mobnumber",
                                              intent=["give_user_info"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        name = tracker.get_slot('name')
        email = tracker.get_slot('email')
        # pin = tracker.get_slot('pincode')
        # mob = tracker.get_slot('mobnumber')

        dispatcher.utter_message(
            "Your details name:  {}, email id: {}".format(name,
                                                          email))

        dispatcher.utter_message(text="Please wait a moment....")
        sent_email(email, name)
        dispatcher.utter_message(text="You will receive a mail from me shortly.Stay safe ! :)")
        return []
