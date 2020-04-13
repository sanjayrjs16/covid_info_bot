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
                                         intent=["give_name"]),
                "email": self.from_entity(entity="email",
                                          intent=["give_email"]),
                "pincode": self.from_entity(entity="pincode",
                                            intent=["give_pincode"]),
                "mobnumber": self.from_entity(entity="mobnumber",
                                               intent=["give_mobnumber"])}

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
