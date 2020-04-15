# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType


#
# class ActionLocation(Action):
#
#     def name(self) -> Text:
#         return "action_location"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="You asked for location with higher no. of cases.")
#
#         return []

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"  # This name function returns the name of the custom action.Here is is action_session_start

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
        # events.extend(self.fetch_slots(tracker))
        #
        # # an `action_listen` should be added at the end as a user message follows
        dispatcher.utter_message(template="utter_greet_ask")
        events.append(ActionExecuted("action_listen"))
        #

        return events


class UserInfo(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "user_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["name", "email", "pincode", "mobnumber"]

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
        pin = tracker.get_slot('pincode')
        mob = tracker.get_slot('mobnumber')
        # utter submit template
        dispatcher.utter_message(
            "Hey, your name is {} , email id : {} , pincode is {} , maobile number is {}".format(name.title(),
                                                                                                 email.title(),
                                                                                                 pin.title(),
                                                                                                 mob.title()))
        return []
