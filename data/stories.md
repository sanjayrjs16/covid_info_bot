
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
* mail_me
    - action_check_userinfo
* give_user_info{"name":"Rodrigo"}
    - user_info
    - form{"name":"user_info"}
    - form{"name":null}
    - utter_userinfo_thank
*thank_bot
    - utter_noworries
* goodbye
    - utter_goodbye
    

## what is corona
* corona_intro
  - utter_corona_intro
  
## how does corona spread
* corona_spread
  - utter_corona_spread
## corona food spread
* corona_food_spread
  - utter_corona_food_spread

## corona warm weather
* warm_weather
  - utter_warm_weather
## corona high risk
* high_risk
   - utter_high_risk