
## happy path
* greet
  - utter_greet_ask
* give_user_info{"name" : "Baljith"}
  - user_info
  - form{"name":"user_info"}
  - form{"name": null}
  - utter_userinfo_thank
* goodbye
  - utter_goodbye
  

## unhappy_path_1
* greet
    - utter_greet_ask
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
* bot_challenge
  - utter_iamabot
* goodbye
    - utter_goodbye
