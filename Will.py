#!/bin/python3

response_code_for_valid_questions = {"what is your name?":"name"}
array_of_invalid_questions = {}
# to register invalid questions requested by users
action_code_for_valid_actions = { "bye!":"exit",
                                  "test!":"run_test"}
array_of_invalid_actions = {} 
# to register invalid actions requested by users
answers_from_response_code = {"name":"Will Caster (Transcendence)",
                    "exit":"Good Bye cya!!",
                    "run_test":"Running test..."}




def is_question(ut):
  if ut.endswith('?'):
    return True;
  return False

def is_action(ut):
  if ut.endswith('!'):
    return True
  return False

def get_action_code_for(ut):
  if len(ut) >1:
    if is_question(ut):
      return response_code_for_valid_questions[ut]
      # compare string with collection of question
      # if the text entered is a question only then it will reply
      
    if is_action(ut):
      return action_code_for_valid_actions[ut]
      # compare string with collection of action commands
      # if the text entered is a action only then it will reply
    return "Not Registered"
  else:
    return "invalid"
  
def get_response_code_for(ut):
  if len(ut) >1:
    if is_question(ut):
      return response_code_for_valid_questions[ut]
      # compare string with collection of question
      # if the text entered is a question only then it will reply
      
    if is_action(ut):
      return action_code_for_valid_actions[ut]
      # compare string with collection of action commands
      # if the text entered is a action only then it will reply
      
    return "Not Registered"
  else:
    return "invalid"
    
def reply(r_c):
  if not r_c in answers_from_response_code:
    return("I don't understand :(")
  return(answers_from_response_code[r_c])

def action(a_c):
  if a_c == 'exit':
    exit()
  elif a_c == 'run_test':
    run_test()

def run_test():
  inputs = ['what is your name?',
            'help me',
            '?',
            '!',
            'bye!']
  outputs = ['Will Caster (Transcendence)',
            'Not Registered',
            'invalid',
            'invalid',
            'Good Bye cya!!']
            
  test_case_count = 0
  for i in inputs:    
    print("\n" + str(test_case_count) + "\t:>" + i)
    r_c = get_response_code_for(i)
    print("\tresponse code: " + r_c)
    a_c = get_action_code_for(i)
    print("\taction code: " + a_c)
    r = reply(r_c)
    print("\toutput: " + r)
    print("\texpected-output: " + str(outputs[test_case_count]), end=" ")
    if r == outputs[test_case_count]:
      print("...PASSED")
    else:
      print("...FAILED")
    test_case_count += 1
    # compare utput and Print passed
  
  
def run_code():
  while True:
    user_entered_text = str(input(":>"))

    response_code = get_response_code_for(user_entered_text)
    # response_code is a number that help me deciding what to reply 

    # get_response_code_for() function checks parameter string from array of 
    # dictionary 


    action_code = get_action_code_for(user_entered_text)
    # action_code is a number that help me deciding what to do 

    # get_action_code_for() function checks parameter string from array of 
    # dictionary


    print(reply(response_code))
    clear()
    action(action_code)




run_test()
