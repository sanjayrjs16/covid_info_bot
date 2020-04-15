## unhappy_path_1
* start
    - utter_bot_function
* greet
    - utter_ask_name
* deny
    - utter_userinfo_reaffirm
* give_user_info{"name": "Shiva"}
    - slot{"name": "Shiva"}
    - user_info
    - form{"name": "user_info"}
    - slot{"name": "Shiva"}
    - slot{"name": "Shiva"}
    - slot{"requested_slot": "email"}
    - utter_ask_email
* deny
    - utter_userinfo_reaffirm
    - action_listen
* form: give_user_info{"email": "shiva32a@yahoo.com"}
    - slot{"email": "shiva32a@yahoo.com"}
    - user_info
    - slot{"email": "shiva32a@yahoo.com"}
    - slot{"requested_slot": "pincode"}
* deny
    - utter_userinfo_reaffirm
    - action_listen
* form: give_user_info{"pincode": "363244"}
    - slot{"pincode": "363244"}
    - user_info
    - slot{"pincode": "363244"}
    - slot{"requested_slot": "mobnumber"}
* deny
    - utter_userinfo_reaffirm
    - action_listen
* form: give_user_info{"mobnumber": "9943556600"}
    - slot{"mobnumber": "9943556600"}
    - user_info
    - slot{"mobnumber": "9943556600"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_userinfo_thank
* goodbye

## bot challenge
* start
    - utter_bot_function
* bot_challenge
  - utter_iamabot
* goodbye
    - utter_goodbye

## happy path
* start
    - utter_bot_function
* greet
    - utter_ask_name
* give_user_info{"name":"Rodrigo"}
    - user_info
    - form{"name":"user_info"}
    - form{"name":null}
    - utter_userinfo_thank
* goodbye
    - utter_goodbye
