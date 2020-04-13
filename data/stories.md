
## say goodbye
* greet
  - utter_greet_ask
* give_name{"name" : "Baljith"}
  - user_info
  - form{"name":"user_info"}
  - form{"name": null}
* goodbye
  - utter_goodbye
  

## bot challenge
* greet
  - utter_greet_ask
* give_name{"name" : "Baljith"}
  - user_info
  - form{"name":"user_info"}
  - form{"name": null}
* bot_challenge
  - utter_iamabot



## interactive_story_1_unhappy_path
* greet
    - utter_greet_ask
* deny
    - utter_userinfo_reaffirm
* deny
    - user_info
    - form{"name": "user_info"}
    - slot{"requested_slot": "name"}
* form: give_name{"name": "Erlich"}
    - slot{"name": "Erlich"}
    - form: user_info
    - slot{"name": "Erlich"}
    - slot{"requested_slot": "email"}
* deny
    - utter_userinfo_reaffirm
    - action_listen
* form: give_email{"email": "erlichbachman72@aviato.com"}
    - slot{"email": "erlichbachman72@aviato.com"}
    - user_info
    - slot{"email": "erlichbachman72@aviato.com"}
    - slot{"requested_slot": "pincode"}
    - utter_ask_pincode
* deny
    - user_info
    - slot{"requested_slot": "pincode"}
    - utter_userinfo_reaffirm
    - action_listen
* form: give_pincode{"pincode": "603010"}
    - slot{"pincode": "603010"}
    - user_info
    - slot{"pincode": "603010"}
    - slot{"requested_slot": "mobnumber"}
    - utter_ask_mobnumber
    - action_listen
* form: give_mobile{"mobnumber": "9447277030"}
    - slot{"mobnumber": "9447277030"}
    - user_info
    - slot{"mobnumber": "9447277030"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_userinfo_thank
* goodbye
    - utter_goodbye

## interactive_story_1_Happy_path
* greet
    - utter_greet_ask
* give_name{"name": "bachmann"}
    - slot{"name": "bachmann"}
    - user_info
    - form{"name": "user_info"}
    - slot{"name": "bachmann"}
    - slot{"name": "bachmann"}
    - slot{"requested_slot": "email"}
    - utter_ask_email
    - action_listen
* form: give_email{"email": "nitin_cool123@hotmail.net"}
    - slot{"email": "nitin_cool123@hotmail.net"}
    - user_info
    - slot{"email": "nitin_cool123@hotmail.net"}
    - slot{"requested_slot": "pincode"}
    - utter_ask_pincode
    - action_listen
* form: give_pincode{"pincode": "680008"}
    - slot{"pincode": "680008"}
    - user_info
    - slot{"pincode": "680008"}
    - slot{"requested_slot": "mobnumber"}
    - utter_ask_mobnumber
    - action_listen
* form: give_mobile{"mobnumber": "9496347600"}
    - slot{"mobnumber": "9496347600"}
    - user_info
    - slot{"mobnumber": "9496347600"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_userinfo_thank
* thank_bot
    - utter_noworries
* goodbye
    - utter_goodbye

## interactive_story_1_happy_path_2
* greet
    - utter_greet_ask
* give_name{"name": "harper"}
    - slot{"name": "harper"}
    - user_info
    - form{"name": "user_info"}
    - slot{"name": "harper"}
    - slot{"name": "harper"}
    - slot{"requested_slot": "email"}
* form: give_email{"email": "pricesscool@gmail.com"}
    - slot{"email": "pricesscool@gmail.com"}
    - form: user_info
    - slot{"email": "pricesscool@gmail.com"}
    - slot{"requested_slot": "pincode"}
* form: give_pincode{"pincode": "657833"}
    - slot{"pincode": "657833"}
    - form: user_info
    - slot{"pincode": "657833"}
    - slot{"requested_slot": "mobnumber"}
    - utter_ask_mobnumber
    - action_listen
* form: give_mobile{"mobnumber": "9236478236"}
    - slot{"mobnumber": "9236478236"}
    - user_info
    - slot{"mobnumber": "9236478236"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_userinfo_thank
* bot_challenge
    - utter_iamabot
* bot_challenge
    - utter_iamabot
* bot_challenge
    - utter_iamabot
* goodbye
    - utter_goodbye