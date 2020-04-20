
## bot challenge
* start
    - utter_whoami
    - utter_bot_function
* bot_challenge
    - utter_whoami
    - utter_bot_function
* goodbye
    - utter_goodbye

##user info happy path with greet
* start
    - utter_whoami
    - utter_bot_function
* greet
    - utter_greet
    - utter_bot_function
* ask_worldwide
    - action_cases_worldwide
    - utter_bot_function
* ask_countrywise
    - action_cases_countrywise
    - utter_bot_function
* ask_visual
    - action_fetch_visual
    - utter_bot_function
* mail_me
    - action_check_userinfo
* give_user_info{"name":"Rodrigo"}
    - user_info
    - form{"name":"user_info"}
    - form{"name":null}
    - utter_userinfo_thank
*thank_bot
    - utter_noworries
    - utter_bot_function
* goodbye
    - utter_goodbye
    

## what is corona
* corona_intro
  - utter_corona_intro
  - utter_bot_function
  
## how does corona spread
* corona_spread
  - utter_corona_spread
  - utter_bot_function
## corona food spread
* corona_food_spread
  - utter_corona_food_spread
  - utter_bot_function

## corona warm weather
* warm_weather
  - utter_warm_weather
  - utter_bot_function
## corona high risk
* high_risk
   - utter_high_risk
   - utter_bot_function
## corona symptom check
*covid_symptom_doubt
   - utter_symptom_check_link
   - utter_bot_function
   
## user_info unhappy path
* start
    - utter_whoami
    - utter_bot_function
* mail_me
    - action_check_userinfo
    - followup{"name": "user_info"}
    - user_info
    - form{"name": "user_info"}
    - slot{"requested_slot": "name"}
* deny
    - utter_userinfo_reaffirm
    - utter_bot_function
* mail_me
    - action_check_userinfo
    - action_listen
    - form: followup{"name": "user_info"}
    - user_info
    - slot{"requested_slot": "name"}
* form: give_user_info{"name": "Sanjay"}
    - slot{"name": "Sanjay"}
    - form: user_info
    - slot{"name": "Sanjay"}
    - slot{"requested_slot": "email"}
* deny
    - utter_userinfo_reaffirm
    - utter_bot_function
* mail_me
    - action_check_userinfo
    - action_listen
    - form: followup{"name": "user_info"}
    - user_info
    - slot{"requested_slot": "email"}
* form: give_user_info{"email": "sanjayrjs16@gmail.com"}
    - slot{"email": "sanjayrjs16@gmail.com"}
    - form: user_info
    - slot{"email": "sanjayrjs16@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_userinfo_thank
    - utter_bot_function
* covid_symptom_doubt
    - utter_symptom_check_link
    - utter_bot_function
* goodbye
    - utter_goodbye
